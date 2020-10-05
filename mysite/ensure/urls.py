from django.urls import path
from ensure import view1


urlpatterns = [
    path('',view1.cal,name='ensure'),
    path('add',view1.add,name='add'),

   ]