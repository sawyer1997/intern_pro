from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .constants import END_TIME_STAMP, API_ENDPOINT, SENDER_MAIL_ID
from .models import Candidate
from django.core.mail import send_mail

import logging
from datetime import datetime

logger = logging.getLogger(__name__)


@api_view(['POST'])
def register(request):
    try:
        if request.method == 'POST':
            return Response({'message': "Congrats! You're registered!"}, status=status.HTTP_200_OK)
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            phone = request.data.get('phone')
            is_referred_by = request.data.get('is_referred_by', False)
            referral_id = None
            if is_referred_by:
                referral_id = request.data.get('referral_id')
            current_timestamp = datetime.timestamp(datetime.now())
            if current_timestamp > END_TIME_STAMP:
                return Response({'message': 'Contest is Over!! No registration possible'},
                                status=status.HTTP_403_FORBIDDEN)
            user_already_exists = Candidate.objects.filter(email=email).exists()
            if user_already_exists:
                return Response({'message': "You're already registered!! with email id: {}"
                                .format(email)}, status=status.HTTP_403_FORBIDDEN)
            if first_name and last_name and email and phone:
                candidate = Candidate(first_name=first_name, last_name=last_name,
                                      email=email, phone=phone)
                candidate.save()
                if is_referred_by:
                    candidate.update_referred_id(referral_id)
                    referrer = Candidate.objects.get(id=referral_id)
                    referrer.update_referral_count()
                referral_link = '{}/{}'.format(API_ENDPOINT, candidate.id)
                send_mail('Registered for competition', 'Congrats! You are successfully registered for the '
                                                        'competition.You can share this referral link with your '
                                                        'friends on facebook/twitter with the link: {}'.format(
                    referral_link),
                          SENDER_MAIL_ID, [email])
                return Response({'message': "Congrats! You're registered!"}, status=status.HTTP_200_OK)
            else:
                logger.error('Data is :{}'.format(request.method))
                return Response({'message': 'Please fill all the details !'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.error('Wrong request method!! {}'.format(request.method))
            return Response({'message': 'Bad'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        raise Exception('Something went wrong!!')
