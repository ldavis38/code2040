import json, requests #importing json and requests in order to be able to post
from datetime import datetime, timedelta #importing datetime and timedelta for the dating game
# Step 2:
# This was the needle in a haystack question. I had to find the index or position of the 'needle' in the 'haystack' array
# (sidenote: I like the idea of finding something in an array being a needle in a haystack. pretty clever) This was not very
# difficult either. For me, it was just a matter of using Python vs C++. I kept wanting to add semicolons, parentheses, and
# brackets haha.

token = 'ac25950ad7723a4b14665c609804ef76' #just decided to actually assign token to my token so that I would not have to continuously hard code it
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
r = requests.post('http://challenge.code2040.org/api/haystack/validate', json = needledict) # posting the results

