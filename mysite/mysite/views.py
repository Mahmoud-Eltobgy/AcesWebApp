from django.shortcuts import redirect

def login_redirect(request):
    if request.user.is_authenticated():
        return redirect('/home')
    return redirect('/login')
