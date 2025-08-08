from typing import List, Dict, Any
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os

load_dotenv()

class Message(BaseModel):
    role: str
    content: str
    timestamp: str

class BaseAgent:
    def __init__(self, name: str, role: str, system_prompt: str):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.conversation_history: List[Message] = []
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_response(self, messages: List[Dict[str, str]]) -> str:
        """Get a response from the agent based on the conversation history."""
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.8,  # Slightly higher for more natural responses
                max_tokens=300,   # Increased for more natural conversation
                presence_penalty=0.6,  # Encourage more diverse responses
                frequency_penalty=0.6  # Reduce repetition
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error getting response from {self.name}: {str(e)}")
            return "I apologize, but I'm having trouble processing that right now."

    def process_message(self, message: Message) -> Message:
        """Process an incoming message and generate a response."""
        # Add the incoming message to conversation history
        self.conversation_history.append(message)
        
        # Prepare messages for the API call
        messages = [
            {"role": "system", "content": self.system_prompt},
            # *[{"role": "assistant" if msg.role != "system" else "system", "content": f"[{msg.role}]: {msg.content}"} for msg in self.conversation_history]
            # *[{"role": "assistant", "content": f"{msg.role}: {msg.content}"}
            *[{"role": "assistant", "content": msg.content} 
              for msg in self.conversation_history]
        ]
        
        # Get response from the agent
        response_content = self.get_response(messages)
        
        # Create and return the response message
        response_message = Message(
            role=self.name,
            content=response_content,
            timestamp=message.timestamp  # Using the same timestamp for response
        )
        
        # Add the response to conversation history
        self.conversation_history.append(response_message)
        
        return response_message

    def reset(self):
        """Reset the agent's conversation history."""
        self.conversation_history = [] 