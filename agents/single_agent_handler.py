from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
import openai
import os
from datetime import datetime

def handle_single_agent(problem_statement):
    console = Console()
    
    # Initialize OpenAI client
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    console.print("\n[bold green]Starting conversation with ChatGPT...[/bold green]")
    
    try:
        # Get response from ChatGPT
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that provides detailed and thoughtful responses. Give top 3 solutions to the problem statement, and briefly explain them."},
                {"role": "user", "content": problem_statement}
            ]
        )
        
        # Get the response content
        content = response.choices[0].message.content
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Display the response
        console.print(Panel(
            content,
            title="[blue]ChatGPT[/blue]",
            subtitle=timestamp
        ))

        # Create conversation history
        conversation = [{
            "role": "ChatGPT",
            "content": content,
            "timestamp": timestamp
        }]

        # Save to file
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"1_agent_response_{timestamp_str}.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Single Agent (ChatGPT) Response\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Problem Statement:\n{problem_statement}\n\n")
            f.write("=" * 50 + "\n\n")
            
            for msg in conversation:
                f.write(f"Role: {msg['role']}\n")
                f.write(f"Timestamp: {msg['timestamp']}\n")
                f.write("-" * 30 + "\n")
                f.write(f"{msg['content']}\n\n")
                f.write("=" * 50 + "\n\n")
        
        console.print(f"\n[green]Response saved to {filename}[/green]")
        
        return conversation
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        return [] 