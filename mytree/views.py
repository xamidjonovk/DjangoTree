from django.shortcuts import render

def home_page(request):
    ctx={"name":"Hello world"}
    return render(request, 'index.html', ctx)