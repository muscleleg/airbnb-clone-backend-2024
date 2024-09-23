from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category
from .serializer import CategorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT


class Categories(APIView):
    ## class안에 있는 모든 메소든는 첫번째가 self라는 것을 잊지말자
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(
            all_categories, many=True
        )  # many=True는 카테코리가 배열이라고 알려주는 것임
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)


"""@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(
            all_categories, many=True
        )  # many=True는 카테코리가 배열이라고 알려주는 것임
        return Response(serializer.data)
    elif request.method == "POST":
        # json형태로 안보내면 실패함
        # print(request.data)

        # 아래와 같이 생성을 할 수는 있으나 Valdiation이 안되었기 때문에 오류가 발생할 수 있어 좋지 않음
        # Category.objects.create(
        #     name=request.data["name"],
        #     kind=request.data["kind"],
        # )

        # serializer로 validation을 해줄 수 있음
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)"""


class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound  # raise는 에러를 일으키는 키워드임, 자바 throw랑 같은듯
        return category

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        # pk를 통해서 찾은 category의 데이터를 request로 받은 data로 변경
        serializer = CategorySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        # partial=True를 지정하면 request에 모델 키의 일부만 있어도 됨
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
            # serializer에 pk를 통해 찾은 category와 request를 통해 받은 data가 있을 경우에는 craete가 아니라 save가 동작함
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


"""@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound  # raise는 에러를 일으키는 키워드임, 자바 throw랑 같은듯

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        # pk를 통해서 찾은 category의 데이터를 request로 받은 data로 변경
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,
        )
        # partial=True를 지정하면 request에 모델 키의 일부만 있어도 됨
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
            # serializer에 pk를 통해 찾은 category와 request를 통해 받은 data가 있을 경우에는 craete가 아니라 save가 동작함
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)"""
