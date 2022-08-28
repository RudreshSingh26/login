from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def register_request(request):
	messages.info(request, 'register step.')
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homeapp:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="homeapp/register.html", context={"register_form":form})

def homepage(request):
    return render(request,'homeapp/homepage.html')    
	# homeapp:index

def login_request(request):
	messages.info(request, 'Login step.')
	if request.method == "POST":
		messages.info(request, 'Login step.')
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homeapp:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="homeapp/login.html", context={"login_form":form})	

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homeapp:homepage")	