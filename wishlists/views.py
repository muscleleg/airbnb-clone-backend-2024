from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wishlists
from .serilalizers import WishlistSerializer


class Wishlists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlists.objects.filter(user=request.user)
        serializer = WishlistSerializer(all_wishlists, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
