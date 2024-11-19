from rest_framework.test import APITestCase
from . import models
from .serializers import AmenitySerializer
from users.models import User


class TestAemenities(APITestCase):
    NAME = "Amenity Test"
    DESC = "Amenity DESC"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self) -> None:
        # 테스트를 싱핼하기 전에 수행하는 코드
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    # test_로 시작하지 않으면 장고는 test코드를 실행하지 않음
    def test_all_amenities(self):
        response = self.client.get(self.URL)  # 자기 자신한테 request 쏨
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

    def test_create_amenity(self):

        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity desc."
        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_description,
            },
        )

        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_description,
        )

        response = self.client.post(self.URL)

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)  # key 값 있는지 확인하는것

        print(response.json())


class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESC = "Test Dsc"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")

        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):

        response = self.client.get("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESC)

    def test_put_amenity(self):
        # given
        amenity = models.Amenity.objects.get(name=self.NAME, description=self.DESC)
        find_data = AmenitySerializer(amenity).data
        updated_name = "Updated Name"
        find_data["name"] = updated_name

        # when
        response = self.client.put("/api/v1/rooms/amenities/1", find_data)

        # then
        updated_data = response.json()
        self.assertEqual(updated_data["name"], updated_name)

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 204)


class TestRooms(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username="nico",
        )
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")
        self.assertEqual(response.status_code, 403)
        # 테스트할때는 관리자 계정도 없음, 넣어줘야함

        self.client.force_login(
            self.user,
        )
        # self.client.login(
        #     username="nico",
        #     password="123",
        # )
        response = self.client.post("/api/v1/rooms/")
        print(response.json())
