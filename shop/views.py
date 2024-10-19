from django.shortcuts import render

# Create your views here.
# views.py
def catalog (request):
    return render(request, 'shop/catalog.html')  