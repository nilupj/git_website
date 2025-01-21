from django.urls import path
from django.urls import path, include


from django.urls import path
from . import views

urlpatterns = [
    path('health-topics/', views.health_topics, name='health_topics'),
    path('topic/<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail')
    
]
