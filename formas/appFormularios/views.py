from django.shortcuts import render


def show_form(request):
    return render(request, 'registro.html')
# Create your views here.
