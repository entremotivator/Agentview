import streamlit as st
from graphviz import Digraph

def create_team_diagram():
    # Initialize the diagram
    diagram = Digraph("Super Agent Team", format="png")
    diagram.attr(rankdir="TB", size="15", style="filled", bgcolor="white")

    # Add the main header
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="deepskyblue")

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
st.set_page_config(page_title="Super Agent Team", page_icon=":gear:", layout="wide")
st.title("Super Agent Team Structure")
st.write("Explore the detailed hierarchical structure of the Super Agent Team, including managers, their responsibilities, team members, and AI integrations.")

# Display the diagram in full screen
diagram = create_team_diagram()
st.graphviz_chart(diagram.source, use_container_width=True)

# Sidebar interactivity
st.sidebar.header("Customize Diagram")
add_team = st.sidebar.checkbox("Add New Team Node")
add_ai = st.sidebar.checkbox("Add New AI Agent Node")

if add_team:
    new_team_name = st.sidebar.text_input("Enter Team Node Name")
    new_team_details = st.sidebar.text_area("Enter Team Responsibilities")
    if st.sidebar.button("Add Team Node"):
        st.write(f"New team '{new_team_name}' added with responsibilities: {new_team_details}")

if add_ai:
    new_ai_name = st.sidebar.text_input("Enter AI Agent Name")
    new_ai_description = st.sidebar.text_area("Enter AI Agent Description")
    if st.sidebar.button("Add AI Agent"):
        st.write(f"New AI Agent '{new_ai_name}' added with description: {new_ai_description}")
