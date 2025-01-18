import streamlit as st

# Extended Mermaid.js diagram
diagram_code = """
%%{init: {'theme': 'default', 'themeVariables': {'primaryColor': '#1f77b4', 'edgeLabelBackground':'#ffffff', 'tertiaryColor': '#e3e3e3'}}}%%
graph TB
    A[Super Agent Team]:::main --> B[Operation Manager]:::manager
    A --> C[Finance Manager]:::manager
    A --> D[Support Manager]:::manager
    
    B --> B1[Task Executor]:::employee
    B --> B2[Data Analyst]:::employee
    B --> B3[Schedule Manager]:::employee
    B --> B4[AI Agent 1 - Operational Support]:::ai
    B --> B5[AI Agent 2 - Data Analysis]:::ai
    
    C --> C1[Budget Analyst]:::employee
    C --> C2[Account Manager]:::employee
    C --> C3[Tax Consultant]:::employee
    C --> C4[AI Agent 3 - Financial Insights]:::ai
    C --> C5[AI Agent 4 - Tax Compliance]:::ai
    
    D --> D1[Customer Liaison]:::employee
    D --> D2[Help Desk Agent]:::employee
    D --> D3[Feedback Specialist]:::employee
    D --> D4[AI Agent 5 - Customer Relations]:::ai
    D --> D5[AI Agent 6 - Feedback Analysis]:::ai

    classDef main fill:#1f77b4,stroke:#333,stroke-width:2px,font-size:18px,color:#ffffff;
    classDef manager fill:#ffcc00,stroke:#333,stroke-width:2px,font-size:16px,color:#333;
    classDef employee fill:#66c2a5,stroke:#333,stroke-width:1px,font-size:14px,color:#333;
    classDef ai fill:#a6d854,stroke:#333,stroke-width:1px,font-size:14px,color:#333;
"""

# Streamlit App
st.set_page_config(page_title="Super Agent Team Chart", layout="wide")
st.title("Super Agent Team Chart")
st.write("A detailed and extended team hierarchy with AI agents displayed using Mermaid.js.")

# Display the diagram
st.markdown(
    f"""
    ```mermaid
    {diagram_code}
    ```
    """,
    unsafe_allow_html=True,
)




