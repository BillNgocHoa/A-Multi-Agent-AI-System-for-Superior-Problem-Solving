from typing import List, Dict
from agents.base import Message, BaseAgent

class MessageRouter:
    def __init__(self):
        self.conversation_history: List[Message] = []

    def build_context(self, agent: BaseAgent, history: List[Message]) -> List[Dict[str, str]]:
        """Build the context for the agent based on conversation history."""
        messages = [
            # {"role": "system", "content": agent.system_prompt},
            # *[{"role": "assistant" if msg.role != "system" else "system", 
            #    "content": f"[{msg.role}]: {msg.content}"} 
            #   for msg in history]
            {"role": "system", "content": agent.system_prompt}
        ]
        
        # Add conversation history with proper role handling
        for msg in history:
            if msg.role == "system":
                messages.append({"role": "system", "content": msg.content})
            else:
                # For agent messages, use the actual agent name as the role
                messages.append({
                    "role": "assistant",
                    "content": msg.content  # Remove role prefix to avoid duplication
                })
        
        return messages

    def add_message(self, message: Message):
        """Add a message to the conversation history."""
        self.conversation_history.append(message)

    def get_history(self) -> List[Message]:
        """Get the complete conversation history."""
        return self.conversation_history

    def reset(self):
        """Reset the conversation history."""
        self.conversation_history = [] 