from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from users.models import User


#BaseAuthentication을 상속 받은 애들은 authenticate를 override해야함
class TrustMeBroAuthentication(BaseAuthentication):

    def authenticate(self, request):
        username = request.headers.get("Trust-Me")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)

            # 튜플(tuple)은 순서가 있는 값의 집합을 나타내는 파이썬의 자료형입니다. 리스트(list)와 비슷하지만, 수정할 수 없는(immutable) 특성을 가지고 있습니다. 즉, 튜플은 한 번 생성된 후에는 그 값을 변경할 수 없습니다.
            return (user, None)
        # 첫 번째 값 (User): 인증된 사용자 객체입니다. 이 객체는 request.user로 사용할 수 있으며, 이후의 뷰에서 인증된 사용자 정보에 접근할 수 있습니다.
        # 두 번째 값 (None): 이는 기본적으로 인증된 사용자의 권한이나 추가 정보를 나타내는 부분입니다. 대부분의 경우 None으로 처리하지만, 권한 시스템을 추가적으로 구현할 경우에는 여기에 권한 정보를 담을 수도 있습니다.
        # return 값으로 user가 나올 때까지 다른 authentication으로 차근차근 넘어감, 이전에는 SessionAuthentication에서 넘어온거임.
        except User.DoesNotExist:
            raise AuthenticationFailed(f'No user {username}')
