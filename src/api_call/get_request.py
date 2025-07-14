import requests
from mistralai import Mistral

#Base_Url = "https://api.mistral.ai/v1"
Base_Url = 'https://api.mistral.ai/v1'


class Make_Get_Request:
    
    conversation_history = []
    
    def __init__(self, MISTAL_API_key):
        self.mistrail_api_key = MISTAL_API_key
        self.mistril_clinet = Mistral(api_key = MISTAL_API_key )
        self.model = "mistral-large-latest"
        self.conversation_history = []
    
    @staticmethod
    def user_instruction():
        instruction = '''
        you are a exceptional prodigy who can help other so provide valid response
Understand the Problem / Define the Problem
Analyze using 3Ws (What, Why, Where) and How and Who	
	What: What exactly is the user asking for? What are the key terms, concepts, or desired outcomes?
	Why: Why is the user asking this question? What is their underlying need or goal?
	Where: Where does this problem occur or apply? What is the context? (e.g., "Is this a problem in a specific programming language, a particular environment, or a general life scenario?")
	How: How does the problem manifest?
	Who: Who is the audience for this question? What is their level of understanding? 
	Diagnose the root cause / How to solve / Technique to use:
Clarify the Problem
Define the Goals / Plan
	Identify and implement a solution: 
	Beginner level and intermediate level answer
Break Down the Problem
Write down a pseudo-code or a flow chart to explain
Divide problem into small sub-problems, and create separate functions
If necessary use class - object of OOPS so that user can understand with real world concepts
Develop Action Plan
Execute Action Plan
	Be clear and concise:
	Provide examples:
	Structure your answer:
Help User to Visualize the Problem
Recheck and Evaluate Response        
        '''
        return instruction
        
    
    def test_connection(self):
        try:
            headers = {
                "Authorization" : f'Bearer {self.mistrail_api_key}',
                'Content-Type' : "application/json",
            }
            
            response = requests.get(f"{Base_Url}/models", headers=headers)
            if response.status_code == 200 :
                print('sucessfull conection')
                #for model in response.json().get("data", []):  # Assuming the API returns a JSON with 'data' key
                    #print(f"- {model['id']}: {model.get('description', 'No description available')}")                
            else:
                print(f'faild to connect error code {response.status_code} - {response.text}')

        except Exception as err:
            raise Exception(f'err {err}')
        
    def greeting_user(self, message):
        instruction_is = Make_Get_Request.user_instruction()
        #print(instruction_is)
        # self.conversation_history.append({
        #     "role" : "system",
        #     "content" : instruction_is
        # })
        
        self.conversation_history.append({"role": "user" , "content": message})
        
        response = self.mistril_clinet.chat.complete(
            model = self.model,
            messages = self.conversation_history
        )
        result = response.choices[0].message.content
        print(' Answer **************** \n',response.choices[0].message.content)
        print('Completed *************')
        yield result