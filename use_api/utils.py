from rest_framework import status


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'status': status.HTTP_200_OK,
        'uid': user.id,
        'username': user.username,
        'token': token
    }