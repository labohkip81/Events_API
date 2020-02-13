from django.urls import path


from .views import ListTodo, DetailTodo, UserCreate

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('users/', UserCreate.as_view(), name='user_create'),
]
