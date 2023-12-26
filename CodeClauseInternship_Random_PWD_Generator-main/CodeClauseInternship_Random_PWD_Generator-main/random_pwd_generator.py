#Random password generator using python

#import the necessary modules
import string
import random
length =int(input("Enter the length of password:"))

#define data
lower = string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

#combine the data
all=lower+upper+num+symbols

#use random
temp=random.sample(all,length)

#create the password
password="".join(temp)

#print the password
print("password is: "+password)