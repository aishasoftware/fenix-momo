import os
import sys
import json
import time
import uuid
import collections
import multiprocessing,datetime
from  MOMO_TASK.config import globalParams
from MOMO_TASK.momoRequest import momoCollect,momoDisburse,momoTranStatus
from multiprocessing import Pool
from multiprocessing import Process
from time import sleep
import random
import threading

# this method add ref-id of momo transaction(collect/disburse) as soon as it is successfully created. 
# ref-id is added to the Queue so we can continuously query the status of transaction and update it in the db
def add_tasks(refId):
    globalParams.q.put(refId)
    # make run = True so a thread is created to process items in the Queue (to query transaction status and update it in db)
    globalParams.run = True
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Queue size after adding request : ')
    print(globalParams.q.qsize())

# this method gets ref-id of certain transaction exists in the Queue, send query request to momo api, and returns status of that transaction and update it in db   
def getTranStatus():
   print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ get transaction status for one of the transactions stored in the Queue ')
   # make run = False because thread already created to process Queue items and it will continue until the Queue is empty
   globalParams.run = False
   while (globalParams.q.empty() != True):
   # sleep for 5 seconds
    sleep(5)
    refId = globalParams.q.get()
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ current ref-id :  ')
    print(refId)
    from MOMO_TASK.models import MRequest
    request = MRequest.objects.get(rid=refId)
    tranStatus = momoTranStatus(refId,request.rtype)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ transactio status of current ref-id :  ')
    print(tranStatus)
    request.rstatus = tranStatus
    request.rcompletionTime = datetime.datetime.now()
    request.save()
   # make run = True so a thread is created to process items in the Queue (to query transaction status and update it in db) 
   globalParams.run = True
   return globalParams.q.qsize()
    
# this method prints size of Queue after thread is done
def printResult(result):
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Queue size after processing item request : ')
    print(globalParams.q.qsize())

# this method creates a thread to process Queue items (query transaction status in the background)
def run():
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Create new thread to query transaction status and updates db in parallel until Queue is empty ')
    statusThread = threading.Thread(target=getTranStatus, )
    statusThread.start()
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ start the Thread! ')
