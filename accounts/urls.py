from django.conf.urls import url
from django.views.generic import TemplateView
from accounts.views import UserProfileView

urlpatterns = [

    url(r'^login/$', 'django.contrib.auth.views.login', name='login_url'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout_url'),

    # url(r'^accounts/signup/$', 'Antmain.views.register', name='registration'),
    url(r'^signup/$', 'accounts.views.signup', name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view(template_name='registration/signup_ok.html'), name='signup_ok'),
    url(r'^(?P<method>update/)$', TemplateView.as_view(template_name='accounts/profile')),
    url(r'^profile/$', UserProfileView.as_view(), name="edit_profile"),
    # url(r'^profile/update/$', UserUpdateView.as_view(), name="user_update"),

]


