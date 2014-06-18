from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuarios.views',
  url(r'^$', 'login', name='login')
)