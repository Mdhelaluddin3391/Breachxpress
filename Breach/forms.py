from django import forms
from .models import Contact, SubmittedStory
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter the subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message here'}),
        }
        

from django import forms
from .models import SubmittedStory, Tag

class SubmittedStoryForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = SubmittedStory
        fields = ['title', 'summary', 'story', 'evidence', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter story title', 'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'placeholder': 'Enter a brief summary', 'class': 'form-control'}),
            'story': forms.Textarea(attrs={'placeholder': 'Write your story', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_evidence(self):
        evidence = self.cleaned_data.get('evidence')
        if evidence:
            if evidence.size > 100 * 1024 * 1024:  
                raise forms.ValidationError("File size must be under 100MB.")
            if not evidence.name.lower().endswith(('.pdf', '.jpg', '.jpeg', '.png', '.doc', '.docx')):
                raise forms.ValidationError("Only PDF, JPG, PNG, and DOC files are allowed.")
        return evidence        
        
        
        
   