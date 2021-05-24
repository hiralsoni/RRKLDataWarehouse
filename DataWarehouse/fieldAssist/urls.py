from django.urls import include, path
from . import views

urlpatterns = [
  path('getbooks', views.get_books),
  path('addbook', views.add_book),
  path('getLocation', views.external_api_view),
  path('getinnermaster', views.getinnermaster),
  path('getbookDetailss', views.get_booksDetail),

]