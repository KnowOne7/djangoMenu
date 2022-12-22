"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    
    # /food/
    path('', views.IndexClassView.as_view(), name = 'index'),
    # path('', views.index, name='index'),

    # Detailed View
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # path('<int:item_id>/', views.detail, name='detail'),

    path('item/', views.item, name='item'),
        #add items
    path('add', views.CreateItem.as_view(), name='create_item'),
    # path('add', views.create_item, name='create_item'),
        #update items
    path('update/<int:item_id>/', views.update_item, name='update_item'),
        #delete
    path('delete/<int:item_id>/', views.delete_item, name='delete_item')
    
]
