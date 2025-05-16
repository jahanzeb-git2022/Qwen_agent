from qwen_agent.agents import Assistant
from tools.file import FileTool
from tools.shell import ShellTool
from tools.memory import ContextMemory
import os

class Qwen3Agent:
    def __init__(self):
        self.tools = [
            FileTool(),
            ShellTool(),
            WebSearchTool(),
            EmailTool(),
            CodeInterpreterTool()
        ]
        
        self.agent = Assistant(
            llm=self._init_llm(),
            function_list=self.tools,
            system_message=self._load_prompt('system_prompt')
        )
        self.memory = ContextMemory(self.agent.llm)
        
    def _init_llm(self):
        from qwen_agent.llm import CustomLLM
        return CustomLLM(
            base_url="https://api.together.xyz/v1 ",
            api_key=os.getenv("TOGETHER_API_KEY"),
            model="Qwen/Qwen3-235B-A22B-FP8"
        )
        
    def run_task(self, user_query):
        # Add memory context
        enriched_query = f"{user_query}\n\nUseful Context:\n{self.memory.summary}"
        
        # Execute task
        result = []
        for response in self.agent.run([{'role': 'user', 'content': enriched_query}]):
            result.append(response)
            
        # Update memory
        self.memory.add_interaction(user_query, "\n".join(result))
        return result
