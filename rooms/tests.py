from rest_framework.test import APITestCase


class TestAemenities(APITestCase):

    # test_로 시작하지 않으면 장고는 test코드를 실행하지 않음
    def test_two_plus_two(self):
        self.assertEqual(2 + 2, 5, "The math is wrong")
