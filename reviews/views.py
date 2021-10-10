from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Feedback


# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            feedback = Feedback(user_name=data['user_name'],
                                review_text=data['review_text'],
                                rating=data['rating'])
            feedback.save()
            return HttpResponseRedirect('thanks')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {
        'form': form,
    })


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
