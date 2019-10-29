import http.client, urllib, base64, uuid,json
from MOMO_TASK.config import globalParams

def createUser():
 print('############################### globalParams.sub_key')
 print(globalParams.sub_key)

 refId = uuid.uuid4()
 sub_key = globalParams.sub_key
 headers = {
     # Request headers
     'X-Reference-Id': f'{refId}',
     'Content-Type': 'application/json',
     'Ocp-Apim-Subscription-Key': f'{sub_key}',
 }
 params = urllib.parse.urlencode({})
 
 body = json.dumps({"providerCallbackHost": "momotask"})
 try:
     conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com') # use config file
     conn.request("POST", "/v1_0/apiuser?%s" % params, body, headers) # use config file
     response = conn.getresponse()
     data = response.read()
     conn.close()
     if(response.status == 201):
      return refId
     else:
      0
     
 except Exception as e:
     print(e)
 