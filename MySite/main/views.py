from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'main/index.html')


def about_me(request):
    return render(request, 'main/about_me.html')


def my_projects(request):
    projects = Projects.objects.order_by('-date_added')

    context = {'projects': projects}

    return render(request, 'main/my_projects.html', context)


def project_view(request, project_slug):
    project = Projects.objects.get(project_slug=project_slug)
    images = ProjectPhoto.objects.prefetch_related('project').filter(project=project.id)

    context = {'project': project, 'project_photo': images}

    return render(request, 'main/project.html', context)


@login_required(login_url='users:login')
def order_view(request):
    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST, files=request.FILES)
        print(request.FILES)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = request.user
            form.save()
            return redirect('main:index')

    context = {'form': form}
    return render(request, 'main/order.html', context)
