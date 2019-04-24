from django.urls import path
from . import views

urlpatterns=[
    # path('login',views.backendLogin,name='login'),
    # path('logout',views.backendLoginout,name="logout"),
    path('',views.HomeView,name="dashboard"),
    path('employee',views.employee,name="employee")

]