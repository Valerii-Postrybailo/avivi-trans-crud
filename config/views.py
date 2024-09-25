from django.shortcuts import render


def forbidden(request):
    return render(request, 'forbidden.html', status=403)


def main_page(request):
    return render(request, 'base.html')
