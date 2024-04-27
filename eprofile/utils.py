from rest_framework_simplejwt.tokens import AccessToken


def get_user_role(request):
    token = AccessToken(request.META.get("HTTP_AUTHORIZATION")
                        .split(" ")[1])
    return token['role']