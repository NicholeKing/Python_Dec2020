from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import User, Card

# Create your views here.
def index(request):
    return render(request, "index.html")

def register_user(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        # add a user to the database
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(real_name=request.POST['real_name'], username=request.POST['username'],email=request.POST['email'],password=hash1)
        request.session['logged_in'] = user.id
        return redirect("/dashboard")

def login_user(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['logged_in'] = user.id
        return redirect("/dashboard")

def dashboard(request):
    if 'logged_in' not in request.session:
        return redirect("/")
    context = {
        'logged_in_user': User.objects.get(id=request.session['logged_in'])
    }
    return render(request, "dashboard.html", context)

def cards(request):
    if 'logged_in' not in request.session:
        return redirect("/")
    context = {
        'logged_in_user': User.objects.get(id=request.session['logged_in']),
        'all_cards': Card.objects.all()
    }
    return render(request, "cards.html", context)

def users(request):
    if 'logged_in' not in request.session:
        return redirect("/")
    context = {
        'logged_in_user': User.objects.get(id=request.session['logged_in']),
        'all_users': User.objects.all()
    }
    return render(request, "users.html", context)

def oneuser(request, id):
    if 'logged_in' not in request.session:
        return redirect("/")
    context = {
        'logged_in_user': User.objects.get(id=request.session['logged_in']),
        'one_user': User.objects.get(id=id)
    }
    return render(request, "oneuser.html", context)

def newcard(request):
    if 'logged_in' not in request.session:
        return redirect("/")
    context = {
        'logged_in_user': User.objects.get(id=request.session['logged_in'])
    }
    return render(request, "cardform.html", context)

def add_card(request):
    errors = Card.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/cards/new")
    else:
        Card.objects.create(name=request.POST['name'], image=request.POST['image'], card_type=request.POST['card_type'])
        return redirect("/cards")

def add_to_collection(request, id):
    user = User.objects.get(id=request.session['logged_in'])
    card = Card.objects.get(id=id)
    user.collection.add(card)
    return redirect("/cards")

def remove_from_collection(request, id):
    user = User.objects.get(id=request.session['logged_in'])
    card = Card.objects.get(id=id)
    user.collection.remove(card)
    return redirect("/dashboard")

def logout(request):
    del request.session['logged_in']
    return redirect("/")