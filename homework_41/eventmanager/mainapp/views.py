from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def index(request):
    
    query = request.GET.get("query")
    
    if query:
        events = Event.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))
    else:
        events = Event.objects.all()
    
    context = {"events": events}
    
    return render(request, "mainapp/index.html", context)

def event_details(request, id):

    try:
        event_info = Event.objects.get(pk=id)
    except:
        event_info = None
        participants = None
    else:
        participants = event_info.user.all()
        
    context = {"event": event_info, 'participants': participants}

    return render(request, "mainapp/event_details.html", context)

def add_event(request):
    
    if request.method == "POST":
        form = EventForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("mainapp:home_page")
    else:
        form = EventForm()
        return render(request, "mainapp/add_event.html", {"form": form})

@permission_required("mainapp.delete_event")
def delete_event(request, id):
    
    try:
        event_to_delete = Event.objects.get(pk=id)
        event_to_delete.delete()
    except:
        event_to_delete = None

    return redirect("mainapp:home_page")



@login_required(login_url="login")
def participate(request, event_id):

    event = get_object_or_404(Event, pk=event_id)
    event.user.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url="login")
def unparticipate(request, event_id):

    event = get_object_or_404(Event, pk=event_id)
    event.user.remove(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@permission_required("mainapp:change_event")
def remove_participant(request, event_id, user_id):
    event = get_object_or_404(Event, pk=event_id)
    user_to_remove = get_object_or_404(User, pk=user_id)

    if user_to_remove in event.user.all():
        event.user.remove(user_to_remove)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))