from typing import List
from agents.base import Message

class TerminationChecker:
    def __init__(self, max_rounds: int = 2):
        self.max_rounds = max_rounds
        self.current_round = 0

    def should_terminate(self, history: List[Message], current_round: int) -> bool:
        """Check if the conversation should terminate based on predefined conditions."""
        # Check if we've reached the maximum number of rounds
        if current_round >= self.max_rounds:
            return True

        # Check if the last message was from the Refiner
        if history and history[-1].role == "Refiner":
            # If the Refiner has provided a comprehensive solution, we might want to end
            if "final solution" in history[-1].content.lower() or "conclusion" in history[-1].content.lower():
                return True

        return False

    def reset(self):
        """Reset the termination checker state."""
        self.current_round = 0 