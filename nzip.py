import zipfile,random,string,time
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
length = [1,2,3,4,5,6,7,8,9,10]
all = lower + upper + num + symbols
z=zipfile.ZipFile(input('Enter Zip path : '))
while True:
	lengh=random.choice(length)
	temp = random.sample(all,lengh)
	password = "".join(temp)
	print('Trying : ',password)
	try:
		z.extractall(pwd=password.encode())
		print('Password Found : '+password)
		break
	except:
		pass