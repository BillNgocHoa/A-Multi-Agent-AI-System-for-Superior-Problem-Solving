from core.orchestrator import Orchestrator
from core.strategies.round_robin import RoundRobinStrategy
from core.strategies.priority_based import PriorityBasedStrategy
from agents.idea_generator import IdeaGenerator
from agents.pragmatist import Pragmatist
from agents.critic import Critic
from agents.refiner import Refiner
from agents.single_agent_handler import handle_single_agent
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
import os
import sys
from dotenv import load_dotenv

load_dotenv() # Load the environment variables from the .env file

def get_agent_selection():
    console = Console()
    available_agents = {
        "1": ("Idea Generator", IdeaGenerator),
        "2": ("Pragmatist", Pragmatist),
        "3": ("Critic", Critic),
        "4": ("Refiner", Refiner)
    }
    
    console.print("\n[bold]Available Agents:[/bold]")
    for key, (name, _) in available_agents.items():
        console.print(f"{key}. {name}")
    
    console.print("\n[bold]Select agents to include (enter numbers separated by spaces, e.g., '1 2 3'):[/bold]")
    while True:
        try:
            choices = input("Enter your choices: ").strip().split()
            selected_agents = []
            for choice in choices:
                if choice in available_agents:
                    name, agent_class = available_agents[choice]
                    selected_agents.append(agent_class())
                else:
                    raise ValueError(f"Invalid choice: {choice}")
            
            if not selected_agents:
                console.print("[red]Error: Please select at least one agent[/red]")
                continue
                
            return selected_agents
        except ValueError as e:
            console.print(f"[red]Error: {str(e)}[/red]")
            console.print("Please try again with valid choices")

def main():
    console = Console()

    # Example problem statement
    problem_statement = """Problem: How to be focused on a task when there are so many distractions for a person who is working from home within tight budget?"""
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        console.print("[red]Error: OPENAI_API_KEY not found in environment variables[/red]")
        console.print("Please create a .env file with your OpenAI API key:")
        console.print("OPENAI_API_KEY=your_api_key_here")
        return


    # Ask user to choose between single or multi-agent system
    console.print("\n[bold]Please choose the type of system:[/bold]")
    console.print("1. Single Agent (ChatGPT)")
    console.print("2. Multi-Agent System")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            break
        console.print("[red]Invalid choice. Please enter 1 or 2.[/red]")

    if choice == '1':
        # Handle single agent case
        messages = handle_single_agent(problem_statement)
        sys.exit()
    else:
        # Initialize agents for multi-agent system
        # Get user's agent selection
        agents = get_agent_selection()


    # Initialize agents
    # agents = [
    #     IdeaGenerator(),
    #     Pragmatist(),
    #     Critic(),
    #     Refiner()
    # ]

    # Choose turn-taking strategy
    # Option 1: Round-robin strategy
    turn_strategy = RoundRobinStrategy(agents)
    
    # Option 2: Priority-based strategy
    # priorities = {
    #     "Idea Generator": 3,
    #     "Pragmatist": 2,
    #     "Critic": 1,
    #     "Refiner": 4
    # }
    # turn_strategy = PriorityBasedStrategy(agents, priorities)

    # Initialize the orchestrator with the chosen strategy
    orchestrator = Orchestrator(turn_strategy)
    


    # Display the welcome message
    console.print(Panel.fit(
        "[bold blue]Multi-Agent AI Collaboration System[/bold blue]\n"
        "This system demonstrates how multiple AI agents can collaborate to solve complex problems.",
        title="Welcome"
    ))

    console.print("\n[bold]Problem Statement:[/bold]")
    console.print(Markdown(problem_statement))
    
    console.print("\n[bold green]Starting conversation...[/bold green]")
    
    # Start the conversation
    orchestrator.start_conversation(problem_statement)
    
    # Run the conversation
    messages = orchestrator.run_conversation()
    
    # Save conversation history
    orchestrator.print_conversation_history()
    
    # Display the conversation
    console.print("\n[bold]Conversation History:[/bold]")
    for msg in messages:
        role = msg["role"]
        content = msg["content"]
        timestamp = msg["timestamp"]
        
        # Color coding for different agents
        if role == "Idea Generator":
            color = "cyan"
        elif role == "Pragmatist":
            color = "yellow"
        elif role == "Critic":
            color = "red"
        elif role == "Refiner":
            color = "green"
        else:
            color = "white"
        
        console.print(Panel(
            content,
            title=f"[{color}]{role}[/{color}]",
            subtitle=timestamp
        ))

if __name__ == "__main__":
    main() 