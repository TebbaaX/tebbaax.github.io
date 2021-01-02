#GReconLists
#Coded by Adnane X Tebbaa
#Github : https://www.github.com/adnane-x-tebbaa/Grecon 
#Twitter : @TebbaaX 
#http://TebbaaX.xyz 

import os 
import sys
import time
import requests 
import random 
from googlesearch import search
from termcolor import colored, cprint
from http import cookiejar 
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('--query', required=True)
args = parser.parse_args()

TLD = ["com","ru","com.hk"]
beta  = random.choice(TLD)
s = requests.Session() 
A = '''
GreconV - Create Wordlists 
coded by @TebbaaX 
'''
print(A) 
print("") 
key  =  args.query
print(colored ('[>] Running...' ,'green')) 
query = key                           
for gamma in search(query, tld=beta, num=30 , stop=90 , pause=2): 
    print("" + gamma)   


