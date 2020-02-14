from django.urls import path


from .views import ListTodo, DetailTodo, ListEvents, DetailEvents

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('events/', ListEvents.as_view()),
    path('events/<int:pk>', DetailEvents.as_view())
]
