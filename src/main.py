import os
from dotenv import load_dotenv
from api_call.get_request import Make_Get_Request

load_dotenv()

MISTAL_API = os.getenv('MISTRAL_API_KEY') 

if not MISTAL_API:
    raise ValueError('Mistral apikey is missing')

obj = Make_Get_Request(MISTAL_API)
print('executing api')
response = obj.test_connection()
print('res is ',response)

print('Welcome to Quasi Agent')
input_is = input('what do you want to ask ?')
greet_user = obj.greeting_user(input_is)
#print(greet_user) 