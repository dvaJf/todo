

from django.urls import path, include
from . import views
urlpatterns = [
    path('main',views.index),
    path('reg',views.reg),
    path('sigin',views.sigin),
    path('task',views.task),
    path('profile',views.profile),
    path('sigin/',views.user_login, name="sigin"),
    path('logout/',views.user_logout, name="logout"),
    path('reg/', views.Register.as_view(), name="reg"),
]
