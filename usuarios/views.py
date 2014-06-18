from django.shortcuts import render

def  login(request):
	return render(request, 'login.html', {},
        content_type="text/html")