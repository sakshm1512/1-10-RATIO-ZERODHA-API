import os
import sys
import json
import datetime
from kiteconnect import KiteConnect 

try:
    with open(f"Login Credentials.json" , "r") as f:
        login_credential = json.load(f)
except:
    print("---- Enter Your Login Credentials ----")
    login_credential = {"api_key": str(input("Enter API Key :")),
                         "api_secret": str(input("Enter API Secret :"))}
    if input("Press Y to save Login Credentials or any key to bypass : ").upper() == "Y":
        with open(f"Login Credentials.json" , "w") as f:
            json.dump(login_credential, f)
        print("Data Saved...")
    else:
        print("Data Save Cancelled!!!!")
        sys.exit()
print("----Getting Access Token----")
if os.path.exists(f"AccessToken/{datetime.datetime.now().date()}.json"):
    with open(f"AccessToken/{datetime.datetime.now().date()}.json" , "r") as f:
        access_token = json.load(f)
else:
    print("Try to Login...")
    kite = KiteConnect(api_key=login_credential["api_key"])
    print("Login URL : " ,  kite.login_url())
    request_tkn = input("Login and enter your request token here : ")
    try:
        access_token = kite.generate_session(request_token=request_tkn, api_secret=login_credential["api_secret"])['access_token']
        os.makedirs(f"AccessToken", exist_ok=True)
        with open(f"AccessToken/{datetime.datetime.now().date()}.json", "w") as f:
            json.dump(access_token, f)
        print("Login Successful...")
    except Exception as e:
        print(f"Login Failed{{{e}}}")
        sys.exit()
print(f"API Key : {login_credential['api_key']}")
print(f"Access Token : {access_token}")
