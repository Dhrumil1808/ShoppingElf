import subprocess
import re
import shlex
import ast
import ReceiptService as receiptService;
from Models import BillReceipt
from Models import BillItem
from Models import User

class ImageProcessor:
	username = None
	filename = None
	billDate = None

	def __init__(self,username,filename,billDate):
		self.username = username
		self.filename = filename
		self.billDate= billDate

	def getImageContents(self):
		print "processing Image"
		try:
			proc = subprocess.Popen(['python', 'pytesseract.py',  'uploads/'+self.filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			#print proc.communicate()[0]
			print "running pytessarct"
			originalOutput = proc.communicate()[0]
			originalString = str(originalOutput)
		except:
			return 'pytesseract processing error'

		try:
			print originalString
			items = [];
			groupBynewLine = re.split(r'[\n\r]+', originalString)
			# del groupBynewLine[0]
			# del groupBynewLine[0]
			# del groupBynewLine[0]

			print groupBynewLine

			dict1 = {}
			dict2 = {}
			counter = 0
			support = 1
			for i in groupBynewLine:
				if len(i) > 0:
					if not i[0].isdigit():
						#i_update = ''.join(e for e in i if e.isalnum())
						i_update = re.sub(r'([^\s\w]|_)+', '', i)
						if i_update:
							dict1[counter]=i_update
							support = 1
						else:
							support = 0
					else:
						dict2[counter-1]=i
						support = 1

				if support == 1:
					counter+=1
				# if not re.search(r"(\d+)", i):
				
			print '1111111'
			print dict1
			print '2222222'
			print dict2

			dc = {}
			for i,j in dict1.items():
				dc[j]=1
				for p,q in dict2.items():
					if i==p:
						dc[j]=q

			discardWords = ['PRODUCE','DAIRY','']
			for p1,q1 in dc.items():
				if p1 in discardWords:
					del dc[p1]
			print '3333333'
			print dc
		except:
			print 'basic logical error'
			return 'please correct input image'

		try:
			for i1,j1 in dc.items():
				if isinstance(j1, int):
					dc[i1]=j1
				else:
					k1=shlex.split(j1)[0]
					dc[i1]=k1
		except:
			return 'please correct input image'

		#create bill receipt_data
		try:
			user = receiptService.findUser(self.username)
			print user
		except:
			return 'please correct the user'

		products = []

		print dc

		try:
			for k, v in dc.items():
				v1 = re.findall(r'\d+', str(v))
				print "k1:"
				print k
				print "v1:"
				print v1

				if len(v1) > 0:
					finalv = float(str(v1[0]))
				else:
					finalv = 1
				print finalv

				billItem = BillItem (k,finalv);
				products.append(k);
				items.append(billItem);
			billReceipt = BillReceipt (self.username,items,self.billDate,user.family_members);
			print "saving receipts!"
			receiptService.addUserReciept(billReceipt);
			receiptService.addProducts(products);
		except:
			return 'please correct input image'

		mlist = []
		count = 0
		for i,j in dc.items():
			ma1 = {}
			print i
			print j
			ma1['product'] = i
			ma1['qty'] = j
			mlist.insert(count,ma1)
			count+=1

		try:
		#call script
			cronProcess = subprocess.Popen(['nohup','python', '../ml-cron/cron.py'], stdout=subprocess.PIPE,
								stderr=subprocess.STDOUT)
			output = cronProcess.communicate()[0]
			originalString = str(output)
			print originalString
		except:
			print 'cron.py error'

		return mlist