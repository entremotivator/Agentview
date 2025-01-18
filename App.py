import streamlit as st
from graphviz import Digraph

# Set page layout to wide
st.set_page_config(page_title="Super Agent Team Structure", layout="wide")

# Custom CSS for fullscreen effect
st.markdown(
    """
    <style>
    .main .block-container {
        padding: 0rem;
        margin: 0rem;
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def create_team_diagram():
    # Initialize the diagram
    diagram = Digraph("Super Agent Team", format="png")
    diagram.attr(rankdir="TB", size="15", style="filled", bgcolor="white")

    # Add the main header
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="lightblue")

    # Add top-level agents
    managers = {
        "Operation Manager": "Responsibilities:\n- Execution\n- Communication\n- Coordination with Team",
        "Finance Manager": "Responsibilities:\n- Budgeting\n- Analysis\n- Financial Reports",
        "Support Manager": "Responsibilities:\n- Customer Support\n- Troubleshooting\n- Communication"
    }

    for manager, details in managers.items():
        diagram.node(manager, f"{manager}\n\n{details}", shape="rectangle", style="filled", fillcolor="lightgrey")
        diagram.edge("Super Agent Team", manager)

    # Add sub-agents with responsibilities and tasks
    sub_agents = {
        "Operation Manager": [
            {"name": "Subagent 1", "tasks": ["Task 1: Create Reports", "Task 2: Analyze Data"]},
            {"name": "Subagent 2", "tasks": ["Task 1: Monitor KPIs", "Task 2: Optimize Operations"]},
            {"name": "Subagent 3", "tasks": ["Task 1: Schedule Meetings", "Task 2: Update SOPs"]}
        ],
        "Finance Manager": [
            {"name": "Subagent 4", "tasks": ["Task 1: Reconcile Accounts", "Task 2: Budget Forecast"]},
            {"name": "Subagent 5", "tasks": ["Task 1: Generate Invoices", "Task 2: Financial Analysis"]}
        ],
        "Support Manager": [
            {"name": "Subagent 6", "tasks": ["Task 1: Resolve Tickets", "Task 2: Customer Feedback"]},
            {"name": "Subagent 7", "tasks": ["Task 1: Escalate Issues", "Task 2: Manage FAQs"]}
        ]
    }

    for manager, agents in sub_agents.items():
        for agent in agents:
            task_details = "\n".join(agent["tasks"])
            diagram.node(agent["name"], f"{agent['name']}\n\n{task_details}", shape="ellipse", style="filled", fillcolor="lightyellow")
            diagram.edge(manager, agent["name"])

    # Add AI agents
    ai_agents = [
        {"name": "AI Agent 1", "description": "Handles NLP tasks, sentiment analysis, and text summarization."},
        {"name": "AI Agent 2", "description": "Manages predictive analytics and decision-making algorithms."},
        {"name": "AI Agent 3", "description": "Specializes in computer vision and image processing tasks."}
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

# Sidebar interactivity for enhancements
st.sidebar.header("Customize Diagram")
st.sidebar.write("Use these options to customize your team structure.")
add_team = st.sidebar.checkbox("Add New Team Node")
add_ai = st.sidebar.checkbox("Add New AI Agent Node")

if add_team:
    team_name = st.sidebar.text_input("Enter Team Node Name")
    team_responsibilities = st.sidebar.text_area("Enter Team Responsibilities")
    if st.sidebar.button("Add Team Node"):
        st.write(f"New team node '{team_name}' with responsibilities added (not yet dynamically integrated).")

if add_ai:
    ai_name = st.sidebar.text_input("Enter AI Agent Name")
    ai_description = st.sidebar.text_area("Enter AI Agent Description")
    if st.sidebar.button("Add AI Agent"):
        st.write(f"New AI agent '{ai_name}' added with description (not yet dynamically integrated).")




