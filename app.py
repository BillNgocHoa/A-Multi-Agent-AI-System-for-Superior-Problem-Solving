from flask import Flask, render_template, jsonify, request
from core.orchestrator import Orchestrator
from core.strategies.round_robin import RoundRobinStrategy
from agents.idea_generator import IdeaGenerator
from agents.pragmatist import Pragmatist
from agents.critic import Critic
from agents.refiner import Refiner
from agents.single_agent_handler import handle_single_agent
import os
from dotenv import load_dotenv
import json
from datetime import datetime
import webbrowser
from threading import Timer
import sys
import signal

app = Flask(__name__)
load_dotenv()

# Agent avatars and colors
AGENT_STYLES = {
    "Idea Generator": {
        "avatar": "💡",
        "color": "#00BCD4",  # Cyan
        "bg_color": "#E0F7FA"
    },
    "Pragmatist": {
        "avatar": "🎯",
        "color": "#FFC107",  # Yellow
        "bg_color": "#FFF8E1"
    },
    "Critic": {
        "avatar": "🔍",
        "color": "#F44336",  # Red
        "bg_color": "#FFEBEE"
    },
    "Refiner": {
        "avatar": "✨",
        "color": "#4CAF50",  # Green
        "bg_color": "#E8F5E9"
    },
    "ChatGPT": {
        "avatar": "🤖",
        "color": "#2196F3",  # Blue
        "bg_color": "#E3F2FD"
    }
}

def open_browser():
    # Prevent multiple browser windows by using a new tab instead
    webbrowser.open_new_tab('http://localhost:5000')

@app.route('/')
def home():
    return render_template('index.html', agent_styles=AGENT_STYLES)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    # Send shutdown signal to the process
    os.kill(os.getpid(), signal.SIGTERM)
    return jsonify({"status": "shutting down"})

@app.route('/start_conversation', methods=['POST'])
def start_conversation():
    data = request.json
    system_type = data.get('system_type')
    problem_statement = data.get('problem_statement')
    selected_agents = data.get('selected_agents', [])

    if system_type == 'single':
        messages = handle_single_agent(problem_statement)
    else:
        # Initialize selected agents
        agents = []
        agent_map = {
            "Idea Generator": IdeaGenerator,
            "Pragmatist": Pragmatist,
            "Critic": Critic,
            "Refiner": Refiner
        }
        
        for agent_name in selected_agents:
            if agent_name in agent_map:
                agents.append(agent_map[agent_name]())

        if not agents:
            return jsonify({"error": "No agents selected"}), 400

        # Initialize orchestrator
        turn_strategy = RoundRobinStrategy(agents)
        orchestrator = Orchestrator(turn_strategy)
        
        # Start and run conversation
        orchestrator.start_conversation(problem_statement)
        messages = orchestrator.run_conversation()
        # Save conversation history
        orchestrator.print_conversation_history()

    # Format messages for the frontend
    formatted_messages = []
    for msg in messages:
        role = msg["role"]
        formatted_messages.append({
            "role": role,
            "content": msg["content"],
            "timestamp": msg["timestamp"],
            "avatar": AGENT_STYLES[role]["avatar"],
            "color": AGENT_STYLES[role]["color"],
            "bg_color": AGENT_STYLES[role]["bg_color"]
        })

    return jsonify({"messages": formatted_messages})

if __name__ == '__main__':
    # Open browser after a short delay
    Timer(1.0, open_browser).start()
    app.run(debug=True) 