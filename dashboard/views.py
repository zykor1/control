from django.shortcuts import render

def dashboard(request):
	print "paso por aqui pero mando lo que quiero xD"
	return render(request, 'dashboard.html', {},
        content_type="text/html")