import LLM_connect
from groq import AsyncGroq

client = AsyncGroq(api_key=)

class agents :
    """
    """
    def __init__(self,description, system_prompt, prompt_templates,api_to_use = "" , model_to_use = "" ,max_iteration = 10 , stop_patterns = None ) -> None:
        self.desc = description
        self.sys_prompt = system_prompt
        self.template = prompt_templates
        self.max_iter = max_iteration
        self.stop_sequence = stop_patterns
        
    async def agent_start(self):
        await call_LLM()
    
async def call_LLM(chosen_api="", chosen_model=""):
    if chosen_api == "":
        