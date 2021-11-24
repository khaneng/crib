

from django.conf.urls import url
from supermarket import views

urlpatterns = [
    url(r'^items', views.item),
    url(r'^categories$', views.category),
]
