from django.urls import path
from . import views

urlpatterns=[
    # path('login',views.backendLogin,name='login'),
    # path('logout',views.backendLoginout,name="logout"),
    path('',views.HomeView,name="dashboard"),
    path('branch',views.branch,name="branch"),
    path('department',views.department,name="department"),
    path('designation',views.designation,name="designation"),
    path('employee',views.employee,name="employee"),
    path('addemployee',views.addemployee,name="addemployee"),

]