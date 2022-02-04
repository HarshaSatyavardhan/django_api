from django.urls import path
from api import views



urlpatterns = [
    path('researchpaper/',views.getResearchpapers),
    path('researchpaper/<str:pk>/',views.getResearchpaper)

]