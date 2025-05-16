from qwen_agent.memory import Memory as BaseMemory

class ContextMemory:
    def __init__(self, llm):
        self.memory = []
        self.summary = ""
        self.llm = llm
        
    def add_interaction(self, user_input, agent_response):
        self.memory.append({
            "user": user_input,
            "agent": agent_response
        })
        self._update_summary()
        
    def _update_summary(self):
        prompt = f"""Summarize these interactions for future context:
        {json.dumps(self.memory[-3:], indent=2)}
        
        Focus on:
        1. File paths/names created/modified
        2. Code snippets
        3. System changes
        
        Format:
        - Files: [file1.py, file2.txt]
        - Code: brief description
        - Changes: system modifications"""
        
        self.summary = self.llm.call(prompt)
