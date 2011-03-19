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
        form = NewItemForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            cd = form.cleaned_data
            #send_mail(
            #    cd['subject'],
            #    cd['message'],
            #    cd.get('email', 'noreply@example.com'),
            #    ['siteowner@example.com'],
            #)
            #return HttpResponseRedirect('/contact/thanks/')
        else:
            # throw error
            return HttpResponse("Error! Form invalid. Form: %s" % form)
        return HttpResponseRedirect('/listings/')
    else:
        form = NewItemForm()
        return render_to_response('listings/item_form.html', {'form': form}, context_instance=RequestContext(request))
