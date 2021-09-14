from .base import *


env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))    #운영체제 내의 경로로 베이스디렉토리랑 .env를 합쳐주는 함수를 경로로 다시 돌려줌

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')     #공백제거용
    start = line.find('=')        #제일 먼저 나오는 인덱스를 알려줌(=을 기준으로 인덱스, 값 구분)
    key = line[:start]            #스타트까지의 값이 키가 되고
    value = line[start+1:]         #스타트+1부터 끝까지를 값으로
    env_list[key] = value

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


#databases관련 공식문서: https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}