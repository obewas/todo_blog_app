from django.urls import path
from . import views

urlpatterns = [

path('taskList/', views.TaskListView.as_view(), name='taskList'),
path('taskCreate/', views.TaskCreateView.as_view(), name='taskCreate'),
path('taskUpdate/<int:pk>/', views.TaskUpdateView.as_view(), name='taskUpdate'),
path('taskDelete/<int:pk>/', views.TaskDeleteView.as_view(), name='taskDelete'),
path('taskDetail/<int:pk>/', views.TaskDetailView.as_view(), name='taskDetail'),
]

