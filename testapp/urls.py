#mycode
from django.urls import path
from . import views
urlpatterns= [ path('',views.index,name='index'),
    path('add/',views.add,name='Addition'),
    path('add/add_dis/',views.add_dis,name='Addition display'),
]
