장고에서 커스텀 ViewSet을 만드는 방법은 다음과 같습니다. Django Rest Framework(DRF)를 사용할 때, ViewSet은 API의 동작을 정의하는 중요한 구성 요소입니다.

### 1. ViewSet 생성

먼저, 필요한 모듈을 가져오고 기본적인 ViewSet을 생성합니다.

```python
from rest_framework import viewsets
from .models import YourModel
from .serializers import YourModelSerializer


class YourModelViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = YourModel.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = YourModel.objects.all()
        your_model = get_object_or_404(queryset, pk=pk)
        serializer = YourModelSerializer(your_model)
        return Response(serializer.data)
```

### 2. URL 설정

다음으로, ViewSet을 URL에 연결합니다. `urls.py` 파일에 다음 코드를 추가합니다.

```python
from django.urls import path
from .views import YourModelViewSet

urlpatterns = [
    path('yourmodel/', YourModelViewSet.as_view({'get': 'list'}), name='yourmodel-list'),
    path('yourmodel/<int:pk>/', YourModelViewSet.as_view({'get': 'retrieve'}), name='yourmodel-detail'),
]
```

### 3. 추가적인 메서드 구현

필요에 따라 `create`, `update`, `destroy` 메서드도 추가할 수 있습니다.

```python
def create(self, request):
    serializer = YourModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update(self, request, pk=None):
    your_model = get_object_or_404(YourModel, pk=pk)
    serializer = YourModelSerializer(your_model, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def destroy(self, request, pk=None):
    your_model = get_object_or_404(YourModel, pk=pk)
    your_model.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

이렇게 하면 커스텀 ViewSet이 생성됩니다. 필요한 추가 기능이나 비즈니스 로직에 따라 메서드를 수정하거나 추가할 수 있습니다.

### 추가적인 메소드 구현

추가적인 메소드는 커스텀 ViewSet 클래스 내에 구현합니다. 기본적인 `list`와 `retrieve` 메서드와 함께 같은 클래스 안에 `create`, `update`, `destroy` 메서드를 추가하면
됩니다.

아래는 전체 예시입니다:

```python
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import YourModel
from .serializers import YourModelSerializer


class YourModelViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = YourModel.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = YourModel.objects.all()
        your_model = get_object_or_404(queryset, pk=pk)
        serializer = YourModelSerializer(your_model)
        return Response(serializer.data)

    def create(self, request):
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        your_model = get_object_or_404(YourModel, pk=pk)
        serializer = YourModelSerializer(your_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        your_model = get_object_or_404(YourModel, pk=pk)
        your_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

이렇게 모든 메서드가 같은 클래스 안에 포함되어 있습니다. 각 메서드는 HTTP 요청에 따라 적절한 동작을 수행합니다. 필요에 따라 더 많은 메서드를 추가하거나 수정할 수 있습니다.

### url에 붙어 있는 name

`name='yourmodel-list'`는 URL 패턴에 대한 이름을 지정하는 것입니다. 이 이름은 Django에서 URL을 참조할 때 사용됩니다. 예를 들어, 템플릿이나 뷰에서 이 URL에 대해 역참조를 할 때
유용합니다.

예를 들어, `reverse` 함수를 사용하거나 `redirect`를 호출할 때 이 이름을 사용할 수 있습니다. 이렇게 하면 URL의 실제 경로가 변경되더라도 코드의 다른 부분에서 URL을 쉽게 참조하고 수정할 수
있습니다.

```python
from django.urls import reverse

# URL을 참조하는 예시
url = reverse('yourmodel-list')
```

이런 방식으로 URL 이름을 사용하는 것은 코드의 유지보수성을 높이고, 가독성을 향상시키는 데 도움이 됩니다.

### name은 안써도 되는지?

`name='yourmodel-list'`는 URL 패턴에 대한 이름을 지정하는 것입니다. 이 이름은 Django에서 URL을 참조할 때 사용됩니다. 예를 들어, 템플릿이나 뷰에서 이 URL에 대해 역참조를 할 때
유용합니다.

예를 들어, `reverse` 함수를 사용하거나 `redirect`를 호출할 때 이 이름을 사용할 수 있습니다. 이렇게 하면 URL의 실제 경로가 변경되더라도 코드의 다른 부분에서 URL을 쉽게 참조하고 수정할 수
있습니다.

```python
from django.urls import reverse

# URL을 참조하는 예시
url = reverse('yourmodel-list')
```

이런 방식으로 URL 이름을 사용하는 것은 코드의 유지보수성을 높이고, 가독성을 향상시키는 데 도움이 됩니다.