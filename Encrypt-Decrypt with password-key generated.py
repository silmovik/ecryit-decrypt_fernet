print("""
          _           _   _   _          _                _    
         | |         | | | | | |        | |              | |   
__      _| |__   __ _| |_| |_| |__   ___| |__   __ _  ___| | __
\ \ /\ / / '_ \ / _` | __| __| '_ \ / _ \ '_ \ / _` |/ __| |/ /
 \ V  V /| | | | (_| | |_| |_| | | |  __/ | | | (_| | (__|   < 
  \_/\_/ |_| |_|\__,_|\__|\__|_| |_|\___|_| |_|\__,_|\___|_|\_\\\n
=================Encrypt-Decrypt Your Password====================
""")
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
option1=int(input("1. Encrypt\n2. Decrypt\nChoose Option: "))
if option1==1:
	option2=int(input("1. Generate key\n2. Insert key\nChoose Option: "))
	if option2==2:
		key = input("Insert your key: ").encode()
		f = Fernet(key)
		message=input("Input your message: ").encode()
		encrypted = f.encrypt(message)
		print("Your encrypted message is:\n",encrypted.decode())
	elif option2==1:
		password = input("Input your password: ").encode()	
		salt = os.urandom(16)
	
		kdf = PBKDF2HMAC(
	     	algorithm=hashes.SHA256(),
	     	length=32,
	     	salt=salt,
	     	iterations=100000,
	     	backend=default_backend()
		)
		key = base64.urlsafe_b64encode(kdf.derive(password))
		print("Your key is: ",key.decode())
		message=input("Input your message: ").encode()
		f = Fernet(key)
		encrypted = f.encrypt(message)
		print("Your encrypted message is:\n",encrypted.decode())

elif option1==2:
	key = input("Input your key: ")
	f = Fernet(key)
	encrypted = input("input encrpyted: ").encode()
	print(f.decrypt(encrypted))

else:
	print("Wrong Option, Try Again", end="")
