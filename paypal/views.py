from django.shortcuts import render
import paypalrestsdk
from paypal.models import Usuario_donacion
from paypal.forms import DonacionForm


def realizar_donacion(request):
	if request.method ==  'POST':
		form = DonacionForm(request.POST)
		if form.is_valid():
			paypalrestsdk.configure({
				"mode": "sandbox", # sandbox or live
				"client_id": "AQehDxB1uiarwzJmeY0YUQEO19COadP-_B8DHKhgDzuBIVaaaHPdJtLft-fF",
				"client_secret": "EB6czRC4FupnnNNkMZIN1AnQj3qxKL3wf3ZAw1SeiBdYUHtZUjidCGfgACT2"
			})
			estado_donacion = dona_y_guarda(paypalrestsdk, form, request.user)
			if estado_donacion == 1:
				return render(request, 'donaciones.html', {"donaciones": donaciones, "success": 1  }, content_type="text/html")
			else:
				return render(request, 'donaciones.html', {"donaciones": donaciones, "error": estado_donacion  }, content_type="text/html")
	else:
		donaciones = Usuario_donacion.objects.filter(user=request.user)
		form = DonacionForm()
		return render(request, 'donaciones.html', {"donaciones": donaciones, "form" : form  }, content_type="text/html")






def dona_y_guarda(paypalrestsdk, form, user):
	metodo = form.cleaned_data['metodo']
	cantidad = form.cleaned_data['cantidad']
	comentario = form.cleaned_data['comentario']
	payment = paypalrestsdk.Payment({
	  "intent": "sale",
	  "redirect_urls": {
		"return_url":"http://localhost:8000/",
	    "cancel_url":"http://localhost:8000/"
	  },
	  "payer": {
	    "payment_method": metodo},
	  "transactions": [{
	    "item_list": {
	      "items": [{
	        "name": "Donacion",
	        "sku": "1",
	        "price": str(cantidad),
	        "currency": "USD",
	        "quantity": 1 }]},
	    "amount": {
	      "total": str(cantidad),
	      "currency": "USD" },
	    "description": "Realizando pruebas con la api de paypal para python xD."
	}]})
	if payment.create():
		paypal_id = payment.id
		try:
			donacion = Usuario_donacion.objects.create(metodo=metodo, cantidad=cantidad, paypalid=paypal_id, user=user, comentario=comentario)
			return 1
		except Exception, e:
			print e
			pass
	else:
		return payment.error