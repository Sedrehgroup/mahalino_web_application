from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.contrib.auth.models import User
import json
from rest_framework.permissions import AllowAny, IsAuthenticated
from .sql import PostConn
from rest_framework_simplejwt.backends import TokenBackend
from .models import Order, Park, Bohran
import random
from django.contrib.gis.geos import Point
import jwt
from django.conf import settings
import ast
from django.core.serializers import serialize
import os


headers = {'Content-Type': 'application/json',
         'Access-Control-Allow-Origin': os.environ.get('ALLOW_ORIGIN'),
         'Access-Control-Allow-Credentials': True,
         'Access-Control-Allow-Methods': 'OPTIONS',
         'Access-Control-Allow-Headers': ['Origin', 'Content-Type', 'Accept']}


def user_return(request):
    try:
        # take jwt token from request
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]

        # take user from jwt token
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(id=payload['user_id'])
    except:
        return None

    return user


class PerTrans(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        # user = user_return(request)
        # if not bool(user):
        #     return Response(status=status.HTTP_401_UNAUTHORIZED, headers=headers)

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        if str(lat) is None or str(lon) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, headers=headers)

        lat = float(lat)
        lon = float(lon)

        data = PostConn(lat, lon).pertrans()
        return Response(data=data, status=status.HTTP_200_OK, headers=headers)


class PubTrans(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        # user = user_return(request)
        # if not bool(user):
        #     return Response(status=status.HTTP_401_UNAUTHORIZED, headers=headers)

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        if lat is None or lon is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, headers=headers)

        lat = float(lat)
        lon = float(lon)

        data = PostConn(lat, lon).pubtrans()
        return Response(data=data , status=status.HTTP_200_OK, headers=headers)


class Refahi(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        # user = user_return(request)
        # if not bool(user):
        #     return Response(status=status.HTTP_401_UNAUTHORIZED, headers=headers)

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        if str(lat) is None or str(lon) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, headers=headers)

        lat = float(lat)
        lon = float(lon)

        data = PostConn(lat, lon).refahi()
        return Response(data=data, status=status.HTTP_200_OK, headers=headers)


class Security(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        # user = user_return(request)
        # if not bool(user):
        #     return Response(status=status.HTTP_401_UNAUTHORIZED, headers=headers)

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        if str(lat) is None or str(lon) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, headers=headers)

        lat = float(lat)
        lon = float(lon)
        data = PostConn(lat, lon).security()
        return Response(data=data, status=status.HTTP_200_OK, headers=headers)
