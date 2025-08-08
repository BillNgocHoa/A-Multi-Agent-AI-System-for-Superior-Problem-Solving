from typing import List, Dict
from datetime import datetime
from agents.idea_generator import IdeaGenerator
from agents.pragmatist import Pragmatist
from agents.critic import Critic
from agents.refiner import Refiner
from core.turn_strategy import TurnStrategy
from core.message_router import MessageRouter
from core.termination_checker import TerminationChecker
from agents.base import Message
import time
import json

class Orchestrator:
    def __init__(self, turn_strategy: TurnStrategy, max_rounds: int = 2):
        self.agents = [
            IdeaGenerator(),
            Pragmatist(),
            Critic(),
            Refiner()
        ]
        self.turn_strategy = turn_strategy
        self.message_router = MessageRouter()
        self.termination_checker = TerminationChecker(max_rounds)
        self.conversation = None

    def start_conversation(self, problem_statement: str) -> List[Dict]:
        """Start a new conversation with the given problem statement."""
        initial_message = Message(
            role="system",
            content=problem_statement,
            timestamp=datetime.now().isoformat()
        )
        self.message_router.add_message(initial_message)
        return [initial_message.dict()]

    def run_conversation(self) -> List[Dict]:
        """Run the conversation following the specified flow."""
        messages = []
        
        while True:
            # Get next agent using the strategy
            agent = self.turn_strategy.get_next_agent()
            current_round = self.turn_strategy.get_current_round()
            
            # Build context for the agent
            context = self.message_router.build_context(agent, self.message_router.get_history())
            
            # Get response from agent
            response = agent.get_response(context)
            
            # Create and store message with proper role
            message = Message(
                role=agent.name,
                content=response,
                timestamp=datetime.now().isoformat()
            )
            
            # Add message to history and current messages
            self.message_router.add_message(message)
            messages.append(message.dict())
            
            # Add delay for natural conversation flow
            time.sleep(1)
            
            # Check termination conditions
            if self.termination_checker.should_terminate(self.message_router.get_history(), current_round):
                break

        return messages

    def get_conversation_history(self) -> List[Dict]:
        """Get the complete conversation history."""
        return [msg.dict() for msg in self.message_router.get_history()]
    
    def print_conversation_history(self):
        """Save to a Text file in a readable format."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_history_{timestamp}.txt"
        
        history = self.get_conversation_history()
        with open(filename, 'w', encoding='utf-8') as f:  # Specify UTF-8 encoding
            for msg in history:
                role = msg["role"]
                content = msg["content"]
                timestamp = msg["timestamp"]
                
                f.write(f"\n{role} ({timestamp}):\n")
                f.write(f"{content}\n")
                f.write("-" * 80 + "\n")

    def reset(self):
        """Reset all components."""
        self.turn_strategy.reset()
        self.message_router.reset()
        self.termination_checker.reset()
        for agent in self.agents:
            agent.reset() 