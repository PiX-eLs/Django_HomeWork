from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("Main page: list of all articles.")

def my_feed(request):
    return HttpResponse("User's feed: subscribed articles.")

def article_detail(request, article_id):
    return HttpResponse(f"Article ID: {article_id}")

def article_comment(request, article_id):
    return HttpResponse(f"Comment on article ID: {article_id}")

def article_update(request, article_id):
    return HttpResponse(f"Update article ID: {article_id}")

def article_delete(request, article_id):
    return HttpResponse(f"Delete article ID: {article_id}")

def article_create(request):
    return HttpResponse("Create a new article.")

def topics_list(request):
    return HttpResponse("List of all topics.")

def topic_articles(request, topic_id):
    return HttpResponse(f"Articles in topic ID: {topic_id}")

def subscribe_topic(request, topic_id):
    return HttpResponse(f"Subscribed to topic ID: {topic_id}")

def unsubscribe_topic(request, topic_id):
    return HttpResponse(f"Unsubscribed from topic ID: {topic_id}")

def user_profile(request):
    return HttpResponse("User profile page.")

def register_user(request):
    return HttpResponse("Register a new user.")

def set_password(request):
    return HttpResponse("Change password.")

def login_user(request):
    return HttpResponse("Login page.")

def logout_user(request):
    return HttpResponse("Logout.")

def articles_by_date(request, year, month):
    if year < 1000 or year > 9999 or month < 1 or month > 12:
        return HttpResponse("Invalid date!", status=400)
    return HttpResponse(f"Articles for {year}/{month}")

urlpatterns = [
    path('', index, name='index'),  # Главная страница
    path('my-feed/', my_feed, name='my_feed'),  # Лента пользователя
    path('<int:article_id>/', article_detail, name='article_detail'),  # Детали статьи
    path('<int:article_id>/comment/', article_comment, name='article_comment'),  # Комментарии к статье
    path('<int:article_id>/update/', article_update, name='article_update'),  # Обновление статьи
    path('<int:article_id>/delete/', article_delete, name='article_delete'),  # Удаление статьи
    path('create/', article_create, name='article_create'),  # Создание новой статьи
    path('topics/', topics_list, name='topics_list'),  # Перечень всех тем
    path('topics/<int:topic_id>/', topic_articles, name='topic_articles'),  # Статьи по теме
    path('topics/<int:topic_id>/subscribe/', subscribe_topic, name='subscribe_topic'),  # Подписка на тему
    path('topics/<int:topic_id>/unsubscribe/', unsubscribe_topic, name='unsubscribe_topic'),  # Отписка от темы
    path('profile/', user_profile, name='user_profile'),  # Профиль пользователя
    path('register/', register_user, name='register_user'),  # Регистрация пользователя
    path('set-password/', set_password, name='set_password'),  # Изменение пароля
    path('login/', login_user, name='login_user'),  # Вход на сайт
    path('logout/', logout_user, name='logout_user'),  # Выход с сайта
    path('<int:year>/<int:month>/', articles_by_date, name='articles_by_date'),  # Статьи по дате
]
