import json, requests #importing json and requests in order to be able to post
from datetime import datetime, timedelta #importing datetime and timedelta for the dating game
# Step 3:
# This was the prefix question. I had to find all the strings in an array that did not start with a certain prefix
# and make a new array with just those. I had to research for this one too and I found startswith which helped 

token = 'ac25950ad7723a4b14665c609804ef76' #just decided to actually assign token to my token so that I would not have to continuously hard code it
pdict = {'token': token} # p dictionary with my token
pfx = requests.post('http://challenge.code2040.org/api/prefix', pdict) # assigning the dictionary from the api to pfx (prefix) 
pfx = pfx.json() 
prefix = pfx['prefix'] # assigning the value of 'prefix' to prefix
array = pfx['array'] # assigning the value of 'array' to array
newArray = [] # newArray declaration
for i in array: # for loop that searches an array 
    if not i.startswith(prefix): # startswith can find any string that starts with whatever string you ask it to
        newArray.append(i) # appending all the strings that don't start with the prefix to a new array 
prefixdict = {'token': token, 'array': newArray} # dictionary with results 
r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = prefixdict) # posting the results 
