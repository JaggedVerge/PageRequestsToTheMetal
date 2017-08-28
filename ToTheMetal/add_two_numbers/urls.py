# URL routing for the add_two_numbers app

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.add_two_numbers_page, name='add-two-numbers-page'),
]
