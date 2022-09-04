from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    
    #context={
    # name='Azizi'

    # nationality = 'Ugandan'

    # age= 24

    #}


    context={name='Azizi',nationality='Ugandan',age=24.2}

    return render(request,'index.html', context)

