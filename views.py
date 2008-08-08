from django.shortcuts import render_to_response
from django.utils import simplejson
from django.conf import settings
from models import Pledge
from google.appengine.api import urlfetch
  
def pledges(request):
    query = Pledge.all()
    return render_to_response('pledges.html', {'query': query})

def messages(request, pledger):
    pledge = Pledge.get(pledger)
    return render_to_response('message.html', {'pledge': pledge})

def pledge(request):
    pledge = Pledge(
        name=request.POST['name'], 
        postcode=request.POST['postcode'],
        email = request.POST['email'],
        message = request.POST['message'],
    )
    mp_details = getMPDetails(pledge.postcode)
    mp = mp_details['full_name']
    pledge.mp = mp
    pledge.constituency = mp_details['constituency']
    pledge.put()
    return render_to_response('pledge.html', {'mp': mp})
    
def getMPDetails(postcode):
    APIkey = "C8Z3FMFpaXSWAjRkGvAXjppv"
    url = "http://www.theyworkforyou.com/api/getMP?postcode=%s&key=%s" % (postcode, APIkey)
    result = urlfetch.fetch(url)
    return simplejson.loads(result.content)