from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# URL CONFIG
urlpatterns = [
    
    # menu links
    path('', website, name="main"),
    path('underthehood/', underthehood, name='underthehood'),

    # redirect links
    path('stock/', stock_form, name="stock_form"),
    path('companydata/', data_form, name="data_form"),
    path('companyoverview', overview_form, name="overview_form"),
    path('econ_indicators/', econ_indicators_form, name="econ_indicators_form"),
    path('commodities/', commodities_form, name="commodities_form"),
    path('forex/', forex_form, name="forex_form"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
