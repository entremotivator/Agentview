import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph
import streamlit.components.v1 as components
import json
from fpdf import FPDF
import os

# Initialize a list to store agents
agents = [
    {"name": "Task Executor", "manager": "Operation Manager", "tasks": ["Execute daily tasks", "Monitor KPIs", "Prepare status reports"]},
    {"name": "Coordinator", "manager": "Operation Manager", "tasks": ["Coordinate with other departments", "Manage scheduling", "Resolve conflicts"]},
    {"name": "Budget Analyst", "manager": "Finance Manager", "tasks": ["Analyze financial statements", "Prepare budget reports", "Forecast future financial needs"]},
    {"name": "Account Manager", "manager": "Finance Manager", "tasks": ["Reconcile accounts", "Track expenses", "Generate financial reports"]},
    {"name": "Customer Liaison", "manager": "Support Manager", "tasks": ["Handle customer inquiries", "Resolve complaints", "Monitor service quality"]},
    {"name": "Support Specialist", "manager": "Support Manager", "tasks": ["Assist customers", "Update FAQs", "Provide technical support"]}
]

# Function to create a NetworkX graph
def create_networkx_graph():
    G = nx.DiGraph()
    
    # Add the original top-level managers
    G.add_edges_from([
        ("Super Agent Team", "Operation Manager"),
        ("Super Agent Team", "Finance Manager"),
        ("Super Agent Team", "Support Manager"),
        ("Operation Manager", "Task Executor"),
        ("Operation Manager", "Coordinator"),
        ("Finance Manager", "Budget Analyst"),
        ("Finance Manager", "Account Manager"),
        ("Support Manager", "Customer Liaison"),
        ("Support Manager", "Support Specialist")
    ])

    # Add new business-related managers
    new_managers = {
        "HR Manager": ["HR Specialist", "Recruitment Specialist", "Training Coordinator", "Payroll Administrator", "Employee Relations Manager"],
        "IT Manager": ["Network Administrator", "Security Specialist", "Help Desk Support", "System Analyst", "Database Administrator"],
        "Sales Manager": ["Regional Sales Manager", "Sales Trainer", "Account Executive", "Sales Analyst", "Customer Success Manager"],
        "Marketing Manager": ["SEO Specialist", "Social Media Manager", "Content Creator", "Advertising Manager", "Brand Manager"],
        "Product Manager": ["Product Designer", "Product Researcher", "Product Strategist", "Product Developer", "Product Analyst"],
        "Operations Manager": ["Logistics Coordinator", "Supply Chain Manager", "Process Optimization Specialist", "Quality Control Manager", "Operations Analyst"]
    }
    
    # Add the new managers and their sub-managers to the graph
    for manager, sub_managers in new_managers.items():
        G.add_edge("Super Agent Team", manager)
        for sub_manager in sub_managers:
            G.add_edge(manager, sub_manager)

    return G

# Function to render a Graphviz diagram
def create_graphviz_diagram():
    diagram = Digraph("Super Agent Team", format="png")
    diagram.attr(rankdir="TB", size="15", style="filled", bgcolor="white")

    # Add main node
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="lightblue")

    # Add original managers and their responsibilities
    managers = {
        "Operation Manager": "Responsibilities:\n- Oversee daily operations\n- Coordinate with all departments\n- Task execution and delivery",
        "Finance Manager": "Responsibilities:\n- Budget allocation and analysis\n- Financial planning\n- Reporting and forecasting",
        "Support Manager": "Responsibilities:\n- Customer support and satisfaction\n- Troubleshooting and resolving issues\n- Managing feedback",
        "HR Manager": "Responsibilities:\n- Manage recruitment\n- Oversee employee relations\n- Handle payroll and benefits",
        "IT Manager": "Responsibilities:\n- Oversee IT infrastructure\n- Manage network security\n- Support system troubleshooting",
        "Sales Manager": "Responsibilities:\n- Drive sales strategies\n- Train sales team\n- Manage client relationships",
        "Marketing Manager": "Responsibilities:\n- Develop marketing strategies\n- Manage brand presence\n- Oversee advertising campaigns",
        "Product Manager": "Responsibilities:\n- Oversee product development\n- Manage product lifecycle\n- Lead product strategy",
        "Operations Manager": "Responsibilities:\n- Manage operations efficiency\n- Oversee logistics\n- Streamline processes"
    }

    for manager, details in managers.items():
        diagram.node(manager, f"{manager}\n\n{details}", shape="rectangle", style="filled", fillcolor="lightgrey")
        diagram.edge("Super Agent Team", manager)

    # Add agents and sub-managers under their respective managers
    sub_managers = {
        "HR Manager": ["HR Specialist", "Recruitment Specialist", "Training Coordinator", "Payroll Administrator", "Employee Relations Manager"],
        "IT Manager": ["Network Administrator", "Security Specialist", "Help Desk Support", "System Analyst", "Database Administrator"],
        "Sales Manager": ["Regional Sales Manager", "Sales Trainer", "Account Executive", "Sales Analyst", "Customer Success Manager"],
        "Marketing Manager": ["SEO Specialist", "Social Media Manager", "Content Creator", "Advertising Manager", "Brand Manager"],
        "Product Manager": ["Product Designer", "Product Researcher", "Product Strategist", "Product Developer", "Product Analyst"],
        "Operations Manager": ["Logistics Coordinator", "Supply Chain Manager", "Process Optimization Specialist", "Quality Control Manager", "Operations Analyst"]
    }

    for manager, sub_list in sub_managers.items():
        for sub_manager in sub_list:
            diagram.node(sub_manager, f"{sub_manager}", shape="ellipse", style="filled", fillcolor="lightyellow")
            diagram.edge(manager, sub_manager)
    
    # Add agents under their managers
    for agent in agents:
        task_details = "\n".join(agent["tasks"])
        diagram.node(agent["name"], f"{agent['name']}\n\n{task_details}", shape="ellipse", style="filled", fillcolor="lightyellow")
        diagram.edge(agent["manager"], agent["name"])

    return diagram

# Streamlit Layout
st.title("Super Agent Team Structure and Responsibilities")
st.write("This visualization provides a comprehensive breakdown of the Super Agent Team, including roles, responsibilities, and tasks.")

# Choose visualization type
st.sidebar.header("Choose Visualization Type")
vis_type = st.sidebar.radio("Select a visualization type:", ("NetworkX Graph", "Graphviz Diagram"))

# Fullscreen button and JavaScript code
fullscreen_button = """
    <style>
        .fullscreen-btn {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            font-size: 16px;
            cursor: pointer;
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 1000;
        }

        .fullscreen-btn:hover {
            background-color: #45a049;
        }
    </style>
    <button class="fullscreen-btn" onclick="toggleFullScreen()">Toggle Fullscreen</button>
    <script>
    function toggleFullScreen() {
        var elem = document.getElementById("content");
        if (!document.fullscreenElement) {
            if (elem.requestFullscreen) {
                elem.requestFullscreen();
            } else if (elem.mozRequestFullScreen) { // Firefox
                elem.mozRequestFullScreen();
            } else if (elem.webkitRequestFullscreen) { // Chrome, Safari and Opera
                elem.webkitRequestFullscreen();
            } else if (elem.msRequestFullscreen) { // IE/Edge
                elem.msRequestFullscreen();
            }
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.mozCancelFullScreen) { // Firefox
                document.mozCancelFullScreen();
            } else if (document.webkitExitFullscreen) { // Chrome, Safari and Opera
                document.webkitExitFullscreen();
            } else if (document.msExitFullscreen) { // IE/Edge
                document.msExitFullscreen();
            }
        }
    }
    </script>
"""

# Display the appropriate visualization
if vis_type == "NetworkX Graph":
    st.subheader("NetworkX Graph Representation")
    G = create_networkx_graph()
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=10, font_weight="bold")
    
    # Create the graph container with id="content"
    st.markdown('<div id="content">', unsafe_allow_html=True)
    st.pyplot(plt)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Use components.html() for fullscreen button
    components.html(fullscreen_button, height=100)

elif vis_type == "Graphviz Diagram":
    st.subheader("Graphviz Hierarchical Diagram")
    diagram = create_graphviz_diagram()
    st.image(diagram.render(filename='/tmp/graphviz_output', format='png'), use_column_width=True)
    components.html(fullscreen_button, height=100)
    
# Add New Agent
st.sidebar.subheader("Add New Agent")
new_agent_name = st.sidebar.text_input("Agent Name")
new_agent_manager = st.sidebar.selectbox("Select Manager", ["Operation Manager", "Finance Manager", "Support Manager", 
                                                          "HR Manager", "IT Manager", "Sales Manager", 
                                                          "Marketing Manager", "Product Manager", "Operations Manager"])
new_agent_tasks = st.sidebar.text_area("Tasks (comma-separated)").split(",")
if st.sidebar.button("Add Agent"):
    if new_agent_name and new_agent_manager and new_agent_tasks:
        new_agent = {
            "name": new_agent_name,
            "manager": new_agent_manager,
            "tasks": [task.strip() for task in new_agent_tasks]
        }
        agents.append(new_agent)
        st.sidebar.success(f"New agent {new_agent_name} added under {new_agent_manager} manager.")

# Export as PDF/JSON (Optional as required)
