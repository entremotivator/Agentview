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
    return G

# Function to render a Graphviz diagram
def create_graphviz_diagram():
    diagram = Digraph("Super Agent Team", format="png")
    diagram.attr(rankdir="TB", size="15", style="filled", bgcolor="white")

    # Add main node
    diagram.node("Super Agent Team", "Super Agent Team", shape="rectangle", style="filled", fillcolor="lightblue")

    # Add managers and their responsibilities
    managers = {
        "Operation Manager": "Responsibilities:\n- Oversee daily operations\n- Coordinate with all departments\n- Task execution and delivery",
        "Finance Manager": "Responsibilities:\n- Budget allocation and analysis\n- Financial planning\n- Reporting and forecasting",
        "Support Manager": "Responsibilities:\n- Customer support and satisfaction\n- Troubleshooting and resolving issues\n- Managing feedback"
    }

    for manager, details in managers.items():
        diagram.node(manager, f"{manager}\n\n{details}", shape="rectangle", style="filled", fillcolor="lightgrey")
        diagram.edge("Super Agent Team", manager)

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
    
    # Create the diagram container with id="content"
    st.markdown('<div id="content">', unsafe_allow_html=True)
    st.graphviz_chart(diagram.source)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show the diagram in fullscreen
    components.html(fullscreen_button, height=100)

# Form to add a new agent
st.sidebar.header("Add New Agent")
new_agent_name = st.sidebar.text_input("Enter New Agent Name")
new_agent_manager = st.sidebar.selectbox("Select Manager", ["Operation Manager", "Finance Manager", "Support Manager"])
new_agent_tasks = st.sidebar.text_area("Enter Tasks for New Agent (separate tasks with commas)").split(",")
if st.sidebar.button("Add New Agent"):
    new_agent = {
        "name": new_agent_name,
        "manager": new_agent_manager,
        "tasks": [task.strip() for task in new_agent_tasks]
    }
    agents.append(new_agent)
    st.sidebar.success(f"New agent {new_agent_name} added under {new_agent_manager}!")
    st.experimental_rerun()

# Customize and Display Added Agents
st.sidebar.header("Current Agents")
for agent in agents:
    st.sidebar.subheader(agent["name"])
    st.sidebar.write(f"Manager: {agent['manager']}")
    st.sidebar.write("Tasks:")
    for task in agent["tasks"]:
        st.sidebar.write(f"- {task}")

# Export Agents as JSON
st.sidebar.header("Export Agents")
json_export = st.sidebar.button("Export Agents as JSON")
if json_export:
    with open("agents.json", "w") as json_file:
        json.dump(agents, json_file, indent=4)
    st.sidebar.success("Agents exported as agents.json!")

# Export Agents as PDF
st.sidebar.header("Export Agents as PDF")
pdf_export = st.sidebar.button("Export Agents as PDF")
if pdf_export:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Super Agent Team", ln=True, align="C")
    pdf.ln(10)

    for agent in agents:
        pdf.cell(200, 10, txt=f"Agent: {agent['name']}", ln=True)
        pdf.cell(200, 10, txt=f"Manager: {agent['manager']}", ln=True)
        pdf.cell(200, 10, txt="Tasks:", ln=True)
        for task in agent["tasks"]:
            pdf.cell(200, 10, txt=f"- {task}", ln=True)
        pdf.ln(5)

    pdf.output("agents.pdf")
    st.sidebar.success("Agents exported as agents.pdf!")

# Import Agents from JSON
st.sidebar.header("Import Agents")
uploaded_file = st.sidebar.file_uploader("Choose a JSON file", type=["json"])
if uploaded_file is not None:
    try:
        imported_agents = json.load(uploaded_file)
        agents.extend(imported_agents)
        st.sidebar.success("Agents imported successfully!")
        st.experimental_rerun()
    except json.JSONDecodeError:
        st.sidebar.error("Failed to decode JSON file.")
