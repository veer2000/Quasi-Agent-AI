import os
from dotenv import load_dotenv
from api_call.get_request import Make_Get_Request

from fastapi import FastAPI, HTTPException

load_dotenv()

MISTAL_API = os.getenv('MISTRAL_API_KEY') 

if not MISTAL_API:
    raise ValueError('Mistral apikey is missing')


app = FastAPI(
    title='Quasi Agentic AI',
    description=' A simple ai chat bot'
)

@app.get('/call_ai/')
def call_ai(usermessage : str):
    try:
        obj = Make_Get_Request(MISTAL_API)
        print('executing api')
        response = obj.test_connection()
        # print('res is ',response)
        print('Welcome to Quasi Agent')
        #input_is = input('what do you want to ask ?')
        greet_user = obj.greeting_user(usermessage)
        yield greet_user
    except Exception as err:
        raise HTTPException(status_code = 500, detail = f'error is {err}')
