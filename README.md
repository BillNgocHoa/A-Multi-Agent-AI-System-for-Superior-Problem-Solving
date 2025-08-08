# Cognitive Synergy: Multi-Agent Collaboration with LLMs for Superior Problem Solving

This project investigates whether **a team of AI agents**—each with a distinct cognitive role—can collaboratively solve open-ended, real-world problems **more effectively than a single AI agent**. Inspired by real-world teamwork, the system orchestrates GPT agents through structured dialogue to produce creative, practical, and robust solutions.


> 🧠 **Goal:** Simulate expert-level discussions using AI to **enhance reasoning and decision-making** for complex or ambiguous challenges.

---

## 🚀 Key Features

- 🤖 **Multi-Agent System**: Four AI agents with distinct personalities and thinking styles work together.
- 🧠 **Cognitive Diversity**: Roles are designed based on the Six Thinking Hats and research in group intelligence.
- 🛠️ **Prompt Engineering**: Each agent is defined with role-specific, constraint-based, and behaviour-anchored prompts.
- 🔁 **Custom Orchestrator**: Manages agent turn-taking via round-robin or priority-based strategies.
- 🌐 **Web Interface**: Built with Flask for easy interaction, agent selection, and live multi-agent chat visualization.
- 📊 **Evaluation Framework**: Combines human feedback and LLM evaluation (Gemini) across metrics like creativity, feasibility, and logical flow.

---
## 📊 Results & Impact

Over **50+ test cases** were conducted on real-world, open-ended problems. The system was evaluated through both **human feedback** and **LLM evaluation (Gemini)**.

### 🏁 Example Problem:  
**"How to stay focused while working from home on a tight budget?"**

- ✅ Multi-agent system consistently produced 3–5 **high-impact** solutions  
- ✅ Ideas included realistic practices (e.g., Pomodoro technique, noise-canceling hacks) combined with creative suggestions (e.g., gamification of tasks)

### 📈 Performance Metrics

| Evaluation Criteria       | Human Users (Avg /10) | Gemini LLM |
|--------------------------|------------------------|------------|
| Creativity               | 7.55                   | 8.1        |
| Feasibility              | 8.45                   | 8.9        |
| Clarity                  | 8.6                    | 9.2        |
| Logical Flow             | 8.65                   | 9.1        |
| Role Consistency         | 95%                    | 96%        |
| Idea Diversity           | 75%                    | 80%        |
| Constructiveness         | 8.75                   | 9.4        |

- 💡 **88% success rate** across problem types
- 📉 Failure cases mostly involved misunderstanding or topic drift (12%)
- 📌 Removing any agent degraded quality, proving value of role diversity

> 🔍 **Conclusion**: The multi-agent system **outperformed single-agent GPT-4o** in generating more holistic, diverse, and robust solutions—especially for ambiguous, high-level, or trade-off-driven problems.

---

## 🛠️ Tech Stack

- Python, Flask, HTML/CSS
- OpenAI GPT-4o (via API)
- Gemini (for independent evaluation)
- Prompt Engineering

---

## 🧪 Try It Yourself

The system supports both CLI and web-based interaction. You can toggle between single-agent and multi-agent modes, or disable individual agents to study their impact on solution quality.

---

## 📌 Why It Matters

This project demonstrates how **collaborative AI systems** can simulate effective team-based reasoning. The results open up pathways for integrating LLM agents into **human decision-making environments**, enhancing creativity, critical thinking, and solution feasibility.

---
## 📄 License

This work is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.  
It may be used and adapted for non-commercial purposes with proper attribution.  
**Commercial use is strictly prohibited.**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

---

## 📄 Author

**Ngoc Hoa Nguyen**  
BSc Hons Computer Science, University of Nottingham  
[LinkedIn] | [Portfolio] 


---

