## create DB tables from model 
## install Mysql workbanch and xammp 
##create database in MysqlBanch
## from setting.py change this command to connect with mysql 
  ''' 
      DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'name_of_DB_created',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        }
    }
  '''
##insert tables we desgined in DB digram 
##in postman request  
''' http://127.0.0.1:8000/api/token/ '''
#user_name and password 
'''
{
    
    "user_name": "admin",
    "password": "admin1234"
   
}
'''

#result 
'''
{
  "token": "3c62935126920127ae32f80bae7cd606b31ed7e9"
  }
'''

##in postman request  
''' http://127.0.0.1:8000/api/jwt/token/ '''
#user_name and password 
'''
{
    
    "user_name": "admin",
    "password": "admin1234"
   
}
'''

#result 
'''
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MzM3MzQ1MiwiaWF0IjoxNjczMjg3MDUyLCJqdGkiOiJjOTA4MzRhMmMxZDk0Yzk3YTlmZDA0N2E5MDYzYjkxMSIsInVzZXJfaWQiOjN9.2oQSZjnDshVQsNX8rdnfnsJeJJq2KM_ieRtIhIWUht0",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczMjg3MzUyLCJpYXQiOjE2NzMyODcwNTIsImp0aSI6ImNkMmMxMjE2MjRkYTQ4YzZhZmJlZDFjYjljZDk0OTg1IiwidXNlcl9pZCI6M30.gerWn2wct88CJqtW18S_oqK5xqXph-_5Ss3IjBKMJak"
'''


##in postman request  
'''http://127.0.0.1:8000/api/jwt/token/refresh/ '''
#for refresh
'''
{
    
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MzM3MDkzNiwiaWF0IjoxNjczMjg0NTM2LCJqdGkiOiJkNjVlNGYyODU0ZGI0ZDQ4YTgxZmJiZGYyMmI5YTVlNCIsInVzZXJfaWQiOjN9.ffaG9JER9IH90nCZH1_YHnZNT2aOO1PrXxcJE3kMdv8"
   
}
'''

#result 
'''
"{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczMjg3NDQ4LCJpYXQiOjE2NzMyODQ1MzYsImp0aSI6IjI4M2RlNmRjMzNhNzQ5MTU4MWQyMTcxMWQ2MzM2MDc1IiwidXNlcl9pZCI6M30.SlN5FunG9g8fx-k-4LwJ0-u8ZopLbnfsLYDbMDV8X0w"
}
'''





