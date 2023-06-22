from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render

# Create your views here.


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'admin_all_items': '/',
        'Search by Category': '/?admin_category=category_name',
        'Search by Subcategory': '/?admin_subcategory=category_name',
        'admin_Add': '/create',
        'admin_Update': '/update/pk',
        'admin_Delete': '/item/pk/delete'
    }
    return Response(api_urls)

# Create your views here.
