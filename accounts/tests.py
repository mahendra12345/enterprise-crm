from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
)


class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(
            {
                "success": True,
                "message": "User registered successfully.",
                "data": UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )



   class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "data": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "user": UserSerializer(user).data,
                },
            },
            status=status.HTTP_200_OK,
        )


    class LogoutAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:

            refresh_token = request.data.get("refresh")

            token = RefreshToken(refresh_token)

            token.blacklist()

            return Response(
                {
                    "success": True,
                    "message": "Logout successful.",
                },
                status=status.HTTP_200_OK,
            )

        except Exception:

            return Response(
                {
                    "success": False,
                    "message": "Invalid refresh token.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


        class ProfileAPIView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



     class ChangePasswordAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = ChangePasswordSerializer

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Password changed successfully.",
            },
            status=status.HTTP_200_OK,
        )


    