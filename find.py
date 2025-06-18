import datetime
import os
import json
import time
import pandas as pd
from kiteconnect import KiteConnect
import operator
from datetime import date
from dateutil.relativedelta import relativedelta, TH

# # Setting Login Credentials from Files in ARB Bot Folder
# with open('Login Credentials.json' , 'r') as json_file:
#     data = json.load(json_file)
#     api_key = data["api_key"]
# if os.path.exists(f"AccessToken/{datetime.datetime.now().date()}.json"):
#     with open(f"AccessToken/{datetime.datetime.now().date()}.json" , "r") as f:
#         access_token = json.load(f)
 
# kite = KiteConnect(api_key=api_key)
# kite.set_access_token(access_token)

# print(kite.quote('NFO:BANKNIFTY2390647900CE'))

# def LotSize(input_str):
#     if input_str[4] == 'N':
#         return 50
#     elif input_str[4] == 'B':
#         return 15
    
# print(LotSize('NFO:NIFTY2390647900CE'))

# def buy_price_calc(input_value, reduction_percent):
#     isinstance(input_value, (int, float)) and isinstance(reduction_percent, (int, float))
#     reduction_percent >= 0 and reduction_percent <= 100
#     reduction_factor = reduction_percent / 100
#     result = input_value - (reduction_factor * input_value)
#     return round(round(result / 0.05) * 0.05 , 2)

# print(buy_price_calc(1.06 , 40))

def strike_finder(input_string):

    input_string = input_string[:-2]
    strike = input_string[-5:]
    return strike

print(strike_finder('NFO:BANKNIFTY2391345200CE'))

