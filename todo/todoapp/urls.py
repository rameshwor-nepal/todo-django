
from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('' ,views.first ,name = 'first'),
    path('create/' ,views.create ,name ='create_todo'),
    path('detail/<int:id>/' ,views.detail ,name='detail_todo'),
    path('detail/<int:id>/deleted' ,views.delete ,name='delete_todo')
]




