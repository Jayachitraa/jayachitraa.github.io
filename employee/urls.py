from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('create_employee/', views.create_employee, name='create_employee'),
]
