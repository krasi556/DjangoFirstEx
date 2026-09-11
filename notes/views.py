from django.http import HttpResponse
from django.shortcuts import render

from notes.models import Note


# Create your views here.


def notes_view(request, ):
    notes = Note.objects.all()

    context = {
        'notes': notes
    }
    return render(request,'note_detail.html', context)
