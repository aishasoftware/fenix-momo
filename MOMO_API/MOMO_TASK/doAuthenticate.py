import http.client, urllib, base64, uuid,json
from MOMO_TASK.createapiuser import createUser 
from MOMO_TASK.createapikey import createKey 
from MOMO_TASK.base64Encoder import encode 
from MOMO_TASK.token import getToken 


# this method creates api user, api key , encodes them and uses them in authorization
def auth():
 user = createUser()
 if (user != 0):
  key = createKey(user)
  if(key != 0):
   encodeStr= f'{user}:{key}'
   result = encode(encodeStr)
   token = getToken(result)
   return token