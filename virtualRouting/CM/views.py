from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views import View
from CM import models
from CM.localInfo import authInfo

# Create your views here.


class Login(View):
    @staticmethod
    def get(request):
        return render(request, 'login.html')

    @staticmethod
    def post(request):
        usr = request.POST.get('username')
        psw = request.POST.get('password')
        if usr == authInfo.userInfo['username'] and psw == authInfo.userInfo['password']:
            response = redirect('/')
            response.set_signed_cookie('username', usr, salt=authInfo.key)
            return response
        return render(request, 'login.html')


def authenticate(func):
    def inner(request, *args, **kwargs):
        try:
            usr = request.get_signed_cookie('username', salt=authInfo.key)
        except:
            return redirect('/login/')
        if not usr:
            return redirect('/login/')
        return func(request, *args, **kwargs)
    return inner


@authenticate
def home(request):
    return render(request, 'home.html')


@authenticate
def printRIB(request):
    RIB = models.RoutingTable.objects.all()
    return render(request, 'RIB.html', {'RIB': RIB})


@authenticate
def error(request):
    return render(request, 'error.html')


