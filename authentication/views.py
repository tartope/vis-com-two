from django.http import HttpResponse
# use this to render and redirect the page
from django.shortcuts import redirect, render
# use this to save the user in the db
from django.contrib.auth.models import User
# use messages to tell the user they were registered successfully
from django.contrib import messages
# use this to authenticate (check if username/password is the same as db) the user during login; if authenticated then login
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

# build how signup function will work:
def signup(request):
    if request.method == 'POST':
        # take all form fields entered by user and store it in a variable; can be written two ways:
        # username = request.POST.get('username')
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        # after the user submits all these inputs, register them in the db
        myuser = User.objects.create_user(username=username, password=password)
        # if you want:
        # myuser.username

        # uses the import above to save the user in the db
        myuser.save()

        # uses the import above to send message
        messages.success(request, "Your account has been successfully created.")

        # after successful signup, redirect user to the login page
        return redirect('log_in')

    return render(request, "authentication/signup.html")


# See Django docs: How to log a user in (https://docs.djangoproject.com/en/4.1/topics/auth/default/#auth-web-requests)
def log_in(request):
    # take all form fields entered by user and store it in a variable; can be written two ways:
    # username = request.POST.get('username')

    # if they go to the login webpage and login (POST) then do soemthing; else, just show the login page:
    # if user goes to the login page and fills it out (POSTed something)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        # authenticate the user (this returns a "None" response if the user is not authenticated; or "not None" response if the user is authenticated)
        user = authenticate(username=username, password=password)

        # check if user is not None (authenticated), login below, and use dictionary below to send welcome message in index.html:
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "authentication/index.html", {'username': username})
        # else, if user is None (not authenticated), send error message and redirect to home page
        else:
            messages.error(request, "Bad credentials")
            return redirect('home')

    # else, just render the page
    return render(request, "authentication/login.html")


# do not need to render anything for logout
def logOut(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')


# from here create and develop the template/authentication: index/login/signup files