from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length = 2,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Your Name",
                "data-constraints" : "@Required",
                "id": "contact-your-name-2",
                "class": "form-input"
            }
        )
    )
    email = forms.EmailField(
        min_length = 2,
        widget = forms.EmailInput(
            attrs = {
                "placeholder": "E-Mail",
                "data-constraints" : "@Email @Required",
                "id": "contact-email-2",
                "class": "form-input"
            }
        )
    )
    phone = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Phone",
                "data-constraints" : "@Required",
                "id": "contact-phone-2",
                "class": "form-input"
            }
        )
    )
    text = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                "placeholder": "Message",
                "data-constraints" : "@Required",
                "id": "contact-message-2",
                "class": "form-input"
            }
        )
    )

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User