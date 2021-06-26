from django.urls import path
from . import views

urlpatterns = [
    path('crimes', views.crimes, name='crimes'), 
    path('solvedcrimes', views.solved_crimes, name='solvedcrimes'), 
    path('crime/<int:crime_id>', views.crime, name='crime'),    
    path('report', views.report, name='report'),    
    path('editcrime/<int:crime_id>', views.editcrime, name='editcrime'),
    path('crimelist', views.usercrimelist, name='usercrimelist'),
]