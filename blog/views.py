from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_blog(request):
    return redirect('index', permanent=True)
