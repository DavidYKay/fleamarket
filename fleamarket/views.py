########################################
# This holds all views that are native to the project and not the app itself.
########################################

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def profile(request):
    """ Renders user's profile """
    if request.user.is_authenticated():
        # Fetch logged in user
        # pull data about user
        # render user to screen
        # Do something for authenticated users.
        return render_to_response('registration/profile.html', {'user': request.user}, context_instance=RequestContext(request))
    else:
        # Do something for anonymous users.
        return HttpResponse("You are NOT logged in!")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/listings/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
            'form': form,
        }, 
        context_instance=RequestContext(request)
    )
