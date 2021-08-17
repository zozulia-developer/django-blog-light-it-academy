from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.db import close_old_connections
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs


class TokenAuthMiddleware(BaseMiddleware):
    """
    Custom token auth middleware via JWT
    """

    async def __call__(self, scope, receive, send):
        close_old_connections()

        token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]

        try:
            # This will automatically validate the token and raise an error if
            # token is invalid
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            print(e)
            return None
        else:
            #  Then token is valid, decode it
            decoded_data = jwt_decode(token, settings.SECRET_KEY,
                                      algorithms=["HS256"])
            print(decoded_data)

            user_id = decoded_data["user_id"]
            user = await self.get_user(user_id)

        # Return the inner application directly and let it run everything else
        scope = dict(scope, user=user)
        return await super().__call__(scope, receive, send)

    @database_sync_to_async
    def get_user(self, user_id):
        return get_user_model().objects.get(id=user_id)
