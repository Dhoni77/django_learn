from django.shortcuts import render

# Create your views here.
def index(request):
    names = 'Ajay,Kamalesh,Abinash'
    return render(request, 'index.html', { 'names': names, 'firstName': names.split(',')[0] })

def greeting_view(request):
    books = {
        "The Justice": "Don Abeman",
        "The night rider": "Ben Author"
    }
    return render(request, 'simple_tag.html', {'username': 'Ajay', 'books': books })

def greeting_context(request):
    return render(request, 'contextual_greet.html', { 'username': 'Kamal'})