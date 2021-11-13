DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'farm_db',  # db 이름
        'USER': 'root',     # 로그인-유저 명
        'PASSWORD': '1234',  # 로그인-비밀번호
        'HOST': '121.147.0.236',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
