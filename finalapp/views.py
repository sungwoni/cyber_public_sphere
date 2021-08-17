from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, "finalapp/about.html")

def terms_of_use(request):
    return render(request, "finalapp/terms_of_use.html")