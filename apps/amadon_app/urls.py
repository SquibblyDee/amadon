from django.conf.urls import url
from . import views

urlpatterns = [
    # root goes to the index
    url(r'^$', views.index),
    # process our order
    url(r'process', views.process),
    # output order results and history
    url(r'checkout',views.checkout),
]
