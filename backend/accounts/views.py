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


    










