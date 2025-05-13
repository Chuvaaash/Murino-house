from django.shortcuts import render, redirect
# from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# from django.contrib.sessions.models import Session

from .models import Occupant, KissTransaction
from .forms import OccupantForm

import datetime


def main_page(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
    else:
        user = None
    occupants = Occupant.objects.all()
    return render(request, 'main_page.html', {
        'occupants': occupants,
        'user': user
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
    occupant_hobbies = Occupant.objects.get(page_name=page_name).hobbies.all()
    return render(request, 'occupant_page.html', {
        'occupant': occupant,
        'occupant_hobbies': occupant_hobbies
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


def login_page(request):
    if request.method == 'POST':
        user_name = request.POST.get("login")
        user_password = request.POST.get("password")
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("<p>Invalid login!</p>")

    else:
        return render(request, 'login_page.html', {

        })


def logout_view(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get("login")
        user_password = request.POST.get("password")
        if len(user_name) > 3 and len(user_password) > 3:
            User.objects.create_user(user_name, "", user_password)
            return redirect('/')
        else:
            return HttpResponse("Enter more than 3 symbols")

    else:
        return render(request, 'signup_page.html', {

        })


def interactions(request, page_name):
    # return HttpResponse("<p>interactions</p>")
    occupant = Occupant.objects.get(page_name=page_name)
    introduction = occupant.interact()
    occupant_hobbies = Occupant.objects.get(page_name=page_name).hobbies.all()
    return render(request, 'interaction_page.html', {
        'occupant': occupant,
        'introduction': introduction,
        'occupant_hobbies': occupant_hobbies
    })


def kisses(request):
    if request.method == 'POST':
        return HttpResponse("<p>kisse</p>")

    else:
        kiss_transactions = KissTransaction.objects.all()
        return render(request, 'kiss_transactions.html', {
            'kiss_transactions': kiss_transactions
        })


def requestkisses(request):
    if request.method == 'POST':
        # return HttpResponse('requestkisses post')
        amount = request.POST.get('amount')
        amount = int(amount)

        today_date = datetime.date.today()
        qs = KissTransaction.objects.filter(request_date=today_date)
        qs_lentgh = qs.count()
        kisses_requested_today = 0
        for el in qs:
            kisses_requested_today += el.number_of_kisses

        if kisses_requested_today > 10:
            return render(request, 'requestkisses.html', {
                'kisses_requested_today': kisses_requested_today
            })


        if amount > 10:
            return render(request, 'requestkisses.html', {
                'amount': amount
            })
        occupant = Occupant.objects.get(page_name='Mishka')
        now = datetime.date.today()
        transaction = KissTransaction.objects.create(
            requested_by=occupant,
            number_of_kisses=amount,
            request_date=now,
            kiss_transaction_status=KissTransaction.REQUESTED)
        return redirect(kisses)

    else:
        amount = 0
        return render(request, 'requestkisses.html', {
            'amount': amount
        })
