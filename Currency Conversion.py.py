import tkinter as tk
from tkinter import messagebox
import requests

def convert_currency():
    from_curr = from_entry.get().upper()
    to_curr = to_entry.get().upper()
    try:
        amount = float(amount_entry.get())
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    url = f"https://api.apilayer.com/currency_data/convert?\n"
    "from={from_curr}&to={to_curr}&amount={amount}"
    

    payload = {}
    headers= {
     "apikey": "RSjfKlfWhSKeMY5PapeuOj6MyxsD9a0b"
    }
    response = requests.get(url,headers=headers)
    data = response.json()

    if response.status_code == 200 and "result" in data:
        result = data["result"]
        result_lable.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")
    else:
        messagebox.showerror("Error", "Conversion failed. Check currency codes.")

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x250")

tk.Label(root, text="From Currency (e.g. USD):").pack()
from_entry = tk.Entry(root)
from_entry.pack()

tk.Label(root, text="To Currency (e.g. EGP):").pack()
to_entry = tk.Entry(root)
to_entry.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

result_lable=tk.Label(root,font=("Arial", 12))
result_lable=tk.Label(root)
result_lable.pack()

root.mainloop()