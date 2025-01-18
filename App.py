import streamlit as st
from graphviz import Digraph

def create_long_pit_diagram():
    # Initialize the pit diagram
    diagram = Digraph("Super Agent Team", format="svg")
    diagram.attr(rankdir="TB", size="15,30", dpi="200", style="filled", bgcolor="white")

    # Add the main node
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="deepskyblue", fontcolor="white")

    # Add tiers and relationships
    tiers = {
        "Tier 1": ["Operation Manager", "Finance Manager", "Support Manager"],
        "Tier 2": [
            "Task Executor", "Data Analyst", "Schedule Manager",
            "Budget Analyst", "Account Manager", "Tax Consultant",
            "Customer Liaison", "Help Desk Agent", "Feedback Specialist"
        ],
        "Tier 3": [
            "AI Agent 1", "AI Agent 2", "AI Agent 3",
            "AI Agent 4", "AI Agent 5", "AI Agent 6", "AI Agent 7"
        ]
    }

    # Add tier nodes
    for tier, nodes in tiers.items():
        for node in nodes:
            if tier == "Tier 1":
                fillcolor = "lightgrey"
            elif tier == "Tier 2":
                fillcolor = "lightyellow"
            else:
                fillcolor = "lightgreen"
            diagram.node(node, node, shape="ellipse", style="filled", fillcolor=fillcolor, fontcolor="black")
            if tier == "Tier 1":
                diagram.edge("Super Agent Team", node)
            elif tier == "Tier 2":
                parent = "Operation Manager" if node in ["Task Executor", "Data Analyst", "Schedule Manager"] else \
                         "Finance Manager" if node in ["Budget Analyst", "Account Manager", "Tax Consultant"] else \
                         "Support Manager"
                diagram.edge(parent, node)
            elif tier == "Tier 3":
                diagram.edge("Super Agent Team", node)

    return diagram

# Streamlit layout
st.set_page_config(page_title="Scrollable Pit Diagram", layout="wide")
st.title("Scrollable Super Agent Team Pit Diagram")
st.write("A detailed hierarchical pit diagram of the Super Agent Team with scrolling enabled.")

# Generate the diagram
diagram = create_long_pit_diagram()
diagram.render("pit_diagram", format="svg", cleanup=True)

# Embed the diagram in an iframe
html_code = """
    <iframe src="pit_diagram.svg" width="100%" height="800px" style="border:none; overflow:auto;"></iframe>
"""
st.markdown(html_code, unsafe_allow_html=True)


