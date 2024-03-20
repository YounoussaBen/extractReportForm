from django.urls import path
from . import views
from .views import GeneratePdf, ApplicationCreateView

urlpatterns = [
    path('pdf/', GeneratePdf.as_view(),name='pdf'), 
    path('create_application/', ApplicationCreateView.as_view(), name='create_application'),

]