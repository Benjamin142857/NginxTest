from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    data = request.META
    return render(request, 'hello.html', data)