Django REST Framework에서 `ModelSerializer`가 아닌 일반 `Serializer`를 사용할 때, 특정 필드를 **읽기 전용**으로 설정하려면 `read_only` 매개변수를 사용하여 필드
정의를 명시적으로 설정할 수 있습니다. 일반적으로 아래와 같이 할 수 있습니다.

### 예시

여기서는 `CategorySerializer`를 일반 `Serializer`로 변환하고, `created_at` 필드를 읽기 전용으로 설정하는 예를 보여줍니다.

```python
from rest_framework import serializers
from .models import Category  # Category 모델 import


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # 읽기 전용
    name = serializers.CharField()  # 쓰기 가능
    kind = serializers.CharField()  # 쓰기 가능
    created_at = serializers.DateTimeField(read_only=True)  # 읽기 전용

    # 필요에 따라 추가 필드를 정의
```

### 필드 설명

- **`read_only=True`**:
    - 이 속성이 설정된 필드는 클라이언트로부터 요청을 받을 때는 무시되고, 오직 응답할 때만 포함됩니다. 즉, 클라이언트가 이 필드에 값을 제공할 수 없게 됩니다.

- **나머지 필드**:
    - 나머지 필드는 기본적으로 읽기/쓰기가 가능하도록 설정되어 있으며, 필요에 따라 `required=True` 또는 `allow_blank=True`와 같은 추가 옵션을 지정할 수 있습니다.

### 전체적인 구조

이제 `CategorySerializer`를 사용하여 생성, 업데이트, 조회 등을 수행할 수 있습니다. 예를 들어, `created_at` 필드는 데이터베이스에 의해 자동으로 설정되며, 클라이언트는 이 값을 설정할
필요가 없고, 읽기 전용으로 제공됩니다.

이 방식으로 일반 `Serializer`를 사용할 때도 읽기 전용 필드를 쉽게 설정할 수 있습니다.


---
Django REST Framework의 `ModelSerializer`를 사용할 때 특정 필드를 읽기 전용(read-only)으로 지정하려면, `Meta` 클래스 내에 `read_only_fields` 속성을
정의하면 됩니다. 이렇게 하면 해당 필드가 클라이언트 요청에서는 무시되고, 오직 응답 시에만 포함됩니다.

### 예시

아래는 `CategorySerializer`에서 `created_at` 필드를 읽기 전용으로 설정하는 방법입니다:

```python
from rest_framework import serializers
from .models import Category  # Category 모델 import


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"  # 모든 필드 포함
        read_only_fields = ("created_at",)  # 읽기 전용으로 설정할 필드
```

### 설명

- **`fields`**:
    - `"__all__"`을 사용하면 모델의 모든 필드를 포함할 수 있습니다. 특정 필드를 제외하고 싶다면, `fields`를 명시적으로 나열할 수 있습니다.

- **`read_only_fields`**:
    - 이 튜플에 포함된 필드는 클라이언트가 요청할 때는 전혀 사용되지 않으며, 데이터베이스에 의해 자동으로 설정되는 값이나 시스템에서 생성된 값에 적합합니다.
    - 위 예시에서는 `created_at` 필드를 읽기 전용으로 설정하여 클라이언트가 이 값을 업데이트하거나 생성할 수 없도록 합니다.

### 추가 예시

필드에 대한 더욱 세부적인 설정을 하고 싶다면, 아래와 같이 개별 필드를 지정할 수도 있습니다:

```python
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "kind", "created_at")  # 명시적으로 필드 선택
        read_only_fields = ("id", "created_at")  # 읽기 전용 필드
```

이렇게 하면 `id`와 `created_at` 필드는 클라이언트의 요청에 대해 읽기 전용으로 작동합니다. `name`과 `kind` 필드는 여전히 클라이언트가 수정할 수 있는 필드로 남아 있게 됩니다.