from django.shortcuts import redirect,render


def login_check(func):
    def wrap(request,*args,**kwargs):
        if not (request.session.get("adminId")):
            return redirect("admin_login")
        else:
            return func(request,*args,**kwargs)
    return wrap


def logout_check(func):
    def wrap(request,*args,**kwargs):
        if  (request.session.get("adminId")):
            return redirect("dashboard")
        else:
            return func(request,*args,**kwargs)
    return wrap