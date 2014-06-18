from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuarios.views',
  url('', 'login', name='login')
)