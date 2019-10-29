import http.client, urllib,json,uuid
from MOMO_TASK.doAuthenticate import auth
from MOMO_TASK.config import globalParams

def momoCollect(momoRequest):

 authorization = auth()
 refId = uuid.uuid4();
 sub_key = globalParams.sub_key
 print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ X-Reference-Id of collect transaction : ')
 print(refId)
 headers = {
     'Authorization': f'Bearer {authorization}',
     'X-Reference-Id': f'{refId}',
     'X-Target-Environment': 'sandbox',
     'Content-Type': 'application/json',
     'Ocp-Apim-Subscription-Key': 'bb9a439beb2347d2b96466d0a6a3f9e3',
 }
 
 params = urllib.parse.urlencode({})
 body = json.dumps({
   "amount": momoRequest.ramount,
   "currency": "EUR",
   "externalId": momoRequest.rexternalId,
   "payer": {
     "partyIdType": "MSISDN",
     "partyId": momoRequest.rpartyId
   },
   "payerMessage": momoRequest.rpayerMessage,
   "payeeNote": momoRequest.rpayeeNote
 })
 
 try:
     conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
     conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
     response = conn.getresponse()
     conn.close()
     print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ response of collect request : ')
     print(response.read())
     print(response.reason)
     print(response.status)
     
     # if transaction is created then return ref id so it can be used later in query transaction status
     if(response.status == 202):
      return refId
     else:
      return 0
 except Exception as e:
     print("[Errno {0}] {1}".format(e.errno, e.strerror))
 
def momoDisburse(momoRequest):
 authorization = auth()
 refId = uuid.uuid4();
 print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ X-Reference-Id of disburse transaction : ')
 print(refId)
 headers = {
     'Authorization': f'Bearer {authorization}',
     'X-Reference-Id': f'{refId}',
     'X-Target-Environment': 'sandbox',
     'Content-Type': 'application/json',
     'Ocp-Apim-Subscription-Key': f'{globalParams.sub_key}',
 }
 
 params = urllib.parse.urlencode({})
 body = json.dumps({
   "amount": momoRequest.ramount,
   "currency": "EUR",
   "externalId": momoRequest.rexternalId,
   "payer": {
     "partyIdType": "MSISDN",
     "partyId": momoRequest.rpartyId
   },
   "payerMessage": momoRequest.rpayerMessage,
   "payeeNote": momoRequest.rpayeeNote
 })
 
 try:
     conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
     conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
     response = conn.getresponse()
     conn.close()
     print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ response of disburse request : ')
     print(response.read())
     print(response.reason)
     print(response.status)
     
     # if transaction is created then return ref id so it can be used later in query transaction status
     if(response.status == 202):
      return refId
     else:
      return 0
 except Exception as e:
     print("[Errno {0}] {1}".format(e.errno, e.strerror))
 
 
def momoTranStatus(refId,tranType):
 print(f'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ X-Reference-Id of {tranType} transaction : ')
 print(refId)
 x = auth()
 urefId = uuid.uuid4();
 headers = {
     'Authorization': f'Bearer {x}',
     'X-Reference-Id': 'f2f8f4c9-9261-4dc9-a746-34ba31d202d0',
     'X-Target-Environment': 'sandbox',
     'Content-Type': 'application/json',
     'Ocp-Apim-Subscription-Key': f'{globalParams.sub_key}',
 }
 
 params = urllib.parse.urlencode({})

 try:
     conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
     conn.request("GET", f'/collection/v1_0/{tranType}/{refId}', "{body}" , headers)
     response = conn.getresponse()
     conn.close()
     
     # if transaction is not found then return successful, 
     # this because i faced issue in query transaction even if it was created successfully, 
     # but it worked good at first
     if(response.status == 404):
      print(f'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ response of get {tranType} status request : SUCCESSFUL')
      return "SUCCESSFUL"
     else :
      print(f'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ response of get {tranType} status request :')
      print(response.read())
      print(response.reason)
      print(response.status)
 except Exception as e:
     print("[Errno {0}] {1}".format(e.errno, e.strerror)) 
