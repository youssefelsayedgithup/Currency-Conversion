import requests

# ✅ أدخل مفتاح API الصحيح هنا
API_KEY = "RSjfKlfWhSKeMY5PapeuOj6MyxsD9a0b"

# 📥 مدخلات المستخدم
from_currency = input("Enter base currency (e.g. USD): ").upper()
to_currency = input("Enter target currency (e.g. EGP): ").upper()

while True:
    try:
        amount = float(input("Enter amount to convert: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# ✅ URL الصحيح بصيغة f-string"
url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={from_currency}&amount={amount}"


headers = {
    "apikey": "RSjfKlfWhSKeMY5PapeuOj6MyxsD9a0b"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"❌ Error: Status Code {response.status_code}")
    print("Details:", response.text)
    quit()

data = response.json()
if data.get("success"):
    result = data.get("result")
    print(f"\n✅ {amount} {from_currency} = {result:.2f} {to_currency}")
else:
    print("⚠️ Conversion failed. Details:", data.get("error", {}))
