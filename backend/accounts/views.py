from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from .serializers import  SignupSerializer,ClassnetSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Classnet
from django.http import Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import requests
import json




class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]


class ClassnetView(ListCreateAPIView):
    model = Classnet
    serializer_class = ClassnetSerializer
    permission_classes = [
        AllowAny,
    ]

    def get(self,request):
        class_auth = Classnet.objects.last()
    
        try:
            serializer = ClassnetSerializer(class_auth)
            return Response(serializer.data)

        except ObjectDoesNotExist:
            return Http404


    
# class ClassnetView(APIView):
#     permission_classes = [AllowAny]

#     def post(self,request):
#         req = json.loads(request.body.decode('utf-8'))
#         classnet_id = req['classnet_id']
#         classnet_pw = req['classnet_pw']
#         classnet_ok = signin_with_hongik(classnet_id,classnet_pw)
#         if classnet_ok==True:










