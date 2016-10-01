import json, requests #importing json and requests in order to be able to post
from datetime import datetime, timedelta #importing datetime and timedelta for the dating game

# Step 1:
# This step is for registration. This honestly took me some time and research. I'd never worked with http requests
# before so it was definitely a learning experience. All it really took though was a simple look at Python
# documentation for requests so I guess I learned that I need to read and not always jump right into code

#payload is a dictionary that will take in token (the token given to me) and github (my url)
payload = {'token': 'ac25950ad7723a4b14665c609804ef76', 'github': 'https://github.com/ldavis38/code2040'} 
r = requests.post('http://challenge.code2040.org/api/register', params = payload) #this will post the payload dict to the api registration endpoint 

token = 'ac25950ad7723a4b14665c609804ef76' #just decided to actually assign token to my token so that I would not have to continuously hard code it

# Step 2:
# This was the reverse a string question. This was not too difficult. At first I was going to use a while or for loop
# but then I discovered Python's slice feature and decided to go for the shorter and more simple route. I already
# knew slice existed but I'd forgotten about it (its been a minute since I've used Python, my current CS courses
# use c++) 
rdict = {'token' : token} # this is a dictionary with just one key, token (the r is for reverse)
string = requests.post('http://challenge.code2040.org/api/reverse', rdict) # this is the string that the api gives 
newstring = string.text[::-1] # reversing the string and assigning it to newstring
reversedict = {'token': token, 'string': newstring} # dictionary with token and string needed to post    
r = requests.post('http://challenge.code2040.org/api/reverse/validate', reversedict) # posting the dictionary

ndict = {'token': token}
nih = requests.post('http://challenge.code2040.org/api/haystack', ndict)
nih = nih.json()
needle = nih['needle']
haystack = nih['haystack']
i = 0
index = 0;
notfound = True
while notfound:
     if needle == haystack[i]:
         index = i
         notfound = False
     else:
        i = i + 1
needledict = {'token': token, 'needle': index}
r = requests.post('http://challenge.code2040.org/api/haystack/validate', needledict)


pdict = {'token': token}
pfx = requests.post('http://challenge.code2040.org/api/prefix', pdict)
pfx = pfx.json()
prefix = pfx['prefix']
array = pfx['array']
newArray = []
for i in array:
    if not i.startswith(prefix):
        newArray.append(i)
prefixdict = {'token': token, 'array': newArray}
r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = prefixdict)


dgdict = {'token': token}
tdg = requests.post('http://challenge.code2040.org/api/dating', dgdict)
tdg = tdg.json()
datestamp = tdg['datestamp']
interval = tdg['interval']
firstdatestamp = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
newdatestamp = firstdatestamp + timedelta(seconds=int(interval))
newdatestamp = newdatestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
datedict = {'token': token, 'datestamp': newdatestamp}
r = requests.post('http://challenge.code2040.org/api/dating/validate', datedict)

