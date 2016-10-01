import json, requests #importing json and requests in order to be able to post
from datetime import datetime, timedelta #importing datetime and timedelta for the dating game

# Step 1:
# This step is for registration. This honestly took me some time and research.  I had to really think about what the prompt
# was asking me to do because while it wasn't extremely difficult or impossible, it wasn't easy or completely handed to
# me either. I'd never worked with http requests before so it was definitely a learning experience.
# What really ended up helping was the Python documentation for requests so I guess I learned that I need to 
# read and not always jump right into code especially for tasks I'm not familiar with

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

# Step 3:
# This was the needle in a haystack question. I had to find the index or position of the 'needle' in the 'haystack' array
# (sidenote: I like the idea of finding something in an array being a needle in a haystack. pretty clever) This was not very
# difficult either. For me, it was just a matter of using Python vs C++. I kept wanting to add semicolons, parentheses, and
# brackets haha.
ndict = {'token': token} # dictionary with token
nih = requests.post('http://challenge.code2040.org/api/haystack', ndict) # getting the dictionary, nih (needleinhaystack)
nih = nih.json() # kept getting error when I would try to use nih in the next lines so I looked up solutions and this one 
# worked. It should convert the json dictionary so that python can access its data
needle = nih['needle'] # assigning the value of the needle key to needle
haystack = nih['haystack'] # assigning the value of the haystack key (an array) to haystack
i = 0 # setting i to 0, this will be our index through the loop below
index = 0; # this index will be the one used once the needle is found 
notfound = True # notfound is true and will be made false once the needle is found
while notfound: # while notfound is true
     if needle == haystack[i]: # if needle is the same as the current element in the haystack array, then it is the needle
         index = i # assign the current index to 'index'
         notfound = False # setting notfound to false because it has been found and we can now exit the while loop
     else: # otherwise (needle is not the same as the current element)
        i = i + 1 # then i = i + 1 so that we can move on to the next index 
needledict = {'token': token, 'needle': index} # needle dictionary that will be used to post 
r = requests.post('http://challenge.code2040.org/api/haystack/validate', needledict) # posting the results

# Step 4:
# This was the prefix question. I had to find all the strings in an array that did not start with a certain prefix
# and make a new array with just those. I had to research for this one too and I found startswith which helped 
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

# Step 5:
# The Dating Game
# This took me the longest and was the most difficult. It was like nothing I had ever done before, ever.
# I had to use the datetime library which I've never even heard of let alone used and it took me a while
# to really even understand what was going on. I finally figured out the right methods to use but it 
# took me some time, focus, and alot of debugging. Honestly, it was kind of frustrating but I personally
# think that sometimes it takes being uncomfortable to be able to learn and grow. Sometimes you have to be 
# clueless to learn something new, right? 
dgdict = {'token': token}
tdg = requests.post('http://challenge.code2040.org/api/dating', dgdict)
tdg = tdg.json()
datestamp = tdg['datestamp']
interval = tdg['interval']
firstdatestamp = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ") # this is converting the datestamp from a string to a datetime object in the ISO 8061 format
newdatestamp = firstdatestamp + timedelta(seconds=interval) # this is adding the interval (an int which holds seconds) to the ISO formatted datestamp. This is done with timedelta. 
# You can't add two datetime objects (learned that the hard way haha) so you have to use timedelta instead
newdatestamp = newdatestamp.strftime("%Y-%m-%dT%H:%M:%SZ") # this is the new date stamp, the sum, being converted back to iso form
datedict = {'token': token, 'datestamp': newdatestamp} # dictionary with results
r = requests.post('http://challenge.code2040.org/api/dating/validate', datedict) # posting the results

