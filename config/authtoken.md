rest_framework.authtoken을 INSTALLED_APPS에 추가한 후 python manage.py migrate만 실행해도 되는 이유는 Django가 기본적으로
rest_framework.authtoken 앱에 필요한 마이그레이션 파일을 이미 제공하기 때문입니다.

makemigrations 명령은 새로 정의된 모델이나 기존 모델의 변경 사항을 반영하여 마이그레이션 파일을 생성할 때 사용하는데, rest_framework.authtoken 앱은 이미 준비된 마이그레이션 파일을
포함하고 있으므로 별도로 makemigrations을 실행할 필요가 없습니다.

따라서, python manage.py migrate만 실행하면 Django가 해당 앱에 대한 마이그레이션 파일을 인식하고 데이터베이스에 필요한 테이블을 자동으로 생성하게 됩니다.