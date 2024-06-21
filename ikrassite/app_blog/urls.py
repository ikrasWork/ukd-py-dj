# app_blog/urls.py
from django.urls import path

from .views import (HomePageView, ArticleDetail, ArticleList, ArticleCategoryList, FeedbackList, AddFeedback, AboutView)

urlpatterns = [
    path(r'', HomePageView.as_view(), name='home'),
    path(r'articles', ArticleList.as_view(), name='articles-list'),
    path(r'articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
    path(r'articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
    path(r'about/', AboutView.as_view(), name='about'),
    path(r'feedbacks/', FeedbackList.as_view(), name='feedbacks-list'),
    path(r'feedbacks/add/', AddFeedback.as_view(), name='add-feedback'),
]
