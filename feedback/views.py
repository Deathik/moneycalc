from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .forms import FeedbackForm


def feedback_form_handler(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for your reply")
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        return HttpResponseRedirect(reverse('blog:index'))
