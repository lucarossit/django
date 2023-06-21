from django import forms
from .models import News
from django.utils.timezone import now

class DateInput(forms.DateInput):
    input_type = 'date'
    def get_context(self, name, value, attrs):
        attrs.setdefault('min', now().strftime('%Y-%m-%d'))
        return super().get_context(name, value, attrs)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'date']
        widgets = {
            'date' : DateInput(),
        }