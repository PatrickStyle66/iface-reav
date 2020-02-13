import re
import pdb
import hashlib
onlyLetters = re.compile("^[a-zA-Z]*$")
onlyLettersAndWhitespace = re.compile("^[a-zA-Z ]*$")
lettersNumbersAndWhitespace = re.compile("^[\w ]*$")
passwordPattern = re.compile("^[\w\W]*$")
def isIn(dicto,key):
	try:
		dicto[key]
	except:
		return False
	return True
def checkMessage(message):
	fields = set(["sender","receiver","body"])
	message = set(message.keys())
	return message.issubset(fields)

def attempt(function,*args):
	if(not callable(function)):
		raise Exception("{} is not a callable object.".format(function))
	try:
		res = function(*args)
		return res
	except Exception as e:
		return e.args[0]

def reMatch(string,pattern):
	return re.search(pattern,string) is not None

def hashPass(password):
	password = str(password)
	if(reMatch(password,passwordPattern)):
		return hashlib.sha512(password.encode("utf-8")).hexdigest()
	else:
		raise Exception("Malformed Password")