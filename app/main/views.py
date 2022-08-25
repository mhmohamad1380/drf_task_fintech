
from django.views.generic import TemplateView
from .models import Crypto
# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

class CMCBitcoin(TemplateView):
    template_name = "cmc_btc.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Crypto.objects.all().count() > 0 :
            context["btc_price"] = Crypto.objects.all().order_by("-id")[0]
        return context