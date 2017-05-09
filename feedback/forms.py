from django.forms.models import ModelForm

from .models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'feedback')

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['feedback'].widget.attrs.update({'class': 'form-control'})