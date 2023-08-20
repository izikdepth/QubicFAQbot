import requests
import json

def get_price(request):
    url = "https://api.livecoinwatch.com/coins/single"
    payload = json.dumps({
      "currency": "USD",
      "code": "QUBIC",
      "meta": True
    })
    
    """"
    currently using livecoin's free api which is 10,000 free calls daily.  get it on
    https://www.livecoinwatch.com/tools/api 
    """
    headers = {
      'content-type': 'application/json',
      'x-api-key': '0d010030-4ec2-4f04-a971-99667a3422b7'
    }
    
    
    
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        price = data['rate']
        return price
    except KeyError:
        return None
