from django.urls import path,include
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('delete/', views.delete, name="delete"),
    path('update/', views.update, name='update'),
    path('password_change/', views.password_change, name='password_change'),
]