import os
import sys
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import ServiceForm

# 🧠 Ensure the current directory is added to sys.path
# (helps VS Code/Pylance resolve local imports correctly)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .models import Service
from .forms import ServiceForm


def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})


@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})
