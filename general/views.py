from django.shortcuts import render
from agents.models import Agent
from properties.models import Property


def app_homepage(request):
    agents = Agent.objects.all()
    properties = Property.objects.all().order_by('date_created')
    properties_slider = properties[0:3]

    context = {
        'agents': agents,
        'properties': properties,
        'properties_slider': properties_slider,
    }
    return render(request, 'index.html', context)


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    agents = Agent.objects.all()

    context = {
        'agents': agents,
    }
    return render(request, 'contact.html', context)
