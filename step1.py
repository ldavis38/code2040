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
