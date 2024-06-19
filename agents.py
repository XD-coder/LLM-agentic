class agents :
    """
    """
    def __init__(self,description, system_prompt, prompt_templates,max_iteration = 10 , stop_patterns = None ) -> None:
        self.desc = description
        self.sys_prompt = system_prompt
        self.template = prompt_templates
        self.max_iter = max_iteration
        self.stop_sequence = stop_patterns
        
    def agent_start(self):
        pass