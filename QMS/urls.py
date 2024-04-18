"""
URL configuration for QMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quotes import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints for Quotes

    # Endpoint for listing all quotes
    path('api/listQuotes/', views.QuotesListView.as_view(), name='listQuotes'),
    
    # Endpoint to create a new quote
    path('api/createQuote/', views.QuotesCreateView.as_view(), name='createQuote'),

    # Endpoint for retrieving a single quote by its primary key
    path('api/getSingleQuote/<int:pk>', views.QuotesRetrieveView.as_view(), name='getSingleQuote'),

    # Endpoint for updating a single quote by its primary key
    path('api/updateQuote/<int:pk>', views.QuotesUpdateView.as_view(), name='updateQuote'),

    # Endpoint for deleting a single quote by its primary key
    path('api/deleteQuote/<int:pk>', views.QuotesDestroyView.as_view(), name='deleteQuote'),

    # API endpoints for JWT Authentication
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
