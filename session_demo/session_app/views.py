from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'happiness' not in request.session:
        request.session['happiness'] = 20
        request.session['energy'] = 30
        request.session['meals'] = 3
        request.session['rested'] = 40
        request.session['death'] = ""
        request.session['alive'] = True
    return render(request, "index.html")

def play(request):
    request.session['happiness'] += 10
    request.session['energy'] -= 5
    print("It worked!")
    if request.session['happiness'] <= 0 or request.session['energy'] <= 0 or request.session['rested'] <= 0:
        request.session['death'] = "OH NO HE'S DEAD!!"
        request.session['alive'] = False
    return redirect("/")

def feed(request):
    if request.session['meals'] > 0:
        request.session['meals'] -= 1
        num = random.randint(5,15)
        request.session['energy'] += num
    else:
        print("You have no meals!")
    if request.session['happiness'] <= 0 or request.session['energy'] <= 0 or request.session['rested'] <= 0:
        request.session['death'] = "OH NO HE'S DEAD!!"
        request.session['alive'] = False
    return redirect("/")

def sleep(request):
    request.session['rested'] += 10
    request.session['happiness'] -= 10
    if request.session['happiness'] <= 0 or request.session['energy'] <= 0 or request.session['rested'] <= 0:
        request.session['death'] = "OH NO HE'S DEAD!!"
        request.session['alive'] = False
    return redirect("/")

def work(request):
    num = random.randint(1,3)
    request.session['meals'] += num
    request.session['rested'] -= 10
    if request.session['happiness'] <= 0 or request.session['energy'] <= 0 or request.session['rested'] <= 0:
        request.session['death'] = "OH NO HE'S DEAD!!"
        request.session['alive'] = False
    return redirect("/")

def reset(request):
    try:
        del request.session['happiness']
    except:
        print("Something went wrong!")
    return redirect("/")

