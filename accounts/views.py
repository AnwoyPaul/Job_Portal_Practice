from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomCreationFrom
from django.contrib.auth.views import LoginView

def signup(request):
  if request.method == 'POST':
    form= CustomCreationFrom(request.POST)
    if form.is_valid():
      form.save()
      return redirect ('login')
  else:
    form=CustomCreationFrom
  return render(request,'accounts/signup.html',{'form':form})


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

