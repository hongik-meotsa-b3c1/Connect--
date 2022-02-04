from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import resolve_url

# Create your models here.
class User(AbstractUser):
    #아이디 암호 이메일 이름
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%y/%m", 
    help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요")
    #classnet_id = models.CharField(max_length=150)
    #classnet_pw = models.CharField(max_length=150)
    # 수정수정수정


    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)

