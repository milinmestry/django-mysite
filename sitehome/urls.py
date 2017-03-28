from django.conf.urls import url

from . import views

app_name = 'sitehome'
urlpatterns = [
    # Process 1
    url(r'^$', views.home, name='home'),
]
