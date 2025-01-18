import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph

# Function to create a NetworkX graph
def create_networkx_graph():
    G = nx.DiGraph()
    G.add_edges_from([
        ("Super Agent Team", "Operation Manager"),
        ("Super Agent Team", "Finance Manager"),
        ("Super Agent Team", "Support Manager"),
        ("Operation Manager", "Task Executor"),
        ("Finance Manager", "Budget Analyst"),
        ("Support Manager", "Customer Liaison")
    ])
    return G

# Function to render a Graphviz diagram
def create_graphviz_diagram():
    diagram = Digraph("Super Agent Team", format="png")
    diagram.attr(rankdir="TB", size="15", style="filled", bgcolor="white")

    # Add main node
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="lightblue")

    # Add managers and their responsibilities
    managers = {
        "Operation Manager": "Responsibilities:\n- Execution\n- Communication\n- Coordination with Team",
        "Finance Manager": "Responsibilities:\n- Budgeting\n- Analysis\n- Financial Reports",
        "Support Manager": "Responsibilities:\n- Customer Support\n- Troubleshooting\n- Communication"
    }

    for manager, details in managers.items():
        diagram.node(manager, f"{manager}\n\n{details}", shape="rectangle", style="filled", fillcolor="lightgrey")
        diagram.edge("Super Agent Team", manager)

    # Add sub-agents for each manager
    sub_agents = {
        "Operation Manager": ["Subagent 1", "Subagent 2", "Subagent 3"],
        "Finance Manager": ["Subagent 4", "Subagent 5"],
        "Support Manager": ["Subagent 6", "Subagent 7"]
    }

    for manager, agents in sub_agents.items():
        for agent in agents:
            diagram.node(agent, agent, shape="ellipse", style="filled", fillcolor="lightyellow")
            diagram.edge(manager, agent)

    # Add AI agents
    ai_agents = [
        {"name": "AI Agent 1", "description": "NLP tasks, sentiment analysis, text summarization."},
        {"name": "AI Agent 2", "description": "Predictive analytics, decision-making algorithms."},
        {"name": "AI Agent 3", "description": "Computer vision and image processing tasks."}
    ]

    for ai_agent in ai_agents:
        diagram.node(ai_agent["name"], f"{ai_agent['name']}\n\n{ai_agent['description']}", shape="parallelogram", style="filled", fillcolor="lightgreen")
        diagram.edge("Super Agent Team", ai_agent["name"])

    return diagram

# Streamlit Layout
st.title("Interactive Team and AI Visualization")
st.sidebar.header("Choose Visualization Type")
vis_type = st.sidebar.radio("Select a visualization type:", ("NetworkX Graph", "Graphviz Diagram"))

if vis_type == "NetworkX Graph":
    st.subheader("NetworkX Graph Representation")
    G = create_networkx_graph()
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=10, font_weight="bold")
    st.pyplot(plt)

elif vis_type == "Graphviz Diagram":
    st.subheader("Graphviz Hierarchical Diagram")
    diagram = create_graphviz_diagram()
    st.graphviz_chart(diagram.source)

# Customization Features
st.sidebar.header("Add New Nodes")
if st.sidebar.checkbox("Add Team Member"):
    new_team_member = st.sidebar.text_input("Enter Team Member Name")
    new_responsibilities = st.sidebar.text_area("Enter Responsibilities")
    if st.sidebar.button("Add Member"):
        st.write(f"Added Team Member: {new_team_member}")
        st.write(f"Responsibilities:\n{new_responsibilities}")

if st.sidebar.checkbox("Add AI Agent"):
    new_ai_agent = st.sidebar.text_input("Enter AI Agent Name")
    new_ai_description = st.sidebar.text_area("Enter AI Agent Description")
    if st.sidebar.button("Add AI Agent"):
        st.write(f"Added AI Agent: {new_ai_agent}")
        st.write(f"Description:\n{new_ai_description}")
