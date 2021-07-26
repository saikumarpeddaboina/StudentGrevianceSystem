from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Complaint


# Create your views here.
@login_required()
def home(request):
    form = UserForm(request.POST or None)
    if request.method == "POST" and form.is_valid:
        form.save()
        print(form)
        return redirect('home_db')
    return render(request, 'dash/home.html', {'form': form})


# def dash(request):

@login_required()
def status(request):
    email = request.user.email
    print(email)
    a = Complaint.objects.filter(email=email)
    print(a)
    return render(request, 'dash/status.html', {'complaints': a})

# Create your views here.


@login_required()
def dashboard(request):
    is_head = request.user.profile.is_head
    if not is_head:
        return HttpResponse("You are not Authorised to view this page !")
    if request.method == "POST":
        print("In POST")
        print(request.POST.get('com_id'), request.POST.get('status_choice'))
        obj = Complaint.objects.filter(
            cid=int(request.POST.get('com_id'))).first()
        d = {'ca': "Complaint Accepted",
             'nc': 'Need more clarity', 'is': 'Issue solved'}
        try:
            obj.status = d[request.POST.get('status_choice')]
            obj.save()
        except KeyError:
            print("Got key error")
    branch = request.user.profile.branch
    a = Complaint.objects.filter(branch=branch)
    finance = Complaint.objects.filter(
        branch=branch, complaint_regarding="Finance")
    admission = Complaint.objects.filter(
        branch=branch, complaint_regarding="Admission")
    exam = Complaint.objects.filter(
        branch=branch, complaint_regarding="Examination")
    learn = Complaint.objects.filter(
        branch=branch, complaint_regarding="Learning")
    context = {'a': a, 'ad': admission, 'fi': finance, 'ex': exam, 'le': learn}

    return render(request, 'dash/dash.html', context)
