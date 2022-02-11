from django.forms import ValidationError
from django.http import Http404
from rest_framework import serializers
from django.contrib.auth import get_user_model
import requests
from .models import Classnet

User = get_user_model()

def signin_with_hongik(user_id, user_pw):
    res = requests.post(
        'https://ap.hongik.ac.kr/login/LoginExec3.php',
        data={'USER_ID': user_id, 'PASSWD': user_pw}
    )
    res.raise_for_status()
    return False if res.text.find('SetCookie') == -1 else True


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        qs = Classnet.objects.all()
        qs.delete()
        
        user = User.objects.create(
            username=validated_data["username"],
            nickname=validated_data["nickname"],
            email = validated_data["email"],
            classnetId=validated_data["classnetId"]
        )   
   
        user.set_password(validated_data["password"])
        user.save()

        return user

      

    class Meta:
        model = User
        fields = ['pk', 'username', 'password', 'nickname', 'email', 'classnetId']


class ClassnetSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        qs = Classnet.objects.all()
        qs.delete()
        classnet_id = validated_data["classnetid"]
        classnet_pw = validated_data["classnetpw"]

        classnet_ok = signin_with_hongik(classnet_id, classnet_pw)
        
        if classnet_ok == True:
            Classnet.objects.create(
             classnet = classnet_ok,  
             classnetid = classnet_id,
            )
            return True

        else:
            raise Http404
       

    class Meta:
        model = Classnet
        fields = ['classnet', 'classnetid', 'classnetpw']


     



        




   
        
        
        

 