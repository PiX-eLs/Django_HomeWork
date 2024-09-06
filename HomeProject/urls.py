"""
URL configuration for HomeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: __import__('django.http').http.HttpResponse("All Articles Page"), name='all_articles'),
    path('my-feed/', lambda request: __import__('django.http').http.HttpResponse("My Feed Page"), name='my_feed'),
    path('<int:article_id>/', lambda request, article_id: __import__('django.http').http.HttpResponse(f"Article Detail Page for article {article_id}"), name='article_detail'),
    path('<int:article_id>/comment/', lambda request, article_id: __import__('django.http').http.HttpResponse(f"Write Comment for article {article_id}"), name='write_comment'),
    path('<int:article_id>/update/', lambda request, article_id: __import__('django.http').http.HttpResponse(f"Update Article {article_id}"), name='update_article'),
    path('<int:article_id>/delete/', lambda request, article_id: __import__('django.http').http.HttpResponse(f"Delete Article {article_id}"), name='delete_article'),
    path('create/', lambda request: __import__('django.http').http.HttpResponse("Create Article Page"), name='create_article'),
    path('topics/', lambda request: __import__('django.http').http.HttpResponse("Topics List Page"), name='topics_list'),
    path('topics/<int:topic_id>/', lambda request, topic_id: __import__('django.http').http.HttpResponse(f"Articles for Topic {topic_id}"), name='topic_articles'),
    path('topics/<int:topic_id>/subscribe/', lambda request, topic_id: __import__('django.http').http.HttpResponse(f"Subscribed to Topic {topic_id}"), name='subscribe_topic'),
    path('topics/<int:topic_id>/unsubscribe/', lambda request, topic_id: __import__('django.http').http.HttpResponse(f"Unsubscribed from Topic {topic_id}"), name='unsubscribe_topic'),
    path('profile/', lambda request: __import__('django.http').http.HttpResponse("Profile Page"), name='profile'),
    path('register/', lambda request: __import__('django.http').http.HttpResponse("Register Page"), name='register'),
    path('set-password/', lambda request: __import__('django.http').http.HttpResponse("Set Password Page"), name='set_password'),
    path('login/', lambda request: __import__('django.http').http.HttpResponse("Login Page"), name='login'),
    path('logout/', lambda request: __import__('django.http').http.HttpResponse("Logout Page"), name='logout'),
    path('<int:year>/<int:month>/', lambda request, year, month: (
    __import__('django.http').http.HttpResponse(f"Articles for {year}-{month}") if (1 <= month <= 12) and (year >= 100) 
    else __import__('django.http').http.Http404("Invalid date")
    ), name='articles_by_date'),
]
