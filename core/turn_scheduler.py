from typing import List
from agents.base import BaseAgent

class TurnScheduler:
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents
        self.current_round = 0
        self.current_agent_index = 0

    def get_next_agent(self) -> BaseAgent:
        """Get the next agent in the round-robin sequence."""
        agent = self.agents[self.current_agent_index]
        self.current_agent_index = (self.current_agent_index + 1) % len(self.agents)
        if self.current_agent_index == 0:
            self.current_round += 1
        return agent

    def get_current_round(self) -> int:
        """Get the current round number."""
        return self.current_round

    def reset(self):
        """Reset the scheduler state."""
        self.current_round = 0
        self.current_agent_index = 0 