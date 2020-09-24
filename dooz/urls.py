from django.urls import path
from . import views

urlpatterns = [
    path('dooz/', views.render_dooz, name="render_dooz"),
]
