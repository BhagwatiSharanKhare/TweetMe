from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "Your Message", "class": "form-control",  'cols': 30}))
    class Meta:
        model = Tweet
        fields = [
        # "user",
        "content",
        ]
        # exclude = ['content']

    # def clean_content(self, *args, **kwargs):
    #     tweet = self.cleaned_data.get("tweet")
    #     if tweet == "":
    #         raise forms.ValidationError("Cannot be empty")
    #     return tweet

# both validator.py & form one works together

# form & .py validator override default
