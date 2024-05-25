from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Attendee
from .forms import AttendeeForm, EventForm
from django.db.models import Q

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
        attendees = None
    else:
        attendees = event_info.attendees.all()
        
    context = {"event": event_info, 'attendees': attendees}

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

def delete_event(request, id):
    
    try:
        event_to_delete = Event.objects.get(pk=id)
        event_to_delete.delete()
    except:
        event_to_delete = None
    
    return redirect("mainapp:home_page")

def add_attendee(request, id):
    
    event = get_object_or_404(Event, pk=id)
    
    if request.method == "POST":
        form = AttendeeForm(request.POST)

        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event
            attendee.save()
            return redirect("mainapp:event_details", event.id)
    else:
        form = AttendeeForm()
        return render(request, "mainapp/add_attendee.html", {"form": form, "event": event})
        
def delete_attendee(request, id):

    try:
        attendee_to_delete = Attendee.objects.get(pk=id)
        event = attendee_to_delete.event_id
        attendee_to_delete.delete()
    except:
        attendee_to_delete = None
        event = None

    if event:
        return redirect("mainapp:event_details", event)
    else:
        return redirect("mainapp:home_page")