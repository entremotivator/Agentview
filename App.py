import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Create a simple graph
G = nx.DiGraph()
G.add_edges_from([("Super Agent Team", "Operation Manager"),
                  ("Super Agent Team", "Finance Manager"),
                  ("Super Agent Team", "Support Manager"),
                  ("Operation Manager", "Task Executor"),
                  ("Finance Manager", "Budget Analyst"),
                  ("Support Manager", "Customer Liaison")])

# Plot the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold')
st.pyplot(plt)


