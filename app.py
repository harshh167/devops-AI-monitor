import streamlit as st
from monitor import get_server_metrics
#triggering refresh for pages folder
st.set_page_config(page_title="Enterprise Control Center", page_icon="🌐", layout="wide")


st.markdown("""
    <style>
        .stMetric {background-color: #1e1e2e; padding: 20px; border-radius: 15px; border: 1px solid #31333f;}
        .main {background-color: #0e1117;}
        h1 {color: #ffffff; font-family: 'Inter', sans-serif;}
        .css-1544g2n {padding-top: 1rem;}
    </style>
""", unsafe_allow_html=True)

st.title("🌐 CloudOps Enterprise Command Suite")
st.caption("Centralized Cluster Management Interface | v2.4.0")
st.write("---")

metrics = get_server_metrics()

st.subheader("📊 Live Infrastructure Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("CPU Pool", f"{metrics['cpu']}%", "Stable")
col2.metric("Memory", f"{metrics['ram']}%", "Optimized")
col3.metric("Disk I/O", f"{metrics['disk']}%", "Healthy")
col4.metric("Gateway", metrics['os'].split()[0], "Active")

st.write("---")
st.subheader("🚀 System Readiness")
s1, s2, s3 = st.columns(3)
s1.success("API Mesh: Operational")
s2.success("K8s Engine: Running")
s3.success("Data Sink: Connected")

st.sidebar.title("🔐 Control Panel")
st.sidebar.info(f"**Operator:** Harsh  \n**Session:** {metrics['ip']}")
