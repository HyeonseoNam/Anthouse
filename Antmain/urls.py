from django.conf.urls import include, url , patterns
from . import views

urlpatterns = patterns('Antmain.views',
    url(r'^$', 'antmain', name='antmain'),

)

