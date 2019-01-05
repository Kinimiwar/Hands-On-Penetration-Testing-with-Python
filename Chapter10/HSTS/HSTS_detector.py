import requests

class Detect_HSTS():
	def __init__(self,target):
		self.target=target

	def start(self):
		try:
			resp=requests.get(self.target)
			headers=resp.headers
			print ("\n\nHeaders set are : \n" )
			for k,v in headers.iteritems():
				print(k+":"+v)

			if "Strict-Transport-Security" in headers.keys():
				print("\n\nHSTS Header present")
			else:
				print("\n\nStrict-Transport-Security is missing ! ")

		except Exception as ex:
			print("EXception caught : " +str(ex))

obj=Detect_HSTS("http://192.168.250.1/dvwa")
obj.start()


