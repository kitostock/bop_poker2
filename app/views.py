from datetime import datetime

from accounts.serializers import UserSerializer
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.db.models.functions import TruncDate, TruncMonth
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BopInfo

User = get_user_model()

class BopInfoRegisterView(APIView):

    def post(self, request):
        try:
            data = request.data
            user_id = data['user_id']
            category_id = data['category_id']
            rate_id = data['rate_id']
            buy_in = data['buy_in']
            cash_out = data['cash_out']
            number_of_hands = data['number_of_hands']
            memo = data['memo']
            register_date = data['register_date']

            dt = datetime.today()  
            print('dt is type {}'.format(type(dt)))
            print('register_date is type {}'.format(type(register_date)))
            register_date = datetime.strptime(register_date, '%Y-%m-%d %H:%M:%S')
            print('register_date is type {}'.format(type(register_date)))
            BopInfo.objects.create(
                user_id = user_id,
                category_id = category_id,
                rate_id = rate_id,
                buy_in = buy_in,
                cash_out = cash_out,
                number_of_hands = number_of_hands,
                register_date = register_date,
                memo = memo,
                created_date = dt,
                updated_date = dt
            )

            return Response(
                {'success': '収支情報登録に成功しました'},
                status=status.HTTP_201_CREATED
            )
         
        except Exception as e:
            print('error is {}'.format(e))
            return Response(
                {'error': '収支情報登録時に問題が発生しました'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BopInfoFindView(APIView):
    """
    ログインユーザの月ごとの集計結果を返却
    - カテゴリ別
    """

    def get(self, request):
        try:
            user = request.user
            user = UserSerializer(user)
            user_id = user.data.get('id')

            print('user_id is {}'.format(user_id))
            # bop_infos = BopInfo.objects.filter(
            #     user_id = user_id
            # )
            monthly_infos = BopInfo.objects.filter(
                user_id = user_id
            ).annotate(
                monthly_date=TruncMonth("register_date")).values("monthly_date"
            ).annotate(
                total=Sum("cash_out") - Sum("buy_in"),
                total_buy_in=Sum("buy_in"),
                total_cash_out=Sum("cash_out"),
                total_hand=Sum("number_of_hands")
            ).values(
                "monthly_date","total","total_buy_in", "total_cash_out", "total_hand", "category_id", "rate_id"
            ).order_by("-monthly_date")

            return Response(
                {
                    'monthly_infos' : monthly_infos
                },
                status=status.HTTP_200_OK
            )
         
        except Exception as e:
            print('error is {}'.format(e))
            return Response(
                {'error': '収支情報取得時に問題が発生しました'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class BopInfoFindDateView(APIView):
    """
    ログインユーザの月内日ごとの集計結果を返却
    - カテゴリ別
    """

    def get(self, request):
        try:
            user = request.user
            user = UserSerializer(user)
            user_id = user.data.get('id')
            data = request.data
            # month = data['month']

            print('user_id is {}'.format(user_id))
            # print('month is {}'.format(month))
            divide_date_category_rate_infos = BopInfo.objects.filter(
                user_id = user_id
            ).annotate(
                trunc_date=TruncDate("register_date")).values("trunc_date"
            ).annotate(
                total=Sum("cash_out") - Sum("buy_in"),
                total_buy_in=Sum("buy_in"),
                total_cash_out=Sum("cash_out"),
                total_hand=Sum("number_of_hands")
            ).values(
                "trunc_date","total","total_buy_in", "total_cash_out", "total_hand", "category_id", "rate_id"
            ).order_by("-trunc_date")

            date_infos = BopInfo.objects.filter(
                user_id = user_id
            ).annotate(
                trunc_date=TruncDate("register_date")).values("trunc_date"
            ).annotate(
                total=Sum("cash_out") - Sum("buy_in"),
                total_buy_in=Sum("buy_in"),
                total_cash_out=Sum("cash_out"),
                total_hand=Sum("number_of_hands")
            ).values(
                "trunc_date","total","total_buy_in", "total_cash_out", "total_hand"
            ).order_by("-trunc_date")

            return Response(
                {
                    'date_infos': date_infos,
                    'divide_date_category_rate_infos' : divide_date_category_rate_infos
                },
                status=status.HTTP_200_OK
            )
         
        except Exception as e:
            print('error is {}'.format(e))
            return Response(
                {'error': '収支情報取得時に問題が発生しました'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

