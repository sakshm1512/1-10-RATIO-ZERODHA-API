from api_helper import ShoonyaApiPy
import logging
import datetime
import pyotp
from collections import OrderedDict
import numpy as np
import conversion as conv

current_time = datetime.datetime.now()

try:
    #start of our program
    api = ShoonyaApiPy()

    #credentials
    user        = ''
    pwd         = ''
    vc          = ''
    app_key     = ''
    imei        = ''
    token       = ''

    api.login(userid=user, password=pwd, twoFA=pyotp.TOTP(token).now(), vendor_code=vc, api_secret=app_key, imei=imei)


    def buyMarket(name, quantity, lp):
        try:
            #types: MKT, LMT
            #Retention = IOC, DAY
            ret = api.place_order(buy_or_sell='B', product_type='M',
                                exchange='NFO', tradingsymbol=(name), 
                                quantity=quantity, discloseqty=0,price_type='LMT', price=lp, trigger_price=None,
                                retention='IOC', remarks=('my_sell_order_'))
            print(ret)
            ordno = ret['norenordno']
            orderHistory = api.single_order_history(ordno)
            status = orderHistory[0]['status']
            return [status, ordno]

    
        except Exception as e:
            print('Network error at shoonya', e)
            return 'rejected'
        
    def MKT_Exit(name, quantity, lp):
        try:
            #types: MKT, LMT
            #Retention = IOC, DAY
            ret = api.place_order(buy_or_sell='B', product_type='M',
                                exchange='NFO', tradingsymbol=(name), 
                                quantity=quantity, discloseqty=0,price_type='MKT', price=lp, trigger_price=None,
                                retention='IOC', remarks=('my_sell_order_'))
            print(ret)
            ordno = ret['norenordno']
            orderHistory = api.single_order_history(ordno)
            status = orderHistory[0]['status']
            return [status, ordno]

    
        except Exception as e:
            print('Network error at shoonya', e)
            return 'rejected'
        
    def buyMarket_LMT_DAY(name, quantity, lp):
        try:
            #types: MKT, LMT
            #Retention = IOC, DAY
            ret = api.place_order(buy_or_sell='B', product_type='M',
                                exchange='NFO', tradingsymbol=(name), 
                                quantity=quantity, discloseqty=0,price_type='LMT', price=lp, trigger_price=None,
                                retention='DAY', remarks=('my_sell_order_'))
            print(ret)
            ordno = ret['norenordno']
            orderHistory = api.single_order_history(ordno)
            status = orderHistory[0]['status']
            return [status, ordno]

    
        except Exception as e:
            print('Network error at shoonya', e)
            return 'rejected'


    def sellMarket(name, quantity, lp):
        try:
            # print('sell')
            ret = api.place_order(buy_or_sell='S', product_type='M',
                                exchange='NFO', tradingsymbol=(name), 
                                quantity=quantity, discloseqty=0,price_type='LMT', price=lp, trigger_price=None,
                                retention='IOC', remarks=('my_sell_order_'))
            print(ret)
            ordno = ret['norenordno']
            orderHistory = api.single_order_history(ordno)
            status = orderHistory[0]['status']
            print(status)
            return [status, ordno]
    
        except Exception as e:
            print('Network error at shoonya', e)
            return 'rejected'
        
    def check(ordno):
        try:
            orderHistory = api.single_order_history(ordno)
            status = orderHistory[0]['status']
            return status
        except Exception as e:
            print('Network error at shoonya', e)
            return 'failed'
            
    
    def cancel(ordno):
        try:
            ret = api.cancel_order(ordno)
            return ret

        except Exception as e:
            print('Failed cancel order: ', e)
            return 'Failed'

except Exception as e:
    print('Network error at shoonya', e)


        
