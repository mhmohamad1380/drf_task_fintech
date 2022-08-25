
from django.urls import path
from .views import CryptoListViewset, CryptoRetrieveUpdateViewset
from dj_rest_auth.urls import LogoutView

urlpatterns = [
    path("list", CryptoListViewset.as_view()),
    path("coin/edit/<pk>", CryptoRetrieveUpdateViewset.as_view()),
    path("logout", LogoutView.as_view()),
]
