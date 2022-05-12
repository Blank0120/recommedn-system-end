from django.urls import path
from book import views
from book import recommendSystem

urlpatterns = [
    path('books/',views.bookList.as_view()),
    # path('users/', views.userList.as_view()),
    # path('bookRatings/', views.bookRatingsList.as_view()),

    path('login/', views.userList.userLogin),

    path('get_top_ratings/', recommendSystem.get_top_rating),

    path('search_book/',recommendSystem.search_book),

    path('getBookDetail/', recommendSystem.get_book_detail),

    path('get_ratings/', recommendSystem.get_ratings)

]