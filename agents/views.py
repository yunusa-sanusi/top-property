from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Agent, SocialAccount
from .forms import AgentForm, SocialAccountForm
from accounts.forms import UpdateForm


def agent_list_view(request):
    agents = Agent.objects.all()

    context = {
        'agents': agents
    }

    return render(request, 'agents/agent-list.html', context)


def agent_details_view(request, slug):
    agent = Agent.objects.get(slug=slug)
    social_accounts = SocialAccount.objects.get(agent=agent)

    context = {
        'agent': agent,
        'social_accounts': social_accounts,
    }

    return render(request, 'agents/agent-details.html', context)


def agent_edit_view(request, slug):
    # instances
    user = request.user
    agent = Agent.objects.get(slug=slug)
    social_account = SocialAccount.objects.get(agent=agent)
    # forms
    agent_form = AgentForm(instance=agent)
    user_form = UpdateForm(instance=user)
    social_account_form = SocialAccountForm(instance=social_account)

    if request.user != agent.user:
        return HttpResponseForbidden(f'<p>Not allowed. You are not authenticated as {agent.user}</p><a href="/agents/">Go back to agent list</a>')
    else:
        if request.method == 'POST':
            agent_form = AgentForm(request.POST, instance=agent)
            user_form = UpdateForm(request.POST, instance=user)
            social_account_form = SocialAccountForm(
                request.POST, instance=social_account)

            if agent_form.is_valid() and user_form.is_valid() and social_account_form.is_valid():
                agent_form.save()
                user_form.save()
                social_account_form.save()
                return redirect('agents:agent-detail', slug=slug)

    context = {
        'agent': agent,
        'agent_form': agent_form,
        'user_form': user_form,
        'social_account_form': social_account_form,
    }

    return render(request, 'agents/agent-edit.html', context)
