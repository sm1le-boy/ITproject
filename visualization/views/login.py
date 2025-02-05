
from .views import *


def login(request):
    # User.test1()
    # smile boy
    return render(request,"test.html",{"data":"WTF"})

def test1(request):
    return render(request,"templates/test.html","test1")