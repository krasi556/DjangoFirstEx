from django.shortcuts import render

from categories.models import Category


# Create your views here.

def list_of_categories(request):
    all_categories = Category.objects.prefetch_related('notes')

    context = {
        'categories': all_categories
    }

    return render(request, 'category_detail.html', context)


def current_category_detail(request, category_id):
    category = Category.objects.prefetch_related('notes').get(id=category_id)

    context = {
        'category': category
    }

    return render(request, 'each_category.html', context)
