from django.conf.urls import include,url
from django.contrib import admin
from django.views.generic import TemplateView
from kaymuscrape import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    url(r'^admin/', admin.site.urls),
    url(r'^kaymuscrape/',include('kaymuscrape.urls')),
    url(r'^KaymuapiView/(?P<search_item1>[\w\+%_& ]+)/', views.ShowKaymuApi.as_view()),
    url(r'^SastoapiView/(?P<search_item2>[\w\+%_& ]+)/', views.ShowSastoApi.as_view()),
    url(r'^viewspecs/(?P<specs_search_item>[\w\+%_& .-]+)', views.specsView),
    url(r'^$',TemplateView.as_view(template_name="index.html")),
    }

urlpatterns= format_suffix_patterns(urlpatterns) 