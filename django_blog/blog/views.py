from django.shortcuts import render, redirect
from .forms import PostRegistrationForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = PostRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PostRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})