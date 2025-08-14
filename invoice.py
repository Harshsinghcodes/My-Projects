#Invoice Generator
import requests
import json
def invoice(amount, des):
    url = "https://api.oxapay.com/v1/payment/invoice"

    headers = {
  'merchant_api_key': 'ZIA9SS-SNHMHF-BFAEH7-INTZZR',
  'Content-Type': 'application/json'
}
    data = {
  "amount": amount,
  "currency": "USD",
  "lifetime": 30,
  "fee_paid_by_payer": 1,
  "under_paid_coverage": 2.5,
  "to_currency": "USDT",
  "auto_withdrawal": False,
  "mixed_payment": True,
  "callback_url": "https://example.com/callback",
  "return_url": "https://example.com/success",
  "email": "customer@oxapay.com",
  "order_id": "ORD-12345",
  "thanks_message": "Thanks message",
  "description": des,
  "sandbox": False
}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    result = response.json()
    return result

while True:
    print("***********************************")
    print("WELCOME TO PYTHON INVOICE GENERATOR")
    print("/SELECT ANY OPTION")
    print("1. Create invocie")
    print("2. QUIT PROGRAM")
    print("***********************************")
    choice = int(input("ENTER YOUR CHOICE (1/2)"))
    if choice == 1:
        amount = int(input("Enter the amount for invoice"))
        des = input("Enter Discription")
        value = invoice(amount, des)
        print(value)
    elif choice == 2:
        print("Bye Have a Good Day!!!")
        break
    else:
        print("Enter Valid Option")



