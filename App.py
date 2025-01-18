import streamlit as st
from graphviz import Digraph

# Function to create the hierarchical diagram
def create_pit_diagram():
    # Initialize the diagram
    diagram = Digraph("Super Agent Team", format="svg")
    diagram.attr(rankdir="LR", size="50,10", dpi="300", style="filled", bgcolor="white")  # Horizontal layout (LR)

    # Add the main node (Super Agent Team)
    diagram.node(
        "Super Agent Team",
        "Super Agent Team",
        shape="rectangle",
        style="filled",
        fillcolor="deepskyblue",
        fontcolor="white",
        fontsize="20"
    )

    # Tier 1: Managers
    managers = {
        "Operation Manager": "lightgrey",
        "Finance Manager": "lightgrey",
        "Support Manager": "lightgrey"
    }
    for manager, color in managers.items():
        diagram.node(manager, manager, shape="ellipse", style="filled", fillcolor=color)
        diagram.edge("Super Agent Team", manager)

    # Tier 2: Sub-agents under each manager
    sub_agents = {
        "Operation Manager": ["Task Executor", "Data Analyst", "Schedule Manager"],
        "Finance Manager": ["Budget Analyst", "Account Manager", "Tax Consultant"],
        "Support Manager": ["Customer Liaison", "Help Desk Agent", "Feedback Specialist"]
    }
    for manager, agents in sub_agents.items():
        for agent in agents:
            diagram.node(agent, agent, shape="ellipse", style="filled", fillcolor="lightyellow")
            diagram.edge(manager, agent)

    # Tier 3: AI Agents (connected to Support Manager)
    ai_agents = ["AI Agent 1", "AI Agent 2", "AI Agent 3", "AI Agent 4", 
                 "AI Agent 5", "AI Agent 6", "AI Agent 7"]
    
    for ai_agent in ai_agents:
        diagram.node(ai_agent, ai_agent, shape="ellipse", style="filled", fillcolor="lightgreen")
        diagram.edge("Support Manager", ai_agent)

    # Additional styling examples (optional)
    diagram.attr(label="Super Agent Team Hierarchy Diagram\n\nGenerated with Streamlit & Graphviz")
    diagram.attr(fontsize="14")

    return diagram

# Streamlit app layout
st.set_page_config(page_title="Super Agent Team Chart", layout="wide")
st.title("📊 Super Agent Team Hierarchy Diagram")
st.write("""
This interactive chart visualizes a hierarchical structure of a team with multiple tiers:
- **Tier 1:** Managers overseeing operations, finance, and support.
- **Tier 2:** Sub-agents reporting to respective managers.
- **Tier 3:** AI agents assisting the support team.
""")

# Generate and render the diagram
diagram = create_pit_diagram()
diagram.render("super_agent_team_diagram", format="svg", cleanup=True)

# Embed the full chart in an iframe for better visualization
html_code = """
<iframe src="super_agent_team_diagram.svg" width="100%" height="1200px" style="border:none; overflow:auto;"></iframe>
"""
st.markdown(html_code, unsafe_allow_html=True)

# Optional: Add a download button for the SVG file
with open("super_agent_team_diagram.svg", "rb") as file:
    st.download_button(
        label="📥 Download Diagram (SVG)",
        data=file,
        file_name="super_agent_team_diagram.svg",
        mime="image/svg+xml"
    )




