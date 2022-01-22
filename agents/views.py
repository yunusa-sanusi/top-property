from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import Agent
from .forms import AgentForm


def agent_list_view(request):
    agents = Agent.objects.all()

    context = {
        'agents': agents
    }

    return render(request, 'agents/agent-list.html', context)


def agent_details_view(request, slug):
    agent = Agent.objects.get(slug=slug)

    context = {
        'agent': agent,
    }

    return render(request, 'agents/agent-details.html', context)


def agent_edit_view(request, slug):
    agent = Agent.objects.get(slug=slug)
    if request.user != agent.user:
        return HttpResponseForbidden(f'<p>Not allowed. You are not authenticated as {agent.user}</p><a href="/agents/">Go back to agent list</a>')
    form = AgentForm(instance=agent)
    context = {
        'agent': agent,
        'form': form,
    }

    return render(request, 'agents/agent-edit.html', context)
