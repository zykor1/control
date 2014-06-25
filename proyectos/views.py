from django.shortcuts import render
from proyectos.models import ParticipanteProyecto
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
import json


# Create your views here.
@login_required(login_url='/login')
def obtener_proyectos(request):
	proyectos = serializers.serialize("json", ParticipanteProyecto.objects.filter(usuario=request.user))
	return HttpResponse(json.dumps(proyectos), content_type="application/json")
