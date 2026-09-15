from django.shortcuts import render, redirect

from people.models import People


# Create your views here.

def show_homepage(request):
    all_people = People.objects.prefetch_related('qualifications').all()

    context = {
        'context': all_people
    }

    return render(request, 'home_page.html', context)


def redirect_to_homepage(request):
    return redirect('core:homepage')


def custom_500(request):

    return render(request, '500.html', status=500)