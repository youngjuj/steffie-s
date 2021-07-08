from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#alt + enter 하면 오류를 알려주고 오류 해결방법을 제시해줌, 엔터하면 다 해결


def hello_world(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'POST METHOD'})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD'})