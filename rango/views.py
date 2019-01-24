from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # Costruct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{boldmessage}} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("The person that is inserting this message asked the tutors where the html had " \
                                   "to be inserted. The answer given was you have to do it yourself. What does the word where have to" \
                                   "do with do it yourself?")
