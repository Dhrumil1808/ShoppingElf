import subprocess
import re
import shlex
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

		dic1 = {}
		dic2 = {}
		counter = 0
		for i in groupBynewLine:
			if not re.search(r"(\d+)", i):
				dic1[counter]=i
			else:
				dic2[counter-1]=i
			print i
			counter+=1

		# print '1111111'
		# print dic1
		# print '2222222'
		# print dic2

		dic = {}
		for i,j in dic1.items():
			dic[j]=1
			for p,q in dic2.items():
				if i==p:
					dic[j]=q

		discardWords = ['PRODUCE','DAIRY','']
		for p1,q1 in dic.items():
			if p1 in discardWords:
				del dic[p1]
		# print '3333333'
		# print dic

		for i1,j1 in dic.items():
			if isinstance(j1, int):
				dic[i1]=j1
			else:
				k1=shlex.split(j1)[0]
				dic[i1]=k1

		#create bill receipt_data

		user = receiptService.findUser(self.username)
		products = [];
		for k, v in dic.items():
			print v
			billItem = BillItem (k,float(v));
			products.append(k);
			items.append(billItem);
		billReceipt = BillReceipt (self.username,items,self.billDate,user.family_members);
		receiptService.addUserReciept(billReceipt);
		receiptService.addProducts(products);

		return dic
