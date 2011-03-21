########################################
# This holds all views that are native to the project and not the app itself.
########################################

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def profile(request):
    """ Renders user's profile """
    if request.user.is_authenticated():
        # Fetch logged in user
        # pull data about user
        # render user to screen
        # Do something for authenticated users.
        #return HttpResponse("Logged in as: %s" % request.user.username)
        return render_to_response('registration/profile.html', {'user': request.user}, context_instance=RequestContext(request))
    else:
        # Do something for anonymous users.
        return HttpResponse("You are NOT logged in!")

