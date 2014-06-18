from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def dashboard(request):
	back = request.user.social_auth.get(provider="facebook")
	return render(request, 'dashboard.html', { 'uid': back.uid },
        content_type="text/html")