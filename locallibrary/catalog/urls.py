from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    #re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    #path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    #path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
]
