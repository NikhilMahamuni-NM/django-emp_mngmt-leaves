import datetime
date_time = datetime.datetime.now()
date = str(date_time.strftime ('%Y-%m-%d')) + ' ' + str(date_time.hour) + ' ' + str(date_time.minute)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile, Leave
from .forms import RegisterUserForm, LeaveForm
from .decorators import allowed, only_admin


@login_required(login_url='leave:login')
@only_admin
def emp_register(request):
    form = RegisterUserForm()
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        username = request.POST['username']
        if form.is_valid():
            user = form.save()
            Profile.objects.create(emp = User.objects.get(username=username), leaves_avai = 10)
            group = Group.objects.get(name='employee')
            user.groups.add(group)
            return redirect('leave:home')
    context = {
        'form' : form
    }
    return render(request, 'registration/emp_registration.html', context)

@login_required(login_url='leave:login')
@only_admin
def mngr_register(request):
    form = RegisterUserForm()
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        username = request.POST['username']
        if form.is_valid():
            user = form.save()
            Profile.objects.create(emp = User.objects.get(username=username), leaves_avai = 10)
            group = Group.objects.get(name='manager')
            user.groups.add(group)
            return redirect('leave:home')
    context = {
        'form' : form
    }
    return render(request, 'registration/mngr_registration.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('leave:home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('leave:home')
        else:
            messages.info(request, 'Username or Password is incorrect')



    context = {
        
    }
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('leave:login')

@login_required(login_url='leave:login')
@only_admin
def home(request):
    context = {
        'employees' : User.objects.filter(groups__name = 'employee'),
        'managers' : User.objects.filter(groups__name = 'manager'),
        'leaves' : Leave.objects.all().order_by('-applied_on')
    }

    return render(request, 'leave/home.html', context)

@login_required(login_url='leave:login')
@allowed(allowed_roles = ['employee'])
def emp_home(request):

    context = {

    }
    return render(request, 'leave/emp_dashboard.html', context)

@login_required(login_url='leave:login')
@allowed(allowed_roles = ['manager','employee'])
def leave_apply(request):
    print(request.user.profile.leaves_avai)
    if request.method == "POST":
        user = request.user
        full_name = request.POST['emp_name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        total = request.POST['total']
        reason = request.POST['reason']
        leaves_avai = request.user.profile.leaves_avai
        leave = Leave(user = user, full_name = full_name, start_date = start_date, end_date = end_date, leaves_avai = leaves_avai, total = total,description = reason)
        leave.save()
        print("Saved Successfully")
        return redirect('leave:leaves')  
    context = {

    }

    return render(request, 'leave/leaveform.html', context)

@login_required(login_url='leave:login')
@allowed(allowed_roles = ['manager'])
def mngr_home(request):

    context = {

    }
    return render(request, 'leave/mngr_dashboard.html', context)

@login_required(login_url='leave:login')
@allowed(allowed_roles = ['manager'])
def leave_approval(request):

    context = {
        'leaves' : Leave.objects.all().order_by('-applied_on').exclude(user=request.user)
    }
    return render(request, 'leave/leaveApprove.html', context)

@login_required(login_url='leave:login')
@allowed(allowed_roles = ['admin', 'manager'])
def leave_detail(request, id):
    obj = Leave.objects.get(pk=id)
    leaves = Leave.objects.filter(user = obj.user)
    if request.method == "POST":
        remark = request.POST['remark']
        approval = True
        approved_by = request.user.first_name + ' ' + request.user.last_name 
        obj.approval = approval
        obj.approved_by = approved_by
        obj.approval_date = datetime.datetime.now()
        leaves_avai = int(obj.leaves_avai) - int(obj.total)
        obj.leaves_avai = leaves_avai
        Leave.objects.filter(user = obj.user).update(leaves_avai = leaves_avai)
        Profile.objects.filter(emp = obj.user).update(leaves_avai = leaves_avai)
        obj.save()
        return redirect('leave:leave_approval')
    context = {
        'leave' : get_object_or_404(Leave, pk=id)
    }
    return render(request, 'leave/leavedetail.html', context)

@login_required(login_url='leave:login')
@allowed(allowed_roles = ['manager','employee'])
def leaves(request):

    context = {
        'leaves' : Leave.objects.filter(user=request.user).order_by('start_date')
    }
    return render(request, 'leave/leaveslist.html', context)

def withdraw(request, id):
    withdraw = get_object_or_404(Leave, pk=id)
    leaves_avai = int(withdraw.leaves_avai) + int(withdraw.total)
    withdraw.leaves_avai = withdraw.leaves_avai
    Leave.objects.filter(user = withdraw.user).update(leaves_avai = leaves_avai)
    Profile.objects.filter(emp = withdraw.user).update(leaves_avai = leaves_avai)
    withdraw.delete()
    context = {
        
    }
    return redirect('leave:leaves')

def disapprove(request, id):
    withdraw = get_object_or_404(Leave, pk=id)
    leaves_avai = int(withdraw.leaves_avai) + int(withdraw.total)
    Leave.objects.filter(user = withdraw.user).update(leaves_avai = leaves_avai, approval = False, 
                                    remark="Disapproved by Admin")
    Profile.objects.filter(emp = withdraw.user).update(leaves_avai = leaves_avai)
    context = {
        
    }
    return redirect('leave:leave_approval')

def dismiss(request, id):
    dismiss = get_object_or_404(Leave, pk=id)
    
    Leave.objects.filter(user = dismiss.user).update(
            approved_by = request.user.first_name + ' ' + request.user.last_name,
            approval_date = datetime.datetime.now(),
            remark = "Dismissed by " + request.user.first_name + ' ' + request.user.last_name
        )
    context = {
        
    }
    return redirect('leave:leave_approval')


