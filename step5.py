import json, requests #importing json and requests in order to be able to post
from datetime import datetime, timedelta #importing datetime and timedelta for the dating game

# Step 5:
# The Dating Game
# This took me the longest and was the most difficult. It was like nothing I had ever done before, ever.
# I had to use the datetime library which I've never even heard of let alone used and it took me a while
# to really even understand what was going on. I finally figured out the right methods to use but it 
# took me some time, focus, and alot of debugging. Honestly, it was kind of frustrating but I personally
# think that sometimes it takes being uncomfortable to be able to learn and grow. Sometimes you have to be 
# clueless to learn something new, right? 

token = 'ac25950ad7723a4b14665c609804ef76' #just decided to actually assign token to my token so that I would not have to continuously hard code it
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
