"""final_project_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from cryptocurrency import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alerts/session/<int:session_id>', views.Alert.as_view(), name="getAlerts"),
    path('alerts/', views.Alert.as_view(), name="postNewAlerts"),
    path('alerts/<int:session_id>/status/', views.Alert.as_view(), name="deleteAlert"),
    #path('coin/<slug:coin_id>/', views.CoinSearch.as_view(), name="coin"),
    path('coin/search/', views.CoinSearch.as_view(), name="coinSearch"),
    
    path('session/', views.SessionView.as_view(), name="newSession"),
]
