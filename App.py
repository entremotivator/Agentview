import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph
import streamlit.components.v1 as components

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
        "Operation Manager": "Responsibilities:\n- Oversee daily operations\n- Coordinate with all departments\n- Task execution and delivery",
        "Finance Manager": "Responsibilities:\n- Budget allocation and analysis\n- Financial planning\n- Reporting and forecasting",
        "Support Manager": "Responsibilities:\n- Customer support and satisfaction\n- Troubleshooting and resolving issues\n- Managing feedback"
    }

    for manager, details in managers.items():
        diagram.node(manager, f"{manager}\n\n{details}", shape="rectangle", style="filled", fillcolor="lightgrey")
        diagram.edge("Super Agent Team", manager)

    # Add sub-agents for each manager with detailed tasks
    sub_agents = {
        "Operation Manager": [
            {"name": "Task Executor", "tasks": ["Execute daily tasks", "Monitor KPIs", "Prepare status reports"]},
            {"name": "Coordinator", "tasks": ["Coordinate with other departments", "Manage scheduling", "Resolve conflicts"]}
        ],
        "Finance Manager": [
            {"name": "Budget Analyst", "tasks": ["Analyze financial statements", "Prepare budget reports", "Forecast future financial needs"]},
            {"name": "Account Manager", "tasks": ["Reconcile accounts", "Track expenses", "Generate financial reports"]}
        ],
        "Support Manager": [
            {"name": "Customer Liaison", "tasks": ["Handle customer inquiries", "Resolve complaints", "Monitor service quality"]},
            {"name": "Support Specialist", "tasks": ["Assist customers", "Update FAQs", "Provide technical support"]}
        ]
    }

    for manager, agents in sub_agents.items():
        for agent in agents:
            task_details = "\n".join(agent["tasks"])
            diagram.node(agent["name"], f"{agent['name']}\n\n{task_details}", shape="ellipse", style="filled", fillcolor="lightyellow")
            diagram.edge(manager, agent["name"])

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

# Customization Features
st.sidebar.header("Customize Your Team Structure")
if st.sidebar.checkbox("Add New Team Member"):
    new_team_member = st.sidebar.text_input("Enter Team Member Name")
    new_responsibilities = st.sidebar.text_area("Enter Responsibilities")
    if st.sidebar.button("Add Member"):
        st.write(f"Added Team Member: {new_team_member}")
        st.write(f"Responsibilities:\n{new_responsibilities}")

if st.sidebar.checkbox("Add New Sub-Agent"):
    manager_name = st.sidebar.selectbox("Select Manager", ["Operation Manager", "Finance Manager", "Support Manager"])
    new_sub_agent_name = st.sidebar.text_input("Enter Sub-Agent Name")
    new_sub_agent_tasks = st.sidebar.text_area("Enter Sub-Agent Tasks (separate tasks with commas)").split(",")
    if st.sidebar.button("Add Sub-Agent"):
        st.write(f"Added Sub-Agent under {manager_name}: {new_sub_agent_name}")
        st.write(f"Tasks:\n" + "\n".join([task.strip() for task in new_sub_agent_tasks]))
