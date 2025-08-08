from core.turn_strategy import TurnStrategy
from agents.base import BaseAgent

class RoundRobinStrategy(TurnStrategy):
    """Round-robin turn-taking strategy."""
    
    def __init__(self, agents: list[BaseAgent]):
        super().__init__(agents)
        self.current_agent_index = 0

    def get_next_agent(self) -> BaseAgent:
        """Get the next agent in the round-robin sequence."""
        agent = self.agents[self.current_agent_index]
        self.current_agent_index = (self.current_agent_index + 1) % len(self.agents)
        if self.current_agent_index == 0:
            self.current_round += 1
        return agent

    def reset(self):
        """Reset the strategy state."""
        super().reset()
        self.current_agent_index = 0 