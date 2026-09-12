from django.shortcuts import render


# Create your views here.

def show_qualifications(request):
    return render(request, 'qualifications_list.html')
