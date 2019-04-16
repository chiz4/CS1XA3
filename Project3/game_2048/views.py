import json

from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_protect

from game_2048 import models
from game_2048.models import GameUser, ScoreRecord

# @csrf_protect
def update_score(request):
    result = {"status": 200, "data": "success",'score':0}
    score1=0
    if request.method=="POST":
        body_re=request.body.decode(encoding='utf-8')
        # json_body=json.loads(body_re,encoding='utf-8')
        list_get=body_re.split('&')
        list1_get=list_get[0].split('=')
        list2_get=list_get[1].split('=')
        # username=json_body['username']
        # userscore=json_body['score']
        username=list1_get[1]
        userscore=int(list2_get[1])
        score1=userscore
        max_score = ScoreRecord.objects.aggregate(Max("max_score"))
        if max_score['max_score__max']:
            score1=max_score['max_score__max']
        if GameUser.objects.filter(user_name=username).exists():
            u_id = GameUser.objects.get(user_name=username)
            if ScoreRecord.objects.filter(u_id=u_id).exists():
                max_score=ScoreRecord.objects.aggregate(Max("max_score"))
                if max_score['max_score__max']<userscore:
                    score1=userscore
                    ScoreRecord.objects.filter(u_id=u_id).delete()
                    score=ScoreRecord()
                    score.u_id=u_id
                    score.max_score=userscore
                    score.save()
            else:
                score = ScoreRecord()
                score.u_id = u_id
                score.max_score = userscore
                score.save()
        result['score']=score1
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")




# @login_required(login_url='/login/')
# @login_required
def index(request):
    print(request.path)
    max_score = ScoreRecord.objects.aggregate(Max("max_score"))
    if max_score:
        max_score_vies=max_score["max_score__max"]
    else:
        max_score_vies=0
    username=request.path[7:]
    return render(request,'game_2048/index.html',{'username': username,'maxs':max_score_vies})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "please input all values！"
        # user = authenticate(user_name=username, password=password)
        # if user:
        #     login()
        if username and password:
            username = username.strip()
            try:
                user = models.GameUser.objects.get(user_name=username)
                if user.password == password:
                    return redirect('/index/'+user.user_name)
                else:
                    message = "Wrong Password！"
            except:
                message = "User don't exist！"
        return render(request, 'game_2048/login.html', {"message": message})
    return render(request, 'game_2048/login.html')



def logout(request):
    return redirect('/login/')