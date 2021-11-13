from django.contrib import admin
from .models import Comments, Crops, Deeplearnings, Dronerunnings, Farmdiaries, Pestinfos, Ptcinfos, Users, Images
from .models import History
from .models import Images, DeepImages,OcrRsult,Audio,privent
# Register your models here.

admin.site.register(Comments)
admin.site.register(Crops)
admin.site.register(Deeplearnings)
admin.site.register(Dronerunnings)
admin.site.register(Farmdiaries)
admin.site.register(Pestinfos)
admin.site.register(Ptcinfos)
admin.site.register(Users)
admin.site.register(Images)
admin.site.register(DeepImages)
admin.site.register(History)
admin.site.register(OcrRsult)
admin.site.register(Audio)
admin.site.register(privent)
