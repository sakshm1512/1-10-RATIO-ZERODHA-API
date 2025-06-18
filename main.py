import datetime
import os
import json
import time
import pandas as pd
from kiteconnect import KiteConnect
import operator
from datetime import date
from dateutil.relativedelta import relativedelta, TH
import instruments as ins
import conversion as conv
import Shoonya as shoon

# Setting Login Credentials from Files in ARB Bot Folder
with open('Login Credentials.json' , 'r') as json_file:
    data = json.load(json_file)
    api_key = data["api_key"]
if os.path.exists(f"AccessToken/{datetime.datetime.now().date()}.json"):
    with open(f"AccessToken/{datetime.datetime.now().date()}.json" , "r") as f:
        access_token = json.load(f)
 
kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

#initialising time
current_time = datetime.datetime.now()
target_time = datetime.datetime(
    year=current_time.year, month=current_time.month, day=current_time.day, hour=23, minute=59, second=00)
start_time = datetime.datetime(
    year=current_time.year, month=current_time.month, day=current_time.day, hour=3, minute=15, second=00)
time_buy = datetime.datetime(
    year=current_time.year, month=current_time.month, day=current_time.day, hour=9, minute=25, second=00)

def round_to_nearest_hundred(price):
    return round(price / 100.0) * 100

def round_to_nearest_fifty(price):
    return round(price / 50.0) * 50

def strike_finder(input_string):
    input_string = input_string[:-2]
    strike = input_string[-5:]
    strike = int(strike) + 700
    return strike

max_retries = 10
retry_delay = .5
count = 1
ins_list = ins.findtoken(["BANKNIFTY"])

while current_time>start_time and current_time<target_time:
    time.sleep(.1)
    print(count)
    count = count+1

    try:
        data =  kite.quote(ins_list)
        exception = False
    except Exception as e:  
        print("connection error:" , e)
        exception = True
        time.sleep(retry_delay)
    if exception == False:
        
        prev_close_bn = data[ins_list[0]]['ohlc']['close']
        lp_bn = data[ins_list[0]]['last_price']
        entry_bn = abs(prev_close_bn-lp_bn)
        # print(entry_bn)
        
        price = data[ins_list[0]]['last_price']
        rounded_price = round_to_nearest_hundred(price)
        prices_below = [rounded_price - i*100 for i in range(1, 6)]
        prices_above = [rounded_price + i*100 for i in range(1, 6)]
        all_prices = prices_below[::-1] + [rounded_price] + prices_above

        tsym = ins.tsym_all(1, all_prices)

        try:
            data =  kite.quote(tsym)
            exception = False
        except Exception as e:  
            print("connection error:" , e)
            exception = True
            time.sleep(retry_delay)
        if exception == False:

            diff_dict = {}
            for x in range (len(all_prices)):
                lp1 = data[tsym[x*2]]['last_price']
                lp2 = data[tsym[(x*2)+1]]['last_price']
                diff = lp1-lp2
                diff_dict[all_prices[x]] = abs(diff)
            atm = min(diff_dict, key=lambda x: diff_dict[x])
            # print(atm)


            strikes = []
            for i in range(25):
                strikes.append(atm + (i * 100))
            
            tsym = ins.tsym_BN_CE(strikes)
            # print(tsym)

            try:
                data =  kite.quote(tsym)
                exception = False
            except Exception as e:  
                print("connection error:" , e)
                exception = True
                time.sleep(retry_delay)
            if exception == False:
                
                lp_strikes = {}
                for x in tsym:
                    if x not in data:
                        lp_strikes[x] = 0
                    else:
                        lp_strikes[x] = data[x]['last_price']

                tradelist = {}
                for key, value in lp_strikes.items():
                    if value >= 70 and value <= 110:
                        strike_10 = strike_finder(key)
                        strike_10 = ins.tsym_BN_CE([strike_10])
                        value2 = lp_strikes[strike_10[0]]
                        if int(value2)*10 - int(value) > 35:
                            tradelist[key] = strike_10[0]
                print(tradelist)

                
                        
                        


                

    current_time = datetime.datetime.now()

            


        