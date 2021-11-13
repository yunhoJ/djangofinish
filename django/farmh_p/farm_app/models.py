from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

# 일지작성페이지 텍스트 저장
#text필드 내용/ input태그 식별 name = text
#diary.html에 있는 td변수명info 확인해서 바꿔주기(text부분)
#class Post(models.Model):
#    title = models.CharField(max_length=50)
#    text = models.TextField()

#    def __str__(self):
#        return self.text


class Comments(models.Model):
    comment_seq = models.AutoField(db_column='COMMENT_SEQ', primary_key=True)  # Field name made lowercase.
    p_num = models.ForeignKey('Pestinfos', models.DO_NOTHING, db_column='P_NUM')  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comments'


class Crops(models.Model):
    f_num = models.AutoField(db_column='F_NUM', primary_key=True)  # Field name made lowercase.
    f_name = models.CharField(db_column='F_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f_area = models.FloatField(db_column='F_AREA', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crops'


class Deeplearnings(models.Model):
    d_num = models.AutoField(db_column='D_NUM', primary_key=True)  # Field name made lowercase.
    p_num = models.ForeignKey('Pestinfos', models.DO_NOTHING, db_column='P_NUM')  # Field name made lowercase.
    d_comment = models.CharField(db_column='D_COMMENT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    d_check = models.CharField(db_column='D_CHECK', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d_date = models.DateTimeField(db_column='D_DATE', blank=True, null=True)  # Field name made lowercase.
    d_img1 = models.CharField(db_column='D_IMG1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    d_img2 = models.CharField(db_column='D_IMG2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    d_img3 = models.CharField(db_column='D_IMG3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'deeplearnings'

class Dronerunnings(models.Model):
    dr_num = models.AutoField(db_column='DR_NUM', primary_key=True)  # Field name made lowercase.
    dr_date = models.DateTimeField(db_column='DR_DATE', blank=True, null=True)  # Field name made lowercase.
    ptc_name = models.CharField(db_column='PTC_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dr_company = models.CharField(db_column='DR_COMPANY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dr_phone = models.CharField(db_column='DR_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    p_num = models.ForeignKey('Pestinfos', models.DO_NOTHING, db_column='P_NUM')  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dronerunnings'


class Farmdiaries(models.Model):
    r_num = models.AutoField(db_column='R_NUM', primary_key=True)  # Field name made lowercase.
    r_plant = models.CharField(db_column='R_PLANT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_bug = models.CharField(db_column='R_BUG', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_ftz = models.CharField(db_column='R_FTZ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_low_c = models.FloatField(db_column='R_LOW_C', blank=True, null=True)  # Field name made lowercase.
    r_ptc = models.ForeignKey('Ptcinfos', models.DO_NOTHING, db_column='R_PTC', blank=True, null=True)  # Field name made lowercase.
    r_weather = models.CharField(db_column='R_WEATHER', max_length=200, blank=True, null=True)  # Field name made lowercase.
    r_date = models.DateTimeField(db_column='R_DATE', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    r_diary = models.CharField(db_column='R_DIARY', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    r_pic1 = models.CharField(db_column='R_PIC1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    r_hum = models.FloatField(db_column='R_HUM', blank=True, null=True)  # Field name made lowercase.
    r_high_c = models.FloatField(db_column='R_HIGH_C', blank=True, null=True)  # Field name made lowercase.
    r_dr_num = models.ForeignKey(Dronerunnings, models.DO_NOTHING, db_column='R_DR_NUM', blank=True, null=True)  # Field name made lowercase.
    r_ptc_name = models.CharField(db_column='R_PTC_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase. 
    r_dr_memo = models.CharField(db_column='R_DR_MEMO', max_length=2000, blank=True, null=True)  # Field name made lowercase. 
    

    class Meta:
        managed = False
        db_table = 'farmdiaries'


class Pestinfos(models.Model):
    p_num = models.AutoField(db_column='P_NUM', primary_key=True)  # Field name made lowercase.
    p_bug = models.CharField(db_column='P_BUG', max_length=100, blank=True, null=True)  # Field name made lowercase.
    p_method = models.CharField(db_column='P_METHOD', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    p_symtom = models.CharField(db_column='P_SYMTOM', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    p_ptc = models.ForeignKey('Ptcinfos', models.DO_NOTHING, db_column='P_PTC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pestinfos'


class Ptcinfos(models.Model):
    ptc_num = models.AutoField(db_column='PTC_NUM', primary_key=True)  # Field name made lowercase.
    ptc_name = models.CharField(db_column='PTC_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ptc_maker = models.CharField(db_column='PTC_MAKER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ptc_use = models.CharField(db_column='PTC_USE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ptc_quantity = models.FloatField(db_column='PTC_QUANTITY', blank=True, null=True)  # Field name made lowercase.
    ptc_pest = models.CharField(db_column='PTC_PEST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ptc_plant = models.CharField(db_column='PTC_PLANT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ptcimg=models.ImageField(null=True,upload_to='ptcimage/',blank=True)
    #ptc_pic1 = models.CharField(db_column='PTC_PIC1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    #ptc_pic2 = models.CharField(db_column='PTC_PIC2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    #user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ptcinfos'


class Users(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    user_pwd = models.CharField(db_column='USER_PWD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_phone = models.CharField(db_column='USER_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_addr = models.CharField(db_column='USER_ADDR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    join_date = models.DateTimeField(db_column='JOIN_DATE', blank=True, null=True)  # Field name made lowercase.
    admin_yn = models.CharField(db_column='ADMIN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

class Images(models.Model):
  
    images = models.ImageField(null=True,upload_to='images/',blank=True)
    class Meta:
        managed = False
        db_table = 'farm_app_images'

class DeepImages(models.Model):
  
    deepimages = models.ImageField(null=True,upload_to='images/',blank=True)
    class Meta:
        managed = False
        db_table = 'farm_app_deepimages'


#농약사진저장띄우기
class History(models.Model):

    history=models.ImageField(null=True,upload_to='historyimg/',blank=True)
    class Meta:
        managed = False
        db_table = 'farm_app_history'


        
class Audio(models.Model):
    audio=models.FileField(upload_to='audio/',null=True,blank=True)
#class Profile(models.Model):

#    profile = models.p

# class PtcImages(models.Model):
#     p_ptc = models.ForeignKey('Ptcinfos', models.DO_NOTHING, db_column='P_PTC', blank=True, null=True)
#     ptcimage=models.ImageField(null=True,upload_to='ptcimage/',blank=True)

class OcrRsult(models.Model):
    ocrresult = models.ImageField(null=True,upload_to='ocrResult/',blank=True)
    

class privent(models.Model):
    pr_bug = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase. 
    pr_text = models.CharField(max_length=2000, blank=True, null=True)  # Field name made lowercase. 