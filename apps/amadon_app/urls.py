from django.conf.urls import url
from . import views
#  import our db
#from .models import ###DBNAME###

urlpatterns = [
    # root goes to the index
    url(r'^$', views.index),
    url(r'process', views.process),
    url(r'checkout',views.checkout),
]
