from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
	nombre = models.CharField(max_length=30)
	comentario = models.TextField()
	creado = models.DateTimeField(auto_now=True)
	creado_por = models.ForeignKey(User)

	class Meta:
		ordering = ["-creado"]
		verbose_name_plural = "Proyectos"


class TipoProyecto(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()


class ConfiguracionProyecto(models.Model):
	proyecto = models.OneToOneField(Proyecto)
	tipo = models.ForeignKey(TipoProyecto)


class ParticipanteProyecto(models.Model):
	ESTADOS = {"Activo" : 1, "Inactivo" : 0}
	ACTIVO = 1
	INACTIVO = 0
	usuario = models.ForeignKey(User)
	proyecto = models.ForeignKey(Proyecto)
	fecha_agregado = models.DateTimeField(auto_now=True)
	estado = models.BooleanField()

	class Meta:
		ordering = ["-fecha_agregado", "-proyecto"]
		verbose_name_plural = "Participantes"