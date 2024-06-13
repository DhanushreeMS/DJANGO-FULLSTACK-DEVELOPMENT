from django.shortcuts import render
from .forms import RegistrationForm

def register_student(request):
    success_message = None 

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Thank you for registering!"
    else:
        form = RegistrationForm()

    return render(request, 'app5/index.html', {'form': form, 'success_message': success_message})

