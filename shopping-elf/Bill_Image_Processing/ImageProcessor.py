import subprocess
import re
import shlex
import re
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
		proc = subprocess.Popen(['python', 'pytesseract.py',  'uploads/'+self.filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		#print proc.communicate()[0]

		originalOutput = proc.communicate()[0]
		originalString = str(originalOutput)
		#print originalString
		items = [];
		groupBynewLine = re.split(r'[\n\r]+', originalString)
		del groupBynewLine[0]
		del groupBynewLine[0]
		del groupBynewLine[0]

		dict1 = {}
		dict2 = {}
		counter = 0
		for i in groupBynewLine:
			if not re.search(r"(\d+)", i):
				dict1[counter]=i
			else:
				dict2[counter-1]=i
			# print i
			counter+=1

		# print '1111111'
		# print dict1
		# print '2222222'
		# print dict2

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
		# print '3333333'
		# print dc

		for i1,j1 in dc.items():
			if isinstance(j1, int):
				dc[i1]=j1
			else:
				k1=shlex.split(j1)[0]
				dc[i1]=k1

		#create bill receipt_data
		user = receiptService.findUser(self.username)
		print user
		products = [];
		for k, v in dc.items():
			print v
			billItem = BillItem (k,float(v));
			products.append(k);
			if v=='':
				v='1'
			v1 = re.sub("\D", "", str(v))
			# print "v1:"
			# print v1
			# print "v:"
			# print v
			#v1 = ast.literal_eval(v)
			#v = filter(lambda x: x.isdigit(), v)
			# billItem = BillItem (k,float(v1));
			items.append(billItem);
		billReceipt = BillReceipt (self.username,items,self.billDate,user.family_members);
		receiptService.addUserReciept(billReceipt);
		receiptService.addProducts(products);

		return dc
