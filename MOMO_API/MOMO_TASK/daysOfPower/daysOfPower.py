import collections, functools, operator , sys 
from collections import OrderedDict 

# this method returns total days of power, total paid rate and balancae transfered
# the idea is to divide the days into to periods
# first period:  is from the start of the first loan to the start of the last loan. during this period total rate keep increasing 
# until it reaches its maximum by the start of the last loan
# second period: is from the start of the last loan till the day when remaining balance does not cover total rate (k < total rate). during 
# this period total daily rate is constant because no new loans are added

def calculate(newRates,money):

 # expand days/rates input list, the new list is composed of pairs (key contains day/value contains total rate at that day)
 newRates = firstPeriod(newRates)
 sortedRate = sorted(newRates)
 finalRate = newRates[-1]
 (finDay,finRate) = finalRate

 totalRate = 0
 days = 0
 totalDays = 0
 
 # calculate total days and total rate from the start of first loan to start of last loan, this because rate gradually increase 
 # throughout this period
 
 for day,rate in newRates:
  if (money > totalRate):
   totalRate = totalRate + rate
   days = days + 1
 
 # calculate total days and total rate from the start of last loan to till the rates exceeds the paid amount, this because
 # rate in this period is fixed and equals to the sum of all rates of loans
 transfer = money - totalRate
 if (money > totalRate):
  newDays = transfer//finRate
  totalRate = totalRate + newDays * finRate
  totalDays = days + newDays

 transfer = money - totalRate
 
 print("^^^^^^^^^^^^^^^^^^^^^^^^ total rate : " )
 print(totalRate)
 print("^^^^^^^^^^^^^^^^^^^^^^^^ total days : ")
 print(totalDays)
 print("^^^^^^^^^^^^^^^^^^^^^^^^ transfered money : ")
 print(transfer)
 result = [totalDays,totalRate,transfer]
 return(result)

# this method takes days/rates list as input and converts it to another longer list that contains day/rate pairs for each day 
# in the first period (period from start of first loan to start of last loan). rate value in the new list represents total rate 
# of all loans started at/before that day

def firstPeriod(rates):

 # reduce input list to key/value pairs by summing values that have the same key. for example if multiple loans start at the same day
 # they will be reduced to one pair (key=day,value= sum of loans'rates)
 
 result = dict(functools.reduce(operator.add, 
          map(collections.Counter, rates))) 
          
 # sort dictionary keys asc
 sortedDays = sorted(list(result.keys()))
 
 totalRate = 0
 acumRate = 0
 firstPeriod = []
 start = 0
 
 # convert rate/day list by expanding it to list that contains total rate per each day from 
 # start of first loan to the start of final loan
 
 for day1 in range(len(sortedDays)):
  curRate = result.get(sortedDays[day1])
  totalRate = curRate + totalRate
  print(f'################## rate = {curRate} , total = {totalRate}')
  if(day1 < len(sortedDays)-1):
   period = sortedDays[day1+1] - sortedDays[day1]
  if(day1 == len(sortedDays)-1):
   period = 1
  for day2 in range(start , period + start):
   print(curRate)
   firstPeriod.append(tuple([day2+1,totalRate]))
  acumRate = totalRate
  start = start + period
 
  print(f'^^^^^^^^^^^^^^^^^^^^^^^^^^ total rate in the first period : {totalRate}')
  print(f'^^^^^^^^^^^^^^^^^^^^^^^^^^ daily rates during first period : {firstPeriod}')

 return firstPeriod
