from django.shortcuts import render, get_object_or_404

from people.models import People
from qualifications.models import Qualifications


# Create your views here.

def show_qualifications(request):
    total_qualifications = Qualifications.objects.prefetch_related('people').all()

    context = {
        'context': total_qualifications
    }

    return render(request, 'qualifications_list.html', context)

