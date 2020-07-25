from django.shortcuts import render
from .models import Tourisam

# Create your views here.
def travello_home(request):
    data = Tourisam.objects.all()
    context = {
        'data':data
    }
    return render(request, 'travello/index.html', context)
