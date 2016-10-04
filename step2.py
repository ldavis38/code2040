import json, requests #importing json and requests in order to be able to post
from datetime import datetime, timedelta #importing datetime and timedelta for the dating game

# Step 2:
# This was the reverse a string question. This was not too difficult. At first I was going to use a while or for loop
# but then I discovered Python's slice feature and decided to go for the shorter and more simple route. I already
# knew slice existed but I'd forgotten about it (its been a minute since I've used Python, my current CS courses
# use c++) 
token = 'ac25950ad7723a4b14665c609804ef76' #just decided to actually assign token to my token so that I would not have to continuously hard code it
rdict = {'token' : token} # this is a dictionary with just one key, token (the r is for reverse)
string = requests.post('http://challenge.code2040.org/api/reverse', rdict) # this is the string that the api gives 
newstring = string.text[::-1] # reversing the string and assigning it to newstring
reversedict = {'token': token, 'string': newstring} # dictionary with token and string needed to post    
r = requests.post('http://challenge.code2040.org/api/reverse/validate', data = reversedict) # posting the dictionary
