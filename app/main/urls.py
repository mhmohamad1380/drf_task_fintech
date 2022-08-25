from django.urls import path
from .views import HomeView, CMCBitcoin

urlpatterns = [
    path("", HomeView.as_view()),
    path("coinmarketcap/bitcoin", CMCBitcoin.as_view())
]
