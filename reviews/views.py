from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Feedback


# Create your views here.
class ReviewView(View):

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


class ReviewList(TemplateView):
    template_name = 'reviews/review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Feedback.objects.all()
        return context


class ReviewDetails(TemplateView):
    template_name = 'reviews/review_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs['id']
        context['review'] = Feedback.objects.get(pk=review_id)
        return context
