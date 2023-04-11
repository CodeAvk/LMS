from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',IndexPage,name='index'),
    path('home/', HomePage, name='home'),
    path('signup/',SignupPage,name='signup'),
    path('login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
    path('status/<int:id>',StatusPage,name='status'),
    path('update_password/',ChangePassword,name='change_password'),
    path('forgot_password/',ForgotPassword,name='forgot_password'),
    path('reset_password/<token>/',ResetPassword,name='reset_password'),
    path('contact/',Contact,name='contact'),
    path('about/', About, name='about'),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
