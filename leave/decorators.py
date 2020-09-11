from django.http import HttpResponse
from django.shortcuts import redirect

def allowed(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                #return HttpResponse('You are not Authorised to View this!')
                return redirect('leave:home')
        return wrapper_func
    return decorator

def only_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        group = request.user.groups.all()[0].name

        if group == 'employee':
            return redirect('leave:emp_home')

        if group == 'None':
            return redirect('leave:login')
        
        if group == 'manager':
            return redirect('leave:mngr_home')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func
    