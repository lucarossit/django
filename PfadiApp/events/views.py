from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from events.models import Event, Participant
from .forms import EventForm, ParticipateForm
from datetime import datetime
from django.db.models import Q

def events(request):
    search_event = request.GET.get('search')
    if search_event:
        events_objs =Event.objects.filter(Q(title__icontains=search_event)).order_by("date")
    else:
        events_objs = Event.objects.filter().order_by("date")
    context = {
        "events": events_objs,
    }
    for event in events_objs:
        if event.date < datetime.today().date():
            deleteEvent('deleteEvent', pk=event.pk)
    return render(request, "events.html", context)

def participate(request):
    if request.method == "POST":
        form = ParticipateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = ParticipateForm()
    return render(request, 'participate.html', {'form': form})

@login_required
def newEvent(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventForm()
    return render(request, 'newEvent.html', {'form': form})

@login_required
def deleteEvent(request, pk):
    Event.objects.filter(pk=pk).delete()
    return redirect('events')

@login_required
def viewParticipants(request, pk):
    participants_objs = Participant.objects.filter(event=pk)
    context = {
        "participants": participants_objs,
    }
    return render(request, "viewParticipants.html", context)

@login_required
def participating(request):
    events_objs = Event.objects.filter(participant__email=request.user.email).order_by("date")
    context = {
        "events": events_objs,
    }
    for event in events_objs:
        if event.date < datetime.today().date():
            deleteEvent('deleteEvent', pk=event.pk)
    return render(request, "events.html", context)