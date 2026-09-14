from django.shortcuts import render

from address.models import Address


# Create your views here.


def show_address(request):

    all_address = Address.objects.all()

    context = {
        'context': all_address
    }

    return render(request, 'address_list.html',context)