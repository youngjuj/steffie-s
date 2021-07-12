from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#alt + enter 하면 오류를 알려주고 오류 해결방법을 제시해줌, 엔터하면 다 해결
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all() #헬로월드라는 리스트에 헬로월드 클래스의 모든 것을 집어넣음

        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})