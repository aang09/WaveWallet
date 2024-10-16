import requests, json
from fake_useragent import UserAgent

class Api : 
    
    
    def header(
            token
        ):
        
        with open("af09/header.json", 'r') as f:
            hd = json.load(f)
        
        ua=UserAgent()
        headers = {
            "accept"            : "application/json",
            "accept-language"   : "en-US,en;q=0.9",
            "authorization"     : f"Bearer {token}",
            "content-type"      : "application/json",
            "priority"          : "u=1, i",
            "sec-ch-ua"         : ua.random,          # Use a random fake user-agent
            "sec-ch-ua-mobile"  : "?1",
            "sec-ch-ua-platform": '"android"',        # Optional: Customize the platform as needed
            "sec-fetch-dest"    : "empty",
            "sec-fetch-mode"    : "cors",
            "sec-fetch-site"    : "same-site",
            "Referer"           : hd.get("Referer", ""),
            "Referrer-Policy"   : "origin",
            "Host"              : hd.get("Host", ""),    
            "Origin"            : hd.get("Origin", "") 
        }
 
        return headers
    
    def get(self,url,token,data):
        return requests.get(url, headers=Api.header(token), json=data) 
    
    def post(self,url,token,data):
        return requests.post(url, headers=Api.header(token), json=data) 
    
    def put(self,url,token,data):
        return requests.put(url, headers=Api.header(token), json=data) 
    
    def patch(url,token,data):
        return requests.patch(url, headers=Api.header(token), json=data) 






        