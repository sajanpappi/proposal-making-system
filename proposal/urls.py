from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The landing page (Screen 1)
    path('branding-styling/', views.branding_styling, name='branding_styling'),  # Screen 2
    path('pages-features/', views.pages_features, name='pages_features'),  # Screen 3
    path('associated-services/', views.associated_services, name='associated_services'),  # Screen 4
    path('budget/', views.budget, name='budget'),  # Screen 5
    path('generate-proposal/', views.generate_proposal_view, name='generate_proposal'),
    path('download-proposal/', views.download_proposal, name='download_proposal'),
]

