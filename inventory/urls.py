from django.urls import path
from . import views
urlpatterns = [
    path('', views.graphql_view, name='graphql'),
]