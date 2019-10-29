import http.client, urllib, base64, uuid,json
from MOMO_TASK.config import globalParams

def createKey(refId):
 sub_key = globalParams.sub_key
 headers = {
     # Request headers
     'Content-Type': 'application/json',
     'Ocp-Apim-Subscription-Key': f'{sub_key}',
 }
 params = urllib.parse.urlencode({})
 body = json.dumps({"providerCallbackHost": "momotask"})
 
 try:
     conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')# use config file
     conn.request("POST", f'/v1_0/apiuser/{refId}/apikey?{params}', body, headers)# use config file
     response = conn.getresponse()
     data = response.read()
     resp_dict = json.loads(data)
     apiKey = resp_dict.get('apiKey')
     conn.close()
     if (response.status == 201):
      return resp_dict.get('apiKey')
     else:
      return 0
 except Exception as e:
     print(e)
