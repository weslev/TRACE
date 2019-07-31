from django.urls import path
from kickstarterAPI import views

urlpatterns = [
    path('kickstarter/', views.kickstarter_list),
    path('kickstarter/<int:pk>/', views.kickstarter_detail),
]
