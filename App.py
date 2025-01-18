import streamlit as st
from graphviz import Digraph

def create_fullscreen_diagram():
    # Initialize the diagram with larger dimensions
    diagram = Digraph("Super Agent Team", format="png")
    diagram.attr(rankdir="LR", size="25,15", dpi="200", style="filled", bgcolor="white")

    # Add the main header
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="deepskyblue", fontcolor="white")

    # Add top-level managers
    managers = {
        "Operation Manager": "Execution\nCoordination\nCommunication",
        "Finance Manager": "Budgeting\nAnalysis\nFinancial Reports",
        "Support Manager": "Customer Support\nTroubleshooting\nCommunication"
    }

    for manager, details in managers.items():
        diagram.node(manager, f"{manager}\n\n{details}", shape="rectangle", style="filled", fillcolor="lightgrey", fontcolor="black")
        diagram.edge("Super Agent Team", manager)

    # Add sub-agents for each manager
    sub_agents = {
        "Operation Manager": [
            {"name": "Task Executor", "tasks": ["Daily operations", "Task delegation"]},
            {"name": "Data Analyst", "tasks": ["Analyze metrics", "Performance reports"]},
            {"name": "Schedule Manager", "tasks": ["Manage timelines", "Ensure task completion"]}
        ],
        "Finance Manager": [
            {"name": "Budget Analyst", "tasks": ["Monitor spending", "Financial forecasts"]},
            {"name": "Account Manager", "tasks": ["Track expenses", "Invoice management"]},
            {"name": "Tax Consultant", "tasks": ["Tax compliance", "Optimize deductions"]}
        ],
        "Support Manager": [
            {"name": "Customer Liaison", "tasks": ["Resolve issues", "Provide updates"]},
            {"name": "Help Desk Agent", "tasks": ["Support tickets", "Technical escalations"]},
            {"name": "Feedback Specialist", "tasks": ["Collect feedback", "Implement improvements"]}
        ]
    }

    for manager, agents in sub_agents.items():
        for agent in agents:
            task_details = "\n".join(agent["tasks"])
            diagram.node(agent["name"], f"{agent['name']}\n\n{task_details}", shape="ellipse", style="filled", fillcolor="lightyellow", fontcolor="black")
            diagram.edge(manager, agent["name"])

    # Add AI agents
    ai_agents = [
        {"name": "AI Agent 1", "description": "Handles NLP tasks, sentiment analysis, and text summarization."},
        {"name": "AI Agent 2", "description": "Manages predictive analytics and decision-making algorithms."},
        {"name": "AI Agent 3", "description": "Specializes in computer vision and image processing tasks."},
        {"name": "AI Agent 4", "description": "Provides chatbot functionality for customer interaction."},
        {"name": "AI Agent 5", "description": "Automates data entry and processing tasks."},
        {"name": "AI Agent 6", "description": "Optimizes marketing campaigns and audience targeting."},
        {"name": "AI Agent 7", "description": "Generates reports on team and project performance."}
    ]

    for ai_agent in ai_agents:
        diagram.node(ai_agent["name"], f"{ai_agent['name']}\n\n{ai_agent['description']}", shape="parallelogram", style="filled", fillcolor="lightgreen", fontcolor="black")
        diagram.edge("Super Agent Team", ai_agent["name"])

    return diagram

# Streamlit app layout
st.set_page_config(page_title="Super Agent Team", page_icon=":star:", layout="wide")
st.title("Super Agent Team Structure")
st.write("A detailed, full-screen hierarchical diagram of the Super Agent Team, including managers, sub-agents, and AI integrations.")

# Render the full-screen diagram
diagram = create_fullscreen_diagram()
st.graphviz_chart(diagram.source, use_container_width=True)

