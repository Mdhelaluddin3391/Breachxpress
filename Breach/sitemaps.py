from django.contrib.sitemaps import Sitemap
from .models import Expose, Tag
from django.urls import reverse

# Sitemap for static pages
class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return [
            {'url': '/', 'priority': 1.0, 'changefreq': 'daily'},
            {'url': '/about/', 'priority': 0.9, 'changefreq': 'monthly'},
            {'url': '/contact/', 'priority': 0.8, 'changefreq': 'monthly'},
            {'url': '/submit-story/', 'priority': 0.8, 'changefreq': 'monthly'},
            {'url': '/exposes/', 'priority': 0.9, 'changefreq': 'daily'},
            {'url': '/community/', 'priority': 0.7, 'changefreq': 'monthly'}, 
        ]

    def location(self, item):
        return item['url']

    def priority(self, item):
        return item['priority']

    def changefreq(self, item):
        return item['changefreq']

# Sitemap for Expose model
class ExposeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Expose.objects.filter(published=True)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.published_date

# Sitemap for Tag model
class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Tag.objects.all()

    def location(self, obj):
        return reverse('tag_detail', kwargs={'slug': obj.slug})

# Sitemap for Navigation Links
class NavigationLinkSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return NavigationLink.objects.filter(is_active=True)

    def location(self, obj):
        return obj.url