from django.shortcuts import render,  redirect
from shortner.models import Urls
import random
import string

# Create your views here.
def home(request):
    if request.method == 'POST':
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(20))
        base_url = 'http://127.0.0.1:8000/short/'
        new_url = Urls.objects.create(url = request.POST['url_input'], shortenedURL=random_string)
        URL = base_url + random_string +'/'
        new_url.save()
        return render(request, 'home.html', {'msg': f"The Shortened URL is {URL}"})
    
    else:
        return render(request, 'home.html', {'msg': " "})

def match(request, url):
    try:
        object = Urls.objects.get(shortenedURL=url)
        URL = object.url
        return redirect(URL)
    
    except:
        return render(request, 'home.html', {'msg' : "No URL found, please generate one to use."})
