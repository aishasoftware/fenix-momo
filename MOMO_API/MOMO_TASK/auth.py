import http.client, urllib, base64, uuid,json
from createapiuser import createUser 
from createapikey import createKey 
from base64Encoder import encode 
from token import getToken 
#sent succ and received created response 201
def auth():#createKey(refId):
 user = createUser()
 if (user != 0):
  key = createKey(user)
  if(key != 0):
   encodeStr= f'{user}:{key}'
   result = encode(encodeStr)
   token = getToken(result)
   print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ access token :')
   print(token)
   return token
