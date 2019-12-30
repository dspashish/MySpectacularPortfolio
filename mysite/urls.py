
from django.urls import path, include
from .views import home, thank

urlpatterns = [
    path('', home, name='home'),
    path('thank/', thank, name="thank")
]
