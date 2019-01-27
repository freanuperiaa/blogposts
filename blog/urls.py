from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('newpost/', views.BlogCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    
]
