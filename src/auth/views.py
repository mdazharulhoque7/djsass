from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

# Create your views here.
def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if all([username, password]):
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    return render(request, "auth/login.html",{})


def register_view(request):
    if request.POST:
        User = get_user_model()
        username = request.POST['username']
        email = request.POST['email']        
        password = request.POST['password']

        is_user_name_exist = User.objects.filter(username__iexact=username).exists()        
        is_email_exist = User.objects.filter(email__iexact=email).exists()        
        if any([is_user_name_exist, is_email_exist]):
            print(f'Duplicate User with email: {is_email_exist}, username: {is_user_name_exist}')
        try:
            User.objects.create_user(username=username, email=email, password=password)
        except Exception as e:
            print(e)
    return render(request, "auth/register.html",{})