from decouple import config

TOKEN = config('TOKEN', cast=str)
DB_NAME = config('DB_NAME', cast=str)
DB_USER = config('DB_USER', cast=str)
DB_PASSWORD = config('DB_PASSWORD', cast=str)
DB_HOST = config('DB_HOST', cast=str)
DB_PORT = config('DB_PORT', cast=int)

ADMIN_PASSWORD = config('ADMIN_PASSWORD', cast=str)

POSTGRES_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
