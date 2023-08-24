from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages module
from .forms import ContEmpMastForm

def create_employee(request):
    if request.method == 'POST':
        form = ContEmpMastForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee details submitted successfully.')  # Add success message
            return redirect('create_employee')  # Redirect to the form after successful submission
    else:
        form = ContEmpMastForm()

    return render(request, 'index.html', {'form': form})
