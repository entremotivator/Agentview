import streamlit as st
from graphviz import Digraph

def create_pit_diagram():
    # Initialize the diagram
    diagram = Digraph("Super Agent Team", format="svg")
    diagram.attr(rankdir="LR", size="50,10", dpi="300", style="filled", bgcolor="white")  # Horizontal layout (LR)

    # Add the main node
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="deepskyblue", fontcolor="white")

    # Tier 1 (Managers)
    managers = ["Operation Manager", "Finance Manager", "Support Manager"]
    for manager in managers:
        diagram.node(manager, manager, shape="ellipse", style="filled", fillcolor="lightgrey")
        diagram.edge("Super Agent Team", manager)

    # Tier 2 (Sub-agents under each manager)
    operation_agents = ["Task Executor", "Data Analyst", "Schedule Manager"]
    finance_agents = ["Budget Analyst", "Account Manager", "Tax Consultant"]
    support_agents = ["Customer Liaison", "Help Desk Agent", "Feedback Specialist"]

    for agent in operation_agents:
        diagram.node(agent, agent, shape="ellipse", style="filled", fillcolor="lightyellow")
        diagram.edge("Operation Manager", agent)

    for agent in finance_agents:
        diagram.node(agent, agent, shape="ellipse", style="filled", fillcolor="lightyellow")
        diagram.edge("Finance Manager", agent)

    for agent in support_agents:
        diagram.node(agent, agent, shape="ellipse", style="filled", fillcolor="lightyellow")
        diagram.edge("Support Manager", agent)

    # Tier 3 (AI agents)
    ai_agents = ["AI Agent 1", "AI Agent 2", "AI Agent 3", "AI Agent 4", "AI Agent 5", "AI Agent 6", "AI Agent 7"]
    for ai_agent in ai_agents:
        diagram.node(ai_agent, ai_agent, shape="ellipse", style="filled", fillcolor="lightgreen")
        diagram.edge("Support Manager", ai_agent)

    return diagram

# Streamlit layout
st.set_page_config(page_title="Full Scrollable Chart", layout="wide")
st.title("Full Scrollable Super Agent Team Chart")
st.write("A detailed hierarchical team chart that is fully visible and scrollable.")

# Generate the diagram
diagram = create_pit_diagram()
diagram.render("super_agent_team_diagram", format="svg", cleanup=True)

# Embed the full chart in an iframe
html_code = """
    <iframe src="super_agent_team_diagram.svg" width="100%" height="1200px" style="border:none; overflow:auto;"></iframe>
"""
st.markdown(html_code, unsafe_allow_html=True)



