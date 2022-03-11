from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from datetime import datetime
from dateutil.relativedelta import relativedelta

User = get_user_model()

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        try:
            data = request.data
            name = data['name']
            email = data['email'].lower()
            password = data['password']
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(
                    name=name, email=email, password=password
                )

                return Response(
                    {'success': 'ユーザ登録に成功しました'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'error': '登録済みのメールアドレスです'},
                    status=status.HTTP_400_BAD_REQUEST
                )                
        except:
            return Response(
                {'error': 'アカウント登録時に問題が発生しました'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserView(APIView):
    def get(self, request):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
      
        except:
            return Response(
                {'error': 'ユーザの取得に問題が発生しました'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class SubscriptionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data = request.data
            email = data['email']
            customer_id = data['customer_id']
            dt = datetime.today()  
            user_data = User.objects.filter(
                customer_id=customer_id
            )
            if len(user_data):
                user_data = user_data[0]
            else:
                user_data = User.objects.get(email=email)
                user_data.customer_id = customer_id
            user_data.current_period_end = dt + relativedelta(months=1)
            user_data.save()

            return Response(
                {'success': 'サブスク有効期限の更新に成功しました'},
                status=status.HTTP_200_OK
            )
           
        except Exception as e:
            print("error is {}".format(e))

            return Response(
                {'error': 'サブスク有効期限の更新に失敗しました。'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )