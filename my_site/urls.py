"""my_site URL Configuration

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
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap
#from django.conf.urls import patterns
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
import views as vs

blog_urls = [
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^weblog/tags/', include('zinnia.urls.tags')),
    url(r'^weblog/feeds/', include('zinnia.urls.feeds')),
    url(r'^weblog/random/', include('zinnia.urls.random')),
    url(r'^weblog/authors/', include('zinnia.urls.authors')),
    url(r'^weblog/categories/', include('zinnia.urls.categories')),
    url(r'^weblog/comments/', include('zinnia.urls.comments')),
    url(r'^weblog/', include('zinnia.urls.entries')),
    url(r'^weblog/', include('zinnia.urls.archives')),
    url(r'^weblog/', include('zinnia.urls.shortlink')),
    url(r'^weblog/', include('zinnia.urls.quick_entry'))
]
sitemaps = {'tags': TagSitemap,
               'blog': EntrySitemap,
               'authors': AuthorSitemap,
               'categories': CategorySitemap,}

admin.autodiscover()
urlpatterns = [
    url(r'^polls/',    include('polls.urls')),
    url(r'^admin/',    include(admin.site.urls)),
    url(r'^weblog/',   include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^',          include(blog_urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ueditor/',  include('ueditor.urls')),
    url(r'^utest/', vs.test),
    #url(r'^demo/$', 'my_site.views.detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#print urlpatterns
#if settings.DEBUG:  
#   urlpatterns += [url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),         url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),]


