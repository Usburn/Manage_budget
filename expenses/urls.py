from . import views
from django.urls import path
urlpatterns = [

path("", views.Home, name= "Home_page") , 
path("all-months", views.all_months, name= "all_months_page"), 
path("all-months/<slug:slug>", views.monthly_expenses, name="single_month_page")
    
]
