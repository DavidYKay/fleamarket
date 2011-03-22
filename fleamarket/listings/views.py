# Create your views here.
from django.shortcuts import render_to_response
from models import Item
from forms import NewItemForm
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from forms import WhichSellerForm

########################################
# Seller Methods
########################################

def testPrint(request):
    latest_item_list = Item.objects.all()
    return render_to_response('listings/item_list.html', {
        'latest_item_list': latest_item_list,
    })

def list(request):
    if request.user.is_authenticated():
        # Show current user's items only
        items = Item.objects.filter(seller__exact=request.user)
    else:
        # Show all items. can show 404 instead.
        items = Item.objects.all()
    return render_to_response('listings/item_list.html', {'object_list': items}, context_instance=RequestContext(request))

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

def print_friendly(request):
    """ Render all items in a printer-friendly manner """ 
    if request.user.is_authenticated():
        # Show current user's items only
        items = Item.objects.filter(seller__exact=request.user)
    else:
        # Show all items. Can show 404 instead.
        items = Item.objects.all()
    return render_to_response('listings/item_list_print.html', {'object_list': items}, context_instance=RequestContext(request))

########################################
# Cashier Methods
########################################

def cash_register(request):
    """ User interface for selling items on register. """
    return render_to_response('listings/cash_register.html', context_instance=RequestContext(request))

def checkin(request):
    """ User interface for checking items in/out. """
    return render_to_response('listings/cash_checkin.html', context_instance=RequestContext(request))

def checkin_list(request):
    """ Pick which user to check in/out. """
    form = WhichSellerForm()
    return render_to_response("listings/pick_seller_form.html", {
            'form': form,
        }, 
        context_instance=RequestContext(request)
    )

    #return render_to_response('listings/seller_list.html', context_instance=RequestContext(request))
    #users = User.objects.all()
    #return render_to_response('listings/seller_list.html', {'object_list': users}, context_instance=RequestContext(request))
