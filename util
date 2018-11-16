from hashlib import sha256
from os.path import getsize
import getpass


def hachtext():
  plaintext = input("Texte a hacher : ")
  hashedText = sha256(plaintext.encode()).hexdigest()
  return hashedText

def getfilesize():
  filename = input("Nom du fichier : ")
  size = getsize(filename)
  return size

def takepassword():
  password = getpass.getpass('Password : ')
  return password
