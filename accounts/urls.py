from django.urls import path

from . import views
from .views import RegisterView, TokenCreate
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenCreate.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add_child/', views.child_add, name='add_child'),
    path('get_all_scores/', views.get_list_score, name='get_all_score'),
    path('get_share_link/<int:children_id>/', views.make_token, name='get_share_link'),
    path('get_children_by_token/', views.get_static_token, name='get_statistic'),
    ]