from django.shortcuts import render, redirect
from .models import CustomUser, Task


# Create your views here.


def user_page(request):
    if request.method == "POST":
        Name = request.POST.get('full_name')
        Email = request.POST.get('user_email')
        Mobile = request.POST.get('user_mobile')

        user = CustomUser.objects.filter(Email=Email).first()
        if not user:
            CustomUser.objects.create(Name=Name, Email=Email, Mobile=Mobile)
        return redirect("taskapp:login_pages")

    return render(request, 'user/user_page.html')

def login_pages(request):
    if request.method == "POST":

        Email = request.POST.get('user_email')
        Mobile = request.POST.get('user_mobile')
        user = CustomUser.objects.filter(Email=Email, Mobile=Mobile).first()
        if user:
            request.session['user_id'] = user.ID  
            request.session['user_email'] = user.Email  
            return redirect('taskapp:task_page')

    return render(request, 'user/login_pages.html')

def task_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('taskapp:login_pages')

    user = CustomUser.objects.get(ID=user_id)
    tasks = Task.objects.filter(user=user, task_type="Pending") 

    if request.method == "POST":
        task_id = request.POST.get('task_id')
        answer = request.POST.get('user_answer')
        task = Task.objects.get(id=task_id)
        task.answer = answer
        task.task_type = "Done"
        task.save()
        return redirect('taskapp:task_page')  

    context = {'user': user,'tasks': tasks,}

    return render(request, 'user/task_page.html', context)