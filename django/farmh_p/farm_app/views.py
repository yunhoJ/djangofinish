# 작성자 : 김지영

from django.shortcuts import redirect, render, get_object_or_404


from decimal import Context
from .python.weather import Weathers
from django.http.response import JsonResponse
from .python.darkflow.deep import deepTo
from farm_app.python.ocr import ocrtest
from farm_app.python.SST import SpeechToText
from farm_app.python.changeEx import Change
#from django.http import HttpResponse
from .forms import *
from .models import  Images, Users, Comments, Crops, Deeplearnings, Dronerunnings,Farmdiaries, Pestinfos, Ptcinfos, DeepImages,privent # 모델 불러오기
from .models import History,OcrRsult,Audio
from django.http import HttpResponse, request
import PIL.Image as Image
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
# Create your views here.

# 메인페이지 출력 / css폴더에 있는 html연결
#def home(request):
#    return HttpResponse('login.html')
    
def Main(request):

    return render(request, 'Main.html')

# 데이터확인하기
# 디비연동이 성공적으로 되었는지 데이터를 출력

# 사용자
def users_view(request):
    users = Users.objects.all()
    #post테이블의 모든  객체 불러와서 posts변수에 저장
    return render(request, 'Main.html',{"users": users})


#
def comments_view(request):
    comments = Comments.objects.all() 
    return render(request, 'Main.html',{"comments": comments})

#딥러닝
def deeplearnings_view(request):
    deeplearnings = Deeplearnings.objects.all()  
    return render(request, 'Main.html',{"deeplearnings": deeplearnings})

#드론
def dronerunnings_view(request):
    dronerunnings = Dronerunnings.objects.all()   
    return render(request, 'Main.html',{"dronerunnings": dronerunnings})

#이력관리
def farmdiaries_view(request):
    farmdiaries = Farmdiaries.objects.all()  
    return render(request, 'Main.html',{"farmdiaries": farmdiaries})

#
def pestinfos_view(request):
    pestinfos = Pestinfos.objects.all()    
    return render(request, 'login.html',{"pestinfos": pestinfos})

#
def ptcinfos_view(request):
    ptcinfos = Ptcinfos.objects.all()  
    return render(request, 'login.html',{"ptcinfos": ptcinfos})

#
def crops_view(request):
    crops = Crops.objects.all()    
    return render(request, 'login.html',{"crops": crops})

# 드론 
def drone(req):
    
    return render(req,"drone_control.html")

def history(req):
    history = History()
    
    return render(req,"history.html")


def analysis(req):
    profile=DeepImages.objects.last()
    print(profile)
    
    return render(req,"analysis.html",{"profile":profile})

def result(req):
    profile=Images.objects.last()
    img=DeepImages()
    print(profile,"profffff")
    uniq=deepTo.deep(profile)    
    try:
        img.deepimages="output/img_result{}.jpg".format(uniq)
        # Image.fromarray(deepTo.deep(profile)
        print(img.deepimages)
        img.save()
    except Exception as e:
        print(e)
    global deepResultName
    deepResultName=""
    name=deepTo.deepName()
    print(name)
    if name=="D_leaf_spot":
        name="점무늬병"
        deepResultName="점무늬병"
    elif name=="D_leaf_mold":
        name="잎곰팡이병"
        deepResultName="잎곰팡이병"

    confidence=deepTo.deepConfidence
    prof=DeepImages.objects.last()
    prevent=privent.objects.filter(pr_bug=deepResultName)
    
    print(prof,"test")
    return render(req,"result.html",{"prof":prof,"name":name,"confidence":confidence,"prevent":prevent})

def upload(request):
    return render(request,'upload.html')

#이미지업로드
def upload_create(req):
    
    img = Images()
    img.images = req.FILES['images'] 
    print(img.images)
    img.save()
    return redirect('/result')

    # form = Images(request.POST, request.FILES)
    # form.images=request.FILES['images']
    # form.save()
    # return Images('/farm_app/media/')  

#def profile(request):
#    profile=Images.objects.all()
#    return render(request,'profile.html',{'profile':profile})



def test(req):
    city=Weathers.city()
    condition=Weathers.condition()
    temp=Weathers.temp()
    precip_mm=Weathers.precip_mm()
    humidity=Weathers.humidity()
    
    return render(req,"test.html",{"humidity":humidity,"precip_mm":precip_mm,"temp":temp,"condition":condition,"city":city})

from django.db.models import Q
def ptc(req):
    test=Ptcinfos.objects.filter(Q(ptc_pest="점무늬병")&Q(ptc_plant="토마토(방울토마토포함)") ) 
    # test=Ptcinfos.objects.filter(Q(ptc_plant="토마토")|Q(ptc_plant="방울토마토")|Q(ptc_plant="토마토(방울토마토포함)"))
    return render(req,"test2.html",{"test":test})

def fertilizer(req):
    deepResultName
    spot=Ptcinfos.objects.filter(Q(ptc_pest=deepResultName)&Q(ptc_plant="토마토(방울토마토포함)"))

    return render(req,"fertilizer.html",{"spot":spot})

def result_drone(req):
    prof=DeepImages.objects.last()
    name=deepTo.deepName()
    print(name)
    if name=="D_leaf_spot":
        name="점무늬병"
       
    elif name=="D_leaf_mold":
        name="잎곰팡이병"
        
    confidence=deepTo.deepConfidence
    return render(req,"result_drone.html",{"prof":prof,"name":name,"confidence":confidence})


    #농약이미지업로드
def history_create(req):
    
    himg = History() 
    himg.history = req.FILES['images']    
    himg.save()
    return redirect('/ocr_result')



#농약 분석 이미지 업로드 
def ocr_result(req):
    profile=History.objects.last()
    img=OcrRsult()
    print(profile,"profffff")
    uniq=ocrtest.detect_text(profile)
    global textptc
    textptc=ocrtest.uniqq()
    try:
        img.ocrresult="ocrResult/img_result{}.jpg".format(uniq)
        print(img.ocrresult)
        img.save()
    except Exception as e:
        print(e)
    ocr_result_img=OcrRsult.objects.last()
    return render(req,"ocr_result.html",{"textptc":textptc,"ocr_result_img":ocr_result_img})

def qr(req):
    return render(req ,"qr.html")


def test3(req):
    profile=History.objects.last()
    profil=Images.objects.last()
    return render(req,"test3.html",{"profile":profile,"profil":profil})
import time
def history_audio(req):
    file=Audio()
    file.audio=req.FILES["audio"]
    # print(req.FILES["audio"])
    file.save()
    audio=req.FILES["audio"]
    print(audio,"te")
    wav=Change.changem4a(audio)
    global textSST
    textSST=SpeechToText.run_quickstart(wav)
    return redirect("/history_text")

def history_text(req):
    city=Weathers.city()
    condition=Weathers.condition()
    temp=Weathers.temp()
    precip_mm=Weathers.precip_mm()
    humidity=Weathers.humidity()
    profile=Audio.objects.last()
    textptc
    textSST
    return render(req,"history_text.html",{"humidity":humidity,"precip_mm":precip_mm,"temp":temp,"condition":condition,"city":city,"textSST":textSST,"textptc":textptc})

def qr_url(request):
   
    if (request.method=="POST"):
        id=request.POST.get("user_id")
        pw=request.POST.get("user_passowrd")
        test=Users.objects.filter(user_id=id)
        print(id)
        print(pw)
   
    
    return render(request,"qr.html",{"test":test,"pw":pw})


# 영농일지 기록 확인
def diary(request):
    return render(request,'diary.html')

def ajaxproject(request):
    template = loader.get_template('/templates/diary.html')
    context1 = {'latest_question_list': "5tte"}  
    return HttpResponse(template.render(context1,request))

@csrf_exempt
def diary_view(request):
    data = request.POST
    data = data['day']
    a = Farmdiaries.objects.filter(r_date__contains = data).values()
    return JsonResponse(list(a), safe=False)


def fertilizer_images(req):
    img=History.objects.all().order_by("history")
    return render(req,"fertilizer_images.html",{"img":img})

from datetime import datetime
def test4(req):
    global imgdeepsave
    imgdeepsave=DeepImages.objects.last()
    
    return render(req,"test4.html",{"imgdeepsave":imgdeepsave})
def test6(request):
    global deepimgsrc
    if (request.method=="POST"):
        deepimgsrc=request.POST.get("imgsrc")
        print(deepimgsrc)

    return render(request,"history.html",)
def test5(req):
 
    return render(req,"main.html")

def save(request):
    if(request.method=="POST"):
        plant=request.POST.get("plant")
        city=request.POST.get("city")
        condition=request.POST.get("condition")
        temp=request.POST.get("temp")
        precip_mm=request.POST.get("precip_mm")
        humidity=request.POST.get("humidity")
        textptc=request.POST.get("textptc")
        tt=request.POST.get("tt")
        farm=Farmdiaries()
        farm.r_pic1=deepimgsrc 
        farm.user=Users(user_id="ok0921")
        farm.r_date=datetime.now()
        farm.r_plant="토마토"
        farm.r_weather=condition
        farm.r_high_c=temp
        farm.r_low_c=precip_mm
        farm.r_hum=humidity
        farm.r_ptc_name=textptc
        farm.r_ftz=tt
        farm.r_diary=textSST
        farm.save()        
    return render(request,"history.html",{"img":imgdeepsave})