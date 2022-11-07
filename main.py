import requests
from twilio.rest import Client
Weather_Endpoint= "https://api.openweathermap.org/data/2.5/forecast"
api_key = "2c169d9a9abee9bbf458aacceac04629"
account_sid = "ACa20a3820567be93d8a8ff2f7f2e1af82"
auth_token = "224fc177e42f972a9129e2a2274d69c3"
# +15618236113
parameters={
    "lat": 23.831457,
    "lon": 91.286781,
    "appid": api_key,
}
respons = requests.get(Weather_Endpoint, params=parameters)
respons.raise_for_status()
data = respons.json()
is_rain=False
weather_data=data["list"][:6]
for hour_data in weather_data:
    condition_code=hour_data["weather"][0]["id"]
    if condition_code < 700:
        is_rain=True

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="it going to rain today",
        from_='+15618236113',
        to='+917085542194'
    )
    print(message.status)

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

n='d'
print(type(5/2))
print(type(5//2))
def gcd(x,y):
    while y:
        x,y=y,x%y

    return x


print(gcd(9,3))

p=("hiiii")
print(type(p))
d={"a":1}
print((d))
try:
    print("code start here")
    p=10/0
except:
    print("error")
finally:
    print("code is end")