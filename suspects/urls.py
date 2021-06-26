from django.urls import path
from . import views

urlpatterns = [
    path('suspects', views.suspects, name='suspects'), 
    path('nabbedsuspects', views.nabbed_suspects, name='nabbedsuspects'), 
    path('suspect/<int:suspect_id>', views.suspect, name='suspect'),
    path('createsuspect', views.createsuspect, name='createsuspect'),
    path('editsuspect/<int:suspect_id>', views.editsuspect, name='editsuspect'),
    path('suspectlist', views.usersuspectlist, name='usersuspectlist'),
    path('spot/<int:suspect_id>', views.spotted_view, name='spot'),
]