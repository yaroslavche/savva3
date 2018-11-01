from django.shortcuts import render
from calenda.models import Event
# Create your views here.
def index(request):
    events = Event.future.order_by('start')
    return render (request, 'index.html', {'events': events})
