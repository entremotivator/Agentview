import streamlit as st
from graphviz import Digraph

def create_team_diagram():
    # Initialize the diagram
    diagram = Digraph("Super Agent Team", format="png")
    diagram.attr(rankdir="TB", size="15", style="filled", bgcolor="white")

    # Add the main header
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="lightblue")

    # Add top-level managers
    managers = {
        "Operation Manager": "Responsibilities:\n- Execution\n- Communication\n- Coordination with Team",
        "Finance Manager": "Responsibilities:\n- Budgeting\n- Analysis\n- Financial Reports",
        "Support Manager": "Responsibilities:\n- Customer Support\n- Troubleshooting\n- Communication"
    }

    for manager, details in managers.items():
        diagram.node(manager, f"{manager}\n\n{details}", shape="rectangle", style="filled", fillcolor="lightgrey")
        diagram.edge("Super Agent Team", manager)

    # Add sub-agents for each manager (from the image)
    sub_agents = {
        "Operation Manager": [
            {"name": "Task Executor", "tasks": ["Oversee daily operations", "Task delegation"]},
            {"name": "Data Analyst", "tasks": ["Analyze operational metrics", "Generate performance reports"]},
            {"name": "Schedule Manager", "tasks": ["Manage timelines", "Ensure task completion"]}
        ],
        "Finance Manager": [
            {"name": "Budget Analyst", "tasks": ["Monitor spending", "Prepare financial forecasts"]},
            {"name": "Account Manager", "tasks": ["Track expenses", "Invoice management"]},
            {"name": "Tax Consultant", "tasks": ["Tax filing and compliance", "Optimize deductions"]}
        ],
        "Support Manager": [
            {"name": "Customer Liaison", "tasks": ["Resolve customer issues", "Provide updates"]},
            {"name": "Help Desk Agent", "tasks": ["Handle support tickets", "Escalate technical issues"]},
            {"name": "Feedback Specialist", "tasks": ["Collect customer feedback", "Implement improvements"]}
        ]
    }

    # Add sub-agents to the diagram
    for manager, agents in sub_agents.items():
        for agent in agents:
            task_details = "\n".join(agent["tasks"])
            diagram.node(agent["name"], f"{agent['name']}\n\n{task_details}", shape="ellipse", style="filled", fillcolor="lightyellow")
            diagram.edge(manager, agent["name"])

    # Add AI agents (from the image)
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
        diagram.node(ai_agent["name"], f"{ai_agent['name']}\n\n{ai_agent['description']}", shape="parallelogram", style="filled", fillcolor="lightgreen")
        diagram.edge("Super Agent Team", ai_agent["name"])

    return diagram

# Streamlit app layout
st.title("Super Agent Team Structure")
st.write("This is a detailed hierarchical view of the Super Agent Team with responsibilities, tasks, and AI integrations.")

# Display the diagram
st.graphviz_chart(create_team_diagram().source)

# Add interactivity for enhancements
st.sidebar.header("Customize Diagram")
st.sidebar.write("Use these options to customize your team structure.")
add_team = st.sidebar.checkbox("Add New Team Node")
add_ai = st.sidebar.checkbox("Add New AI Agent Node")

if add_team:
    st.sidebar.text_input("Enter Team Node Name")
    st.sidebar.text_area("Enter Team Responsibilities")
    st.sidebar.button("Add Team Node")

if add_ai:
    st.sidebar.text_input("Enter AI Agent Name")
    st.sidebar.text_area("Enter AI Agent Description")
    st.sidebar.button("Add AI Agent")
