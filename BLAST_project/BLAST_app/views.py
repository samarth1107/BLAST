from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HomeForm
from .blast_algorithm import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        form=HomeForm(request.POST)
        if form.is_valid():
            sequence = form.cleaned_data['sequence']
            path_to_database = form.cleaned_data['data_base_path']
            # path_to_database = "sequence.fasta"
            align_result = BLAST_DRIVER(sequence,path_to_database)
            return render(request, 'BLAST_app/result.html', {'alignments': align_result})
    form = HomeForm()
    return render(request, 'BLAST_app/home.html', {'form': form})

def result(request):
    return render(request, 'BLAST_app/result.html')