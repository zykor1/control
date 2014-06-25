from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario_donacion(models.Model):
	metodo = models.CharField(max_length=30)
	comentario = models.TextField()
	cantidad = models.DecimalField(max_digits=9, decimal_places=2)
	paypalid = models.TextField()
	fecha_donacion = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)

	class Meta:
		ordering = ["-fecha_donacion"]
		verbose_name_plural = "donaciones"
