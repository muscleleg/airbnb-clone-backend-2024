from rest_framework.test import APITestCase
from . import models


class TestAemenities(APITestCase):
    NAME = "Amenity Test"
    DESC = "Aemnity DESC"

    def setUp(self) -> None:
        # 테스트를 싱핼하기 전에 수행하는 코드
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    # test_로 시작하지 않으면 장고는 test코드를 실행하지 않음
    def test_all_amenities(self):

        response = self.client.get(
            "/api/v1/rooms/amenities/"
        )  # 자기 자신한테 request 쏨
        data = (
            response.json()
        )  # 출력해도 빈배열만 나옴, 왜냐하면 장고는 test를 위한 db를 따로 사용함, test에만 사용하고 이후에 없애는 데이터베이스임

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200",
        )
        print(data)  # 빈배열도 list이기때문에 테스트 가능

        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )
        # self.assertIsInstance(data, str)
