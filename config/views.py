from django.shortcuts import render
from django.http import JsonResponse


def forbidden(request):
    return render(request, 'forbidden.html', status=403)


def main_page(request):
    return render(request, 'base.html')


def health_check(request):
    return JsonResponse({'status': "healthy"})
