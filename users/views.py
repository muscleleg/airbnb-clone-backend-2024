from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import User
from django.conf import settings
import jwt


class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)

            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            # 생성할때 ModelSerializer가 unique를 지켜줌, unique해야하는 값과 동일하게 저장하려고 시도하면 막줌아줌
            # User가 상속받고 있는 AbstractUser를 보면 username은 unique가 true임
            user = serializer.save()
            # user객체안에 set_password가 있고 이놈이 password를 해쉬화해줌 따라서 객체를 쓰기 위해 저장을 해야함(객체가 있어야 내부 메소드를 쓰던가 하니까)
            # 이걸로 유저를 만들어도 관리자패널에는 접근못함, 관리자 패널 접근 계정은 일반 유저s가 아님, 관리자 패널에서 스태프권한과, 최상위 사용자 권한을 모두 주면 관리자 패널 사용가능
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# {
# "username":"password-test",
# "email": "password@gmail.com",
# "name": "니콜라스",
# "gender": "male",
# "language": "kr",
# "currency": "won",
# "password":"12345"
# }


# code-challenge: 특정 유저의 모들 리뷰나오게 하기
class PublicUser(APIView):

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)


class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):

        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome!"})
        else:
            return Response({"error": "wrong password"})


class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "bye!"})


class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",
            )  # 정보, secret(서명), 알고리즘
            return Response({"token": token})
        else:
            return Response({"error": "wrong password"})
