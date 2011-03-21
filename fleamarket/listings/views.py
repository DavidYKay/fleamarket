# Create your views here.
from django.shortcuts import render_to_response
from models import Item
from forms import NewItemForm
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

def testPrint(request):
    latest_item_list = Item.objects.all()
    return render_to_response('listings/item_list.html', {
        'latest_item_list': latest_item_list,
    })

def new(request):
    if request.method == 'POST':
        # We're accepting form data for save to DB
        if not request.user.is_authenticated():
            return render_to_response('registration/pleaselogin.html')
        form = NewItemForm(request.POST)
        if not form.is_valid():
            # throw error
            return HttpResponse("Error! Form invalid. Form: %s" % form)
        else:
            new_item = form.save(commit=False) 

            # grab the user id from the current user
            #new_item.seller = request.user.id
            new_item.seller = request.user

            #cd = form.cleaned_data
            new_item.save()
            #send_mail(
            #    cd['subject'],
            #    cd['message'],
            #    cd.get('email', 'noreply@example.com'),
            #    ['siteowner@example.com'],
            #)
            #return HttpResponseRedirect('/contact/thanks/')
        return HttpResponseRedirect('/listings/')
    else:
        # user GET
        if not request.user.is_authenticated():
            # not logged in
            return render_to_response('registration/pleaselogin.html')
        else:
            # we are logged in
            form = NewItemForm()
            return render_to_response('listings/item_form.html', {'form': form}, context_instance=RequestContext(request))
