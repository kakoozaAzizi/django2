from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    
    #context={
    name='Azizi'

    nationality = 'Ugandan'

    age= 24

    #}

    return render(request,'index.html', {'name':name,'nationality':nationality,'age':age})

