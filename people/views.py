from django.shortcuts import render, redirect, get_object_or_404

from people.models import People


# Create your views here.


def employees_info(request):
    employers_total_info = People.objects.prefetch_related('qualifications').all()

    context = {
        'context': employers_total_info
    }

    return render(request, 'people_list.html', context)


def get_people_info(request, person_id):
    person = get_object_or_404(People.objects.prefetch_related('qualifications'), pk=person_id)
    context = {
        'context': person
    }
    return render(request, 'person_detail.html', context)


