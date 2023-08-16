from django.urls import path
from  rest_framework.authtoken.views import obtain_auth_token
from make_token_user_app.views import RegistrationView, LogoutView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
