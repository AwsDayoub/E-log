from unicodedata import name
from django.urls import  path
from . import views

""" Defines URL patterns for elogs """

app_name = 'elogs'

urlpatterns = [
    # Home Page
    path('', views.posts, name='posts'),
    # Add a post
    path('new_post/',views.new_post, name='new_post'),
    # Page show all comments of a post
    path('comments/<int:post_id>', views.comments, name='comments'),
    # Page for editing a comment
    path('edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
    # Page for adding a comment
    path('add_comment/<int:post_id>', views.add_comment, name='add_comment'),

]