from django.urls import path, include

from ads import views

urlpatterns = [
    # path('/', views.AdsListView.as_view()),
    # path('/<int:pk>/', views.AdsDetailView.as_view()),
    # path('/create/', views.AdsCreateView.as_view()),
    # path('/<int:pk>/update/', views.AdsUpdateView.as_view()),
    # path('/<int:pk>/delete/', views.AdsDeleteView.as_view()),
    # path('/<int:pk>/upload_image/', views.AdsImageView.as_view()),

    path('user/', include('users.urls')),
]
