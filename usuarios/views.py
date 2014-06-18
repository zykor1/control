from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def  login(request):
	return render(request, 'login.html', {},
        content_type="text/html")

def logout(request):
	auth_logout(request)
	return redirect('/')