from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import Occupant
from .forms import OccupantForm


def main_page(request):
    occupants = Occupant.objects.all()
    return render(request, 'main_page.html', {
        'occupants': occupants
    })


def owner_panel(request):
    return render(request, 'owner_panel.html', {})


def owner_panel_create(request):
    if request.method == 'POST':
        form = OccupantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = OccupantForm()
        return render(request, 'owner_panel_create.html', {
            'form': form
        })


def occupant_page(request, page_name):
    occupant = Occupant.objects.get(page_name=page_name)
    return render(request, 'occupant_page.html', {
        'occupant': occupant
    })


def edit_occupant(request, page_name):
    occupant = Occupant.objects.get(page_name=page_name)
    if request.method == 'POST':
        form = OccupantForm(request.POST, request.FILES, instance=occupant)
        if form.is_valid():
            form.save()
            return redirect('occupant_page', page_name=occupant.page_name)
        else:
            return render(request, 'edit_occupant.html', {
                'form': form
            })
    else:
        form = OccupantForm(instance=occupant)
        return render(request, 'edit_occupant.html', {
            'form': form
        })
