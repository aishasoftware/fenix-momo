import http.client, urllib, base64, uuid,json,os,base64
from MOMO_TASK.config import globalParams

# this method gets token that will used for authorization in momo api transactions
def getToken(token):    

 sub_key = globalParams.sub_key 
 headers = {
     'Authorization': f'Basic {token}',
     'Content-Type': 'application/json',
     'Ocp-Apim-Subscription-Key': f'{sub_key}',
 }
 params = urllib.parse.urlencode({})
 try:
     conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
     conn.request("POST", "/collection/token/?%s" % params, "{body}", headers)
     response = conn.getresponse()
     data = response.read() 
     resp_dict = json.loads(data)
     token = resp_dict.get('access_token')
     if (response.status == 200):
      return token
     else:
      return 0
      
     conn.close()
 except Exception as e:
     print("[Errno {0}] {1}".format(e.errno, e.strerror))
