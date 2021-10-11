from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm


# Create your views here.
class Feedback(View):

    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form,
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks')
        else:
            return render(request, 'reviews/review.html', {
                'form': form,
            })


class ThankYou(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Thank you for submitting your feedback here'
        return context
