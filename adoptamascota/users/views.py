from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UserRegisterForm, UserUpdatedForm

def register(request):
    if request.method == 'POST':
    	form = UserRegisterForm(request.POST)
    	if form.is_valid():
    		form.save()
    		return redirect('/organization/create')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
	if request.method =='POST':
		form = UserUpdatedForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserUpdatedForm(instance=request.user)

	return render(request, 'registration/profile.html', {'form': form})

