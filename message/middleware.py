# This file is for  custome middleware for websocket authentication uaing JWT tocken.


import jwt
from django.conf import settings
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from account.models import User
from urllib.parse import parse_qs
from asgiref.sync import sync_to_async

@sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except:
        return AnonymousUser()

class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):

        query_string = parse_qs(scope["query_string"].decode())

        token = query_string.get("token")
        if token:
            token = token[0]

            try:
                decoded_data = jwt.decode(
                    token, settings.SECRET_KEY, algorithms=["HS256"]
                )
                user = await get_user(decoded_data["user_id"])
                scope["user"] = user
            except:
                scope["user"] = AnonymousUser()
        else:
            scope["user"] = AnonymousUser()

        return await super().__call__(scope, receive, send)