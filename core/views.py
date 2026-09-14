from django.shortcuts import render

from people.models import People


# Create your views here.

def show_homepage(request):
    all_people = People.objects.prefetch_related('qualifications').all()

    context = {
        'context': all_people
    }

    return render(request, 'home_page.html', context)
