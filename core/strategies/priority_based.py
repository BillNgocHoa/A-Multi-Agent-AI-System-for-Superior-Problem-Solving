from core.turn_strategy import TurnStrategy
from agents.base import BaseAgent
from typing import Dict

class PriorityBasedStrategy(TurnStrategy):
    """Priority-based turn-taking strategy."""
    
    def __init__(self, agents: list[BaseAgent], priorities: Dict[str, int]):
        super().__init__(agents)
        self.priorities = priorities
        self.agent_order = self._sort_agents_by_priority()
        self.current_agent_index = 0

    def _sort_agents_by_priority(self) -> list[BaseAgent]:
        """Sort agents based on their priority."""
        return sorted(
            self.agents,
            key=lambda agent: self.priorities.get(agent.name, 0),
            reverse=True
        )

    def get_next_agent(self) -> BaseAgent:
        """Get the next agent based on priority."""
        agent = self.agent_order[self.current_agent_index]
        self.current_agent_index = (self.current_agent_index + 1) % len(self.agents)
        if self.current_agent_index == 0:
            self.current_round += 1
        return agent

    def reset(self):
        """Reset the strategy state."""
        super().reset()
        self.current_agent_index = 0
        self.agent_order = self._sort_agents_by_priority() 