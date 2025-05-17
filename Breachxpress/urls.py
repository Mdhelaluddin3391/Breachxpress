from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from Breach.sitemaps import StaticSitemap, ExposeSitemap ,TagSitemap
from django.views.generic import TemplateView

# Define sitemaps
sitemaps = {
    'tags': TagSitemap,
    'static': StaticSitemap,
    'exposes': ExposeSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Breach.urls')), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.png'))), 
    
    ]
    
from django.conf import settings
from django.conf.urls.static import static

    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

