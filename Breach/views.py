from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import HeroSection, HomeContent, SiteMetadata, NavigationLink, FooterSection, Quote, Expose, Tag, AboutPageContent, Contact, SubmittedStory
from .forms import ContactForm, SubmittedStoryForm
import logging

logger = logging.getLogger(__name__)


from django.contrib.auth.models import User
from django.db.utils import OperationalError

def create_superuser():
    try:
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='mdhelal',
                email='muhammadhelal123',
                password='helal123'
            )
            print("Superuser created successfully")
    except OperationalError:
        print("Database not ready, skipping superuser creation")

create_superuser()


def get_base_context():
    """Returns base context with site metadata, navigation links, and footer sections."""
    site_metadata = SiteMetadata.objects.first()
    nav_links = NavigationLink.objects.filter(is_active=True)
    footer_sections = FooterSection.objects.all()
    return {
        'site_metadata': site_metadata,
        'nav_links': nav_links,
        'footer_sections': footer_sections,
    }

def home(request):
    """Renders the homepage with hero section, content sections, and recent exposes."""
    context = {
        **get_base_context(),
        'hero_section': HeroSection.objects.first(),
        'mission_section': HomeContent.objects.filter(section_type='mission').first(),
        'expose_section': HomeContent.objects.filter(section_type='expose').first(),
        'truth_section': HomeContent.objects.filter(section_type='truth').first(),
        'community_section': HomeContent.objects.filter(section_type='community').first(),
        'recent_exposes': Expose.objects.filter(published=True).order_by('-published_date')[:3],
        'featured_expose': Expose.objects.filter(published=True).order_by('-published_date').first(),
    }
    return render(request, 'home.html', context)

def exposes(request):
    """Renders the exposes list page with pagination and featured expose."""
    expose_list = Expose.objects.filter(published=True)
    paginator = Paginator(expose_list, 10)
    page_number = request.GET.get('page')
    exposes = paginator.get_page(page_number)
    featured_expose = Expose.objects.filter(is_featured=True, published=True).first()
    quote = Quote.objects.first()
    context = {
        **get_base_context(),
        'exposes': exposes,
        'featured_expose': featured_expose,
        'quote': quote,
    }
    return render(request, 'exposes.html', context)

def article_detail(request, slug):
    """Renders the detail page for a specific expose with related exposes."""
    expose = get_object_or_404(Expose, slug=slug, published=True)
    related_exposes = Expose.objects.filter(tags__in=expose.tags.all(), published=True).exclude(slug=slug).distinct()[:3]
    if not related_exposes:
        related_exposes = Expose.objects.filter(published=True).exclude(slug=slug).order_by('-published_date')[:5]
    context = {
        **get_base_context(),
        'expose': expose,
        'related_exposes': related_exposes,
    }
    return render(request, 'article_detail.html', context)

def tag_detail(request, slug):
    """Renders the detail page for a specific tag with associated exposes."""
    tag = get_object_or_404(Tag, slug=slug)
    expose_list = tag.exposes.filter(published=True)
    paginator = Paginator(expose_list, 10)
    page_number = request.GET.get('page')
    exposes = paginator.get_page(page_number)
    context = {
        **get_base_context(),
        'tag': tag,
        'exposes': exposes,
    }
    return render(request, 'tag_detail.html', context)



def submit_story(request):
    """Handles user-submitted stories and creates corresponding Expose."""
    if request.method == 'POST':
        form = SubmittedStoryForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                story = form.save(commit=False)
                story.save() 
                form.save_m2m() 
                
                expose = Expose.objects.create(
                    title=story.title,
                    summary=story.summary,
                    content=story.story,
                    evidence=story.evidence,
                    is_featured=False,
                    category=story.category,
                    slug=story.slug,
                    author="Anonymous",
                    meta_description=story.meta_description,
                    published=True,
                )
                expose.tags.set(story.tags.all())  # Copy tags
                logger.info(f"Created story and expose: {story.title}, Category: {expose.category}, Author: {expose.author}, Tags: {list(expose.tags.values_list('name', flat=True))}")
                messages.success(request, 'Your story has been published successfully!', extra_tags='green-message')
                return redirect('exposes')
            except Exception as e:
                logger.error(f"Error saving story or creating Expose: {str(e)}")
                messages.error(request, 'Error publishing story. Please try again.', extra_tags='error-message')
        else:
            logger.error(f"Form errors: {form.errors}")
            error_message = 'Please correct the following errors: ' + '; '.join([f"{field}: {error[0]}" for field, error in form.errors.items()])
            messages.error(request, error_message, extra_tags='error-message')
    else:
        form = SubmittedStoryForm()
    context = {
        **get_base_context(),
        'form': form,
    }
    return render(request, 'submit_story.html', context)
    
def about(request):
    """Renders the about page with content from AboutPageContent."""
    about_content = AboutPageContent.objects.first()
    context = {
        **get_base_context(),
        'about_content': about_content,
    }
    return render(request, 'about.html', context)




def contact(request):
    """Handles contact form submissions."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been saved! We will get back to you soon.', extra_tags='green-message')
            return redirect('contact')
        else:
            logger.error(f"Contact form errors: {form.errors}")
            error_message = 'Please correct the following errors: ' + '; '.join([f"{field}: {error[0]}" for field, error in form.errors.items()])
            messages.error(request, error_message, extra_tags='error-message')
    else:
        form = ContactForm()
    context = {
        **get_base_context(),
        'form': form,
    }
    return render(request, 'contact.html', context)

def custom_404(request, exception):
    """Renders a custom 404 error page."""
    context = {
        **get_base_context(),
        'message': 'Page not found.',
    }
    return render(request, '404.html', context, status=404)

def community(request):
    """Renders the community page."""
    return render(request, 'community.html')
    
def terms_conditions(request):
    """Renders the Conditions page."""
    return render(request, 'terms_conditions.html')
    
def privacy(request):
    """Renders the Privacy page."""
    return render(request, 'privacy.html')
         
        