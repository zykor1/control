#from django.shortcuts import render
import paypalrestsdk


paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AQehDxB1uiarwzJmeY0YUQEO19COadP-_B8DHKhgDzuBIVaaaHPdJtLft-fF",
  "client_secret": "EB6czRC4FupnnNNkMZIN1AnQj3qxKL3wf3ZAw1SeiBdYUHtZUjidCGfgACT2" })


payment = paypalrestsdk.Payment({
  "intent": "sale",
  "redirect_urls": {
	"return_url":"http://localhost/",
    "cancel_url":"http://localhost/"
  },
  "payer": {
    "payment_method": "paypal"},
  "transactions": [{
    "item_list": {
      "items": [{
        "name": "Chips a la diabla",
        "sku": "001",
        "price": "10.00",
        "currency": "MXN",
        "quantity": 1 }]},
    "amount": {
      "total": "10.00",
      "currency": "MXN" },
    "description": "Realizando pruebas con la api de paypal para python xD." }]})


if payment.create():
  print payment
  print("Payment created successfully")
else:
  print(payment.error)