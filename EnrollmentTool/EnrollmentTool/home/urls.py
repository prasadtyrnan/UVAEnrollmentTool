from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home-home'),
    path('lecture/<int:pk>', views.lecture_detail_view, name='lecture-detail'),
    path('d_l/<int:pk>', views.discussion_detail_view, name='d_l-detail'),
    path('search', views.search, name='search'),
    path('search_results/lv/<str:dp>/<str:cn>', views.SearchListView.as_view(), name='search-results-lv'),
]