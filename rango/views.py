from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner!")
def about(request):
    return HttpResponse("The person that is inserting this message asked the tutors where the html had " \
                                   "to be inserted. The answer given was you have to do it yourself. What does the word where have to" \
                                   "do with do it yourself?")
