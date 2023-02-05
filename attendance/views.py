from .forms import SnippetForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Snippet
import datetime
from django.contrib.auth.decorators import login_required
import random


def index(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                # Check if user with the same email already exists
                existing_snippet = Snippet.objects.get(email=email)
                existing_snippet.points += 1
                # need this line to go into the db, delete the event info and rewrite it
                existing_snippet.save()
                return HttpResponseRedirect(reverse('attendance:completed'))
            except Snippet.DoesNotExist:
                # If user does not exist, create a new one
                new_snippet = form.save()
                new_snippet.points += 1
                new_snippet.save()
                return HttpResponseRedirect(reverse('attendance:completed'))
    else:
        form = SnippetForm
        return render(request, 'attendance/form.html', {'form': form})


def completed_detail(request):
    return render(request, 'attendance/completed.html')


def rankings_view(request):
    top_seven = Snippet.objects.all().order_by('-points')[:7]
    return render(request, 'attendance/rankings.html', {'top_seven': top_seven})


def archive(request, year, month, day):
    date = datetime.datetime(year, month, day)
    entries = Snippet.objects.filter(created_at__date=date)
    return render(request, 'archive.html', {'entries': entries})


@login_required
def winner(request):
    fr_recipient = random.choice(Snippet.objects.filter(FR=True))
    so_recipient = random.choice(Snippet.objects.filter(SO=True))
    jr_recipient = random.choice(Snippet.objects.filter(JR=True))
    sr_recipient = random.choice(Snippet.objects.filter(SR=True))
    return render(request, 'attendance/winner.html', {
        'fr_recipient': fr_recipient,
        'so_recipient': so_recipient,
        'jr_recipient': jr_recipient,
        'sr_recipient': sr_recipient,
    })
