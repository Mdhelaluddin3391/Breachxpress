from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.utils.html import strip_tags
from ckeditor.fields import RichTextField


def generate_unique_slug(model_class, title, timestamp=None):
    
    if timestamp is None:
        timestamp = timezone.now()
    base_slug = slugify(title)
    slug = f"{base_slug}-{timestamp.strftime('%Y%m%d%H%M%S')}"
    while model_class.objects.filter(slug=slug).exists():
        timestamp = timezone.now()
        slug = f"{base_slug}-{timestamp.strftime('%Y%m%d%H%M%S')}"
    return slug


class SiteMetadata(models.Model):
    """Stores site-wide metadata like name, contact details, and social media links."""
    site_name = models.CharField(max_length=100, default="BreachXpress", verbose_name="Site Name")
    footer_tagline = models.CharField(max_length=200, default="Exposing corruption, one story at a time.", verbose_name="Footer Tagline")
    footer_text = models.CharField(max_length=200, default="© 2025 BreachXpress. All Rights Reserved.", verbose_name="Footer Copyright Text")
    contact_email = models.EmailField(default="contact@BreachXpress.com", verbose_name="Contact Email")
    contact_phone = models.CharField(max_length=20, default="+123-456-7890", verbose_name="Contact Phone")
    contact_address = models.CharField(max_length=200, default="123, Justice Street, Truth City", verbose_name="Contact Address")
    facebook_url = models.URLField(default="#", verbose_name="Facebook URL")
    twitter_url = models.URLField(default="#", verbose_name="Twitter URL")
    instagram_url = models.URLField(default="#", verbose_name="Instagram URL")
    linkedin_url = models.URLField(default="#", verbose_name="LinkedIn URL")

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Site Metadata"
        verbose_name_plural = "Site Metadata"


class NavigationLink(models.Model):
    """Manages navigation links for navbar and slide menu."""
    title = models.CharField(max_length=100, verbose_name="Link Title")
    url = models.CharField(max_length=200, default="/", verbose_name="Link URL")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Navigation Link"
        verbose_name_plural = "Navigation Links"


class FooterSection(models.Model):
    """Manages footer sections with titles and optional content."""
    title = models.CharField(max_length=100, verbose_name="Section Title")
    content = models.TextField(blank=True, verbose_name="Section Content")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Footer Section"
        verbose_name_plural = "Footer Sections"


class HeroSection(models.Model):
    """Manages the hero section content for the homepage."""
    title = models.CharField(max_length=200, default="Welcome to BreachXpress", verbose_name="Hero Title")
    description = models.TextField(
        default="Join us in exposing corruption and empowering whistleblowers. Share your story and be part of a movement for justice.",
        verbose_name="Hero Description"
    )
    cta_text = models.CharField(max_length=100, default="Submit Your Story", verbose_name="CTA Text")
    cta_link = models.URLField(default="#", verbose_name="CTA Link")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"


class HomeContent(models.Model):
    """Manages content sections for the homepage (e.g., mission, community)."""
    SECTION_TYPES = (
        ('mission', 'Mission Section'),
        ('expose', 'Featured Expose Section'),
        ('truth', 'Why Truth Matters Section'),
        ('community', 'Community Section'),
    )
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    section_type = models.CharField(max_length=50, choices=SECTION_TYPES, unique=True, verbose_name="Section Type")
    cta_text = models.CharField(max_length=100, blank=True, verbose_name="CTA Text")
    cta_link = models.CharField(max_length=200, blank=True, verbose_name="CTA Link")

    def __str__(self):
        return f"{self.title} ({self.get_section_type_display()})"

    class Meta:
        verbose_name = "Home Content Section"
        verbose_name_plural = "Home Content Sections"


class Tag(models.Model):
    """Manages tags for categorizing Expose and SubmittedStory instances."""
    name = models.CharField(max_length=50, verbose_name="Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Expose(models.Model):
    """Represents published articles exposing corruption or stories."""
    title = models.CharField(max_length=255, verbose_name="Title")
    summary = models.TextField(verbose_name="Summary")
    content = RichTextField(verbose_name="Content")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Published Date")
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name="Slug")
    evidence = models.FileField(
        upload_to='evidence/',
        blank=True,
        null=True,
        help_text="Optional evidence file (PDF, JPG, PNG, DOC)",
        verbose_name="Evidence"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Is Featured")
    tags = models.ManyToManyField(Tag, related_name='exposes', blank=True, verbose_name="Tags")
    category = models.CharField(max_length=50, blank=True, verbose_name="Category")
    author = models.CharField(max_length=100, blank=True, null=True, verbose_name="Author")
    published = models.BooleanField(default=False, verbose_name="Is Published")
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="Custom meta description for SEO (max 160 chars)",
        verbose_name="Meta Description"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Expose, self.title)
        super().save(*args, **kwargs)

    def reading_time(self):
        """Calculate estimated reading time based on word count."""
        word_count = len(strip_tags(self.content).split())
        minutes = max(1, round(word_count / 200))
        return f"{minutes} min read"

    class Meta:
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['published_date']),
            models.Index(fields=['slug']),
        ]
        verbose_name = "Expose"
        verbose_name_plural = "Exposes"


class SubmittedStory(models.Model):
    """Represents user-submitted stories before they are published as Expose."""
    CATEGORY_CHOICES = (
        ('user_submited', 'User Submited'),
        ('corruption', 'Corruption'),
        ('investigative', 'Investigative'),
        ('justic', 'Justic'),
        ('other', 'Other'),
    )
    title = models.CharField(max_length=255, verbose_name="Title")
    summary = models.TextField(verbose_name="Summary")
    story = RichTextField(verbose_name="Story")
    evidence = models.FileField(
        upload_to='evidence/',
        blank=True,
        null=True,
        help_text="Optional evidence file (PDF, JPG, PNG, DOC)",
        verbose_name="Evidence"
    )
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Slug")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='user_submitted',
        verbose_name="Category"
    )
    tags = models.ManyToManyField(Tag, related_name='submitted_stories', blank=True, verbose_name="Tags")
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="Custom meta description for SEO (max 160 chars)",
        verbose_name="Meta Description"
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(SubmittedStory, self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['title', 'created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['slug']),
        ]
        verbose_name = "Submitted Story"
        verbose_name_plural = "Submitted Stories"


class Quote(models.Model):
    """Stores inspirational quotes for display on the site."""
    text = models.CharField(max_length=500, verbose_name="Quote Text")
    author = models.CharField(max_length=100, blank=True, verbose_name="Author")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"{self.text} - {self.author or 'Unknown'}"

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"


class AboutPageContent(models.Model):
    """Manages content for the About page."""
    intro_paragraph = models.TextField(blank=True, null=True, verbose_name="Intro Paragraph")
    mission_statement = models.CharField(max_length=200, blank=True, null=True, verbose_name="Mission Statement")
    second_paragraph = models.TextField(blank=True, null=True, verbose_name="Second Paragraph")
    process_step_1 = models.TextField(blank=True, null=True, verbose_name="Process Step 1")
    process_step_2 = models.TextField(blank=True, null=True, verbose_name="Process Step 2")
    process_step_3 = models.TextField(blank=True, null=True, verbose_name="Process Step 3")
    process_step_4 = models.TextField(blank=True, null=True, verbose_name="Process Step 4")
    movement_paragraph = models.TextField(blank=True, null=True, verbose_name="Movement Paragraph")

    def __str__(self):
        return "About Page Content"

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"
        
        
class Contact(models.Model):
    """Stores contact form submissions from users."""
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted At")

    def __str__(self):
        return f"Message from {self.email} at {self.submitted_at}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"        