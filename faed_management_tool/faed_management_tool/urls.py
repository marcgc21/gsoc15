"""faed_management_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from faed_drone_publisher.views import drone_detail
from faed_management.views import HangarsView, HangarsList, DropPointsView, DropPointsList, MeteoStationsList, MeteoStationsView
from django.views.generic.base import TemplateView
from rest_framework import routers

from faed_management import views


router = routers.DefaultRouter()
router.register(r'hangars', views.HangarViewSet, 'hangars')
router.register(r'droppoints', views.DropPointViewSet, 'droppoints')
router.register(r'meteostations', views.MeteoStationViewSet, 'meteostations')

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^index/$', TemplateView.as_view(template_name='index.html')),
    url(r'^styleurlform/$', views.submit_styleurl),
    url(r'^droneform/$', views.submit_drone),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^hangars/$', HangarsView.as_view(), name='hangars-list'),
    url(r'^hangar_list/$', HangarsList.as_view()),
    url(r'^hangarform/$', views.submit_hangar),

    url(r'^droppoints/$', DropPointsView.as_view(), name='droppoint-list'),
    url(r'^droppoint_list/$', DropPointsList.as_view()),
    url(r'^droppointform/$', views.submit_droppoint),

    url(r'^meteostations/$', MeteoStationsView.as_view(), name='meteostations_list'),
    url(r'^meteostations_list/$', MeteoStationsList.as_view()),
    url(r'^meteostationform/$', views.submit_meteostation),

    url(r'^drone/(?P<drone_plate>\w+)/$', drone_detail),

]
