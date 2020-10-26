from accounts.views import UserRegistrationView
from django.conf.urls import url
from django.contrib.auth import views as auth_view

app_name = 'accounts'

urlpatterns = [
    url(r'^register/$', UserRegistrationView.as_view(), name="register"),
    url(r'^login/$', auth_view.LoginView.as_view(), {"template_name": "accounts/login.html"}, name="login"),
    url(r'^logout/$', auth_view.LogoutView.as_view(), {"next_page": "/"}, name="logout"),
]
