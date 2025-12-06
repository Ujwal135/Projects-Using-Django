from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup),
    path('signin',views.signup),
    path('login',views.loginn),
    path('todos',views.todos),
    path('delete_todo/<int:srno>', views.delete_todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('signout/', views.signout, name='signout'),
]   

