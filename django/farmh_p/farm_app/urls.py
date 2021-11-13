from django.urls import path
from . import views
import farm_app
from django.conf.urls import url 

urlpatterns = [
    path("",views.Main,name="main"),
    # path("123/",views.Insert,name="create"),
    path("drone/",views.drone,name="drone"),
    
    path("history/",views.history,name="history"),
    path("analysis/",views.analysis,name="analysis"),
    path("result/",views.result,name="result"),
    path("result_drone/",views.result_drone,name="result_drone"),
    path("fertilizer/",views.fertilizer,name="fertilizer"),
    path('farm_app/history_create/',views.history_create,name="history_create"),
    path('farm_app/upload/',views.upload,name="upload"),
    path('farm_app/upload_create/',views.upload_create,name="upload_create"),
    path("test/",views.test,name="test"),
    path("test2/",views.ptc,name="test2"),
    path("test3/",views.test3,name="test3"),
    path("test4/",views.test4,name="test4"),
    path("test5/",views.test5,name="test5"),
    path("test6/",views.test6,name="test6"),
    path("ocr_result/",views.ocr_result,name="ocr_result"),
    path("qr/",views.qr,name="qr"),
    path("save/",views.save,name="save"),
    path('farm_app/history_audio/',views.history_audio,name="history_audio"),
    path("history_text/",views.history_text,name="history_text"),
    path("qr_url/",views.qr_url,name="qr_url"),
    path("fertilizer_images/",views.fertilizer_images,name="fertilizer_images"),
    #path('farm_app/profile/',views.profile,name="profile"),
    path('diary/',views.diary,name="diary"),
    path('farm_app/diary_view/',views.diary_view,name="diary_view"),
    url(r'^ajaxproject/$', views.ajaxproject, name='ajaxproject'),
]


