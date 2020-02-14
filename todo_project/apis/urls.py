from django.urls import path, include


from .views import ListTodo, DetailTodo

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    	#path to djoser end points
   
]
