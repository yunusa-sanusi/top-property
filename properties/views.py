from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import AmenityForm, PropertyForm, PropertyImageForm
from .models import Amenity, Property, PropertyImage
from agents.models import Agent, SocialAccount


def property_list_view(request):
    properties = Property.objects.all()

    context = {
        'properties': properties,
    }
    return render(request, 'properties/property-list.html', context)


@login_required(login_url='accounts:login')
def property_create_view(request):
    agent = Agent.objects.get(user=request.user)
    amenity_form = AmenityForm
    property_form = PropertyForm
    property_image_form = PropertyImageForm

    if request.method == 'POST':
        amenity_form = AmenityForm(request.POST)
        property_form = PropertyForm(request.POST, request.FILES)
        property_image_form = PropertyImageForm(request.POST, request.FILES)

        if amenity_form.is_valid() and property_form.is_valid() and property_image_form.is_valid():
            property = property_form.save(commit=False)
            property.agent = agent
            property.save()

            amenities = amenity_form.cleaned_data['amenity'].split(',')

            for amenity in amenities:
                Amenity.objects.create(property=property, amenity=amenity)
            for image in request.FILES.getlist('image'):
                PropertyImage.objects.create(property=property, image=image)

            return redirect('properties:property-list')

    context = {
        'amenity_form': amenity_form,
        'property_form': property_form,
        'property_image_form': property_image_form,
    }
    return render(request, 'properties/property-create.html', context)


def property_detail_view(request, slug):
    property = Property.objects.get(slug=slug)
    amenities = Amenity.objects.filter(property=property) or None
    property_images = PropertyImage.objects.filter(property=property)
    social_accounts = SocialAccount.objects.get(agent=property.agent) or None

    context = {
        'property': property,
        'amenities': amenities,
        'property_images': property_images,
        'social_accounts': social_accounts,
    }
    return render(request, 'properties/property-detail.html', context)


@login_required(login_url='accounts:login')
def property_update_view(request, slug):
    property = Property.objects.get(slug=slug)
    property_form = PropertyForm(instance=property)

    if request.user != property.agent.user:
        return HttpResponseForbidden(f'<p>Not allowed. You are not authenticated as {property.agent.user}</p><a href="/agents/">Go back to agent list</a>')

    if request.method == 'POST':
        property_form = PropertyForm(
            request.POST, request.FILES, instance=property)

        if property_form.is_valid():
            new_property = property_form.save()

            return redirect('properties:property-detail', new_property.slug)

    context = {
        'property_form': property_form,
    }

    return render(request, 'properties/property-update.html', context)


@login_required(login_url='accounts:login')
def property_delete_view(request, slug):
    property = Property.objects.get(slug=slug)
    if request.user != property.agent.user:
        return HttpResponseForbidden(f'<p>Not allowed. You are not authenticated as {property.agent.user}</p><a href="/agents/">Go back to agent list</a>')

    if request.method == 'POST':
        property.delete()
        return redirect('properties:property-list')

    return render(request, 'properties/property-delete.html', {'property': property})
