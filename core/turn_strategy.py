from abc import ABC, abstractmethod
from typing import List
from agents.base import BaseAgent

class TurnStrategy(ABC):
    """Abstract base class for turn-taking strategies."""
    
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents
        self.current_round = 0

    @abstractmethod
    def get_next_agent(self) -> BaseAgent:
        """Get the next agent based on the strategy."""
        pass

    def get_current_round(self) -> int:
        """Get the current round number."""
        return self.current_round

    def reset(self):
        """Reset the strategy state."""
        self.current_round = 0 