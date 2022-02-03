from django.urls import path

from .views import *
from .drf_views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('games/<str:game>', views.game, name='game'),
    path('games/<str:game>/token/<path:token>', views.regenerate_token, name='game'),
    path('games/', views.games, name='games'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile')
]

drf_urlpatterns = [
    path('api/v1/login/<game>/<username>/<password>/', GameApiView.as_view())
]


urlpatterns = [*urlpatterns, *drf_urlpatterns]
