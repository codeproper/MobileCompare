from django.conf.urls import include,url
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	url(r'^$', views.new.as_view(),name='new'),
    url(r'^scrape/',TemplateView.as_view(template_name="boot.html")),
    #url(r'^(?P<search_item>[0-9]+)/$', views.ShowApi.as_view()),
]


