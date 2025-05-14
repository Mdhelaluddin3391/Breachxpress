from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteMetadata, NavigationLink, FooterSection, HeroSection, HomeContent,
    Quote, Expose, Tag, Contact, SubmittedStory, AboutPageContent
)


@admin.register(SiteMetadata)
class SiteMetadataAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'contact_email', 'contact_phone', 'facebook_url']
    fieldsets = (
        ('Site Information', {
            'fields': ('site_name', 'footer_tagline', 'footer_text'),
            'description': 'Manage site-wide settings like name and footer text.'
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'contact_address'),
            'description': 'Update contact details displayed in the footer.'
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url'),
            'description': 'Enter URLs for social media profiles (use "#" for inactive links).'
        }),
    )
    actions = None


@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    fields = ['title', 'url', 'order', 'is_active']
    actions = None
    list_per_page = 20
    help_text = "Manage navigation links for navbar and slide menu. Use URLs like '/' for Home."


@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    fields = ['title', 'content', 'order']
    actions = None
    list_per_page = 20
    help_text = "Manage footer sections. Leave content empty for 'Contact Us' and 'Follow Us' (uses Site Metadata)."


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'cta_text']
    fields = ['title', 'description', 'cta_text', 'cta_link']
    actions = None
    list_per_page = 20
    help_text = "Manage the hero section on the homepage."


@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_type', 'get_section_type_display', 'cta_text']
    list_filter = ['section_type']
    search_fields = ['title', 'description']
    fields = ['title', 'description', 'section_type', 'cta_text', 'cta_link']
    list_per_page = 20

    def get_section_type_display(self, obj):
        return obj.get_section_type_display()
    get_section_type_display.short_description = 'Section Type (Friendly)'


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'created_at']
    search_fields = ['text', 'author']
    list_per_page = 20


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_per_page = 20


@admin.register(Expose)
class ExposeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_date', 'is_featured', 'published', 'author', 'category']
    list_filter = ['published_date', 'is_featured', 'published', 'category']
    search_fields = ['title', 'summary', 'content', 'author', 'category', 'meta_description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['published_date']
    ordering = ['-published_date']
    filter_horizontal = ['tags']
    list_per_page = 20
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'summary', 'meta_description', 'content', 'author', 'category'),
            'description': 'Manage the main content of the expose.'
        }),
        ('Media', {
            'fields': ('evidence',),
            'description': 'Upload optional evidence files.'
        }),
        ('Metadata', {
            'fields': ('published_date', 'is_featured', 'published', 'tags'),
            'description': 'Manage publication status and tags.'
        }),
    )


@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'intro_paragraph']
    fields = [
        'intro_paragraph', 'mission_statement', 'second_paragraph',
        'process_step_1', 'process_step_2', 'process_step_3', 'process_step_4',
        'movement_paragraph'
    ]
    list_per_page = 20

    def has_add_permission(self, request):
        return not AboutPageContent.objects.exists()


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at']
    list_filter = ['submitted_at']
    search_fields = ['name', 'email', 'subject']
    list_per_page = 20


@admin.register(SubmittedStory)
class SubmittedStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'category', 'has_evidence', 'evidence_link']
    list_filter = ['created_at', 'category']
    search_fields = ['title', 'summary', 'story', 'meta_description']
    readonly_fields = ['created_at']
    fields = [
        'title', 'summary', 'story', 'meta_description', 'evidence',
        'category', 'tags', 'created_at'
    ]
    filter_horizontal = ['tags']
    list_per_page = 20

    def has_evidence(self, obj):
        return bool(obj.evidence)
    has_evidence.boolean = True
    has_evidence.short_description = 'Evidence Present'

    def evidence_link(self, obj):
        if obj.evidence:
            return format_html('<a href="{}" target="_blank">View Evidence</a>', obj.evidence.url)
        return "No Evidence"
    evidence_link.short_description = 'Evidence'


admin.site.site_header = "Breachxpress Admin"
admin.site.site_title = "Breachxpress Admin"
admin.site.index_title = "Manage Layout and Home Settings"