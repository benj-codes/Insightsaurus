from django.forms import ModelForm, widgets
from django import forms
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'reviewBody']

        labels = {'value': 'Do you like this analysis? Cast your vote: 👍 or 👎', 'reviewBody': 'Feel free to leave a comment!'}

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

