from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuarios.views',
  url(r'^$', 'login', name='login'),
  url(r'^logout', 'logout', name='logout')
)