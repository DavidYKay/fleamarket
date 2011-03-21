########################################
# This holds all views that are native to the project and not the app itself.
########################################

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import NewSellerForm

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
        form = NewSellerForm(request.POST)
        if form.is_valid():
            #new_user = form.save()
            cd = form.cleaned_data
            raw_password = cd['password']
            user = User.objects.create_user(
                cd['username'],
                cd['email'],
            )
            user.set_password(raw_password)
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            # TODO: Add Phone Field
            user.save()
            return HttpResponseRedirect("/listings/")
    else:
        form = NewSellerForm()
    return render_to_response("registration/register.html", {
            'form': form,
        }, 
        context_instance=RequestContext(request)
    )
