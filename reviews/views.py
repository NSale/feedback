from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from .forms import ReviewForm
from .models import Feedback


# Create your views here.
class ReviewView(CreateView):
    model = Feedback
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = 'thanks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYou(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Thank you for submitting your feedback here'
        return context


class ReviewList(ListView):
    template_name = 'reviews/review_list.html'
    model = Feedback
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__lt=10)
        return data


class ReviewDetails(DetailView):
    template_name = 'reviews/review_details.html'
    model = Feedback
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context


class AddFavorite(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)
