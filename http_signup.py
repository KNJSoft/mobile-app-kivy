import json
import asyncio
import httpx
from kivy.network.urlrequest import UrlRequest
import requests

def signup_post():
    mail="knjprod@gmai1l.com"
    mdp="hhhh"
    dict={
        'email':mail,
        'password':mdp
    }
    result=json.dumps(dict)
    print(result)
    url = "http://127.0.0.1:8000/sign_up/"

    r=requests.post(url,data=result)


signup_post()