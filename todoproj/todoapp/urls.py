
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('update/<int:id>',views.Update,name='update'),
    
    path('delete/<int:id>',views.Delete,name='delete'),
    path('view/<int:id>',views.view,name='view'),
    
    
    
    # path('contact/',views.contact,name='contact')

]
