from django import forms
from .models import Event, Participant
from django.utils.timezone import now

class DateInput(forms.DateInput):
    input_type = 'date'
    def get_context(self, name, value, attrs):
        attrs.setdefault('min', now().strftime('%Y-%m-%d'))
        return super().get_context(name, value, attrs)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date']
        widgets = {
            'date': DateInput(),
        }

class ParticipateForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'event']
