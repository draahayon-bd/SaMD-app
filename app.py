import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# GLOBAL THEME & SETUP
# ---------------------------------------------------------
st.set_page_config(page_title="Connectome-BCI Master Engine", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main {background-color: #0E1117;}
    h1, h2, h3 {color: #E0E0E0;}
    .stMetric {background-color: #161A22; padding: 15px; border-radius: 8px; border: 1px solid #262D3D;}
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation System
st.sidebar.title("🎛️ Navigation Hub")
app_mode = st.sidebar.selectbox("Select Active Framework Subsystem:", 
    ["1. Comparative Surgical Framework", 
     "2. Connectome Signal Rerouting Graph", 
     "3. Triad Architecture Simulator", 
     "4. Intraoperative Mapping Engine",
     "5. Full System Dashboard Simulator"]) # <-- Added the 5th Option

st.sidebar.markdown("---")

# =========================================================
# SUBSYSTEM 1: COMPARATIVE SURGICAL FRAMEWORK (BCI VS ROBOTICS)
# =========================================================
if app_mode == "1. Comparative Surgical Framework":
    st.title("Surgical Framework: BCI vs. Robotics")
    st.markdown("##### Pipeline Analysis: BCI-Human maintains high fidelity across variable operational terrains.")
    
    st.sidebar.subheader("Terrain Settings")
    econ_setting = st.sidebar.selectbox("Economic Setting", ["High-Income", "Middle-Income", "Low-Income"], index=1)
    shift_severity = st.sidebar.slider("Brain Shift Severity", 1, 5, 2)
    emi_noise = st.sidebar.toggle("Inject Servo EMI Noise", value=False)
    
    cost_savings = "13.5x" if econ_setting == "Low-Income" else ("8.2x" if econ_setting == "Middle-Income" else "3.1x")
    scalability = "9.4x" if econ_setting == "Low-Income" else ("5.7x" if econ_setting == "Middle-Income" else "1.8x")
    shift_impact = "Critical Risk" if shift_severity > 3 else "Moderate"
    
    m1, m2, m3 = st.columns(3)
    m1.metric("COST SAVINGS", cost_savings, "SaMD Frugal Advantage")
    m2.metric("SCALABILITY", scalability, "Hardware-Agnostic Footprint")
    m3.metric("ROBOTIC SHIFT IMPACT", shift_impact, "Viscoelastic Mismatch")
    
    st.markdown("### Operational Metrics Comparison")
    
    rob_access = 85 if econ_setting == "High-Income" else (35 if econ_setting == "Middle-Income" else 5)
    bci_access = 95
    rob_adapt = max(90 - (shift_severity * 15), 10)
    bci_adapt = 95
    rob_snr = max(85 - (45 if emi_noise else 0), 15)
    bci_snr = 92
    
    metrics_label = ['Access (%)', 'Adaptability', 'Preservation', 'SNR (dB)']
    
    fig_bars = go.Figure(data=[
        go.Bar(name='Robotics', x=metrics_label, y=[rob_access, rob_adapt, 65, rob_snr], marker_color='#FF6B6B'),
        go.Bar(name='BCI-Human', x=metrics_label, y=[bci_access, bci_adapt, 95, bci_snr], marker_color='#4A90E2')
    ])
    fig_bars.update_layout(barmode='group', template='plotly_dark', height=400, margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig_bars, width='stretch')
    
    st.markdown("### Tissue Preservation Profile vs. Brain Shift")
    shift_axis = np.linspace(1, 5, 20)
    bci_line = 100 - (shift_axis * 0.5)
    rob_line = 95 - (shift_axis ** 2.1)
    
    fig_grid = go.Figure()
    fig_grid.add_trace(go.Scatter(x=shift_axis, y=bci_line, name='BCI-Human (Optimal Zone)', line=dict(color='#4A90E2', width=3)))
    fig_grid.add_trace(go.Scatter(x=shift_axis, y=rob_line, name='Robotics Platform', line=dict(color='#FF6B6B', width=2, dash='dash')))
    fig_grid.update_layout(template='plotly_dark', height=300, xaxis_title="Brain Shift Severity Index", yaxis_title="Tissue Preservation (%)")
    st.plotly_chart(fig_grid, width='stretch')

# =========================================================
# SUBSYSTEM 2: CONNECTOME-WEIGHTED SIGNAL REROUTING GRAPH
# =========================================================
elif app_mode == "2. Connectome Signal Rerouting Graph":
    st.title("Connectome-Weighted Signal Rerouting")
    
    st.sidebar.subheader("Stunning Simulation")
    stunning_level = st.sidebar.slider("Surgical Stunning at M1 Core (%)", 0, 100, 0)
    
    m1_val = max(88.0 - (stunning_level * 0.8), 5.0)
    pathway_reroute_idx = min(0.12 + (stunning_level * 0.008), 0.98)
    snr_val = max(14.2 - (stunning_level * 0.05), 8.5)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("DECODING ACCURACY", f"{m1_val:.1f}%", "Prior Dominated" if stunning_level > 50 else "Nominal")
    c2.metric("SIGNAL SNR", f"{snr_val:.1f} dB", "Attenuated" if stunning_level > 50 else "Stable")
    c3.metric("PATHWAY REROUTE COEFFICIENT", f"{pathway_reroute_idx:.2f}")
    
    st.markdown("#### Cortical Topographical Network Map")
    
    nodes = {
        'Parietal Assoc.': (1, 2),
        'SMA': (2.5, 3.5),
        'M1 (Core)': (2.5, 2),
        'Premotor': (2.5, 0.5),
        'Decoded Intent': (4, 2)
    }
    
    fig_network = go.Figure()
    
    m1_line_width = max(5 - (stunning_level * 0.05), 0.5)
    reroute_line_width = min(1 + (stunning_level * 0.04), 4.5)
    line_color_m1 = "#4A90E2" if stunning_level < 60 else "#3A4454"
    line_color_alt = "#2CA02C" if stunning_level > 20 else "#5A6578"
    
    paths = [
        ('Parietal Assoc.', 'M1 (Core)', line_color_m1, m1_line_width),
        ('M1 (Core)', 'Decoded Intent', line_color_m1, m1_line_width),
        ('Parietal Assoc.', 'SMA', line_color_alt, reroute_line_width),
        ('SMA', 'Decoded Intent', line_color_alt, reroute_line_width),
        ('Parietal Assoc.', 'Premotor', line_color_alt, reroute_line_width),
        ('Premotor', 'Decoded Intent', line_color_alt, reroute_line_width)
    ]
    
    for p in paths:
        x_coords = [nodes[p[0]][0], nodes[p[1]][0]]
        y_coords = [nodes[p[0]][1], nodes[p[1]][1]]
        fig_network.add_trace(go.Scatter(x=x_coords, y=y_coords, mode='lines+markers', 
            line=dict(color=p[2], width=p[3]), marker=dict(size=1, color="#A1B0CB"), showlegend=False))
        
    nx = [v[0] for v in nodes.values()]
    ny = [v[1] for v in nodes.values()]
    nlabels = list(nodes.keys())
    
    node_colors = ['#222A38', '#222A38', '#FF6B6B' if stunning_level > 40 else '#4A90E2', '#222A38', '#10141D']
    node_sizes = [45, 45, 50, 45, 60]
    
    fig_network.add_trace(go.Scatter(x=nx, y=ny, mode='markers+text', text=nlabels, textposition="bottom center",
        marker=dict(size=node_sizes, color=node_colors, line=dict(width=2, color='#5A6C8C')), 
        textfont=dict(color='#E2E8F0', size=11), showlegend=False))
        
    fig_network.update_layout(template='plotly_dark', height=500, xaxis=dict(visible=False), yaxis=dict(visible=False))
    st.plotly_chart(fig_network, width='stretch')

# =========================================================
# SUBSYSTEM 3: CONNECTOME-BCI TRIAD SIMULATOR
# =========================================================
elif app_mode == "3. Triad Architecture Simulator":
    st.title("Connectome-BCI Triad Simulator")
    st.markdown("##### System Nominal: Data stream synchronized with connectome structural priors.")
    
    t1, t2, t3 = st.columns(3)
    t1.metric("SYSTEM LATENCY", "16.0 ms", "Sub-20ms Latency Budget Enforced")
    t2.metric("HARDWARE CAPITAL OVERHEAD", "$0.00", "Leveraging Existing Institutional Systems")
    t3.metric("MARGIN CONFIDENCE BOUNDARY", "99.0%", "Strict Target Acquisition Tracking")
    
    blocks = {
        'PRE-OP PRIORS\n(DTI/fMRI)': (1, 3),
        'INTRA-OP ECOG\n(High-Gamma)': (1, 1),
        'PROCESSING ENGINE\n(Edge Compute)': (2.5, 2),
        'HUD/FEEDBACK\n(Microscope Overlay)': (4, 2),
        'ACTUATOR\n(Surgeon Hand)': (5.5, 2),
        'BRAIN MARGIN': (4, 0.5)
    }
    
    fig_triad = go.Figure()
    
    triad_edges = [
        ('PRE-OP PRIORS\n(DTI/fMRI)', 'PROCESSING ENGINE\n(Edge Compute)'),
        ('INTRA-OP ECOG\n(High-Gamma)', 'PROCESSING ENGINE\n(Edge Compute)'),
        ('PROCESSING ENGINE\n(Edge Compute)', 'HUD/FEEDBACK\n(Microscope Overlay)'),
        ('HUD/FEEDBACK\n(Microscope Overlay)', 'ACTUATOR\n(Surgeon Hand)'),
        ('ACTUATOR\n(Surgeon Hand)', 'BRAIN MARGIN'),
        ('BRAIN MARGIN', 'HUD/FEEDBACK\n(Microscope Overlay)')
    ]
    
    for edge in triad_edges:
        fig_triad.add_trace(go.Scatter(
            x=[blocks[edge[0]][0], blocks[edge[1]][0]],
            y=[blocks[edge[0]][1], blocks[edge[1]][1]],
            mode='lines', line=dict(color='#4ECDC4', width=2, dash='dot'), showlegend=False))
            
    bx = [v[0] for v in blocks.values()]
    by = [v[1] for v in blocks.values()]
    blabels = list(blocks.keys())
    
    fig_triad.add_trace(go.Scatter(x=bx, y=by, mode='markers+text', text=blabels, textposition="middle center",
        marker=dict(size=70, symbol='square', color='#1E222B', line=dict(width=2, color='#4ECDC4')),
        textfont=dict(color='#FFFFFF', size=10), showlegend=False))
        
    fig_triad.update_layout(template='plotly_dark', height=450, xaxis=dict(visible=False), yaxis=dict(visible=False))
    st.plotly_chart(fig_triad, width='stretch')

# =========================================================
# SUBSYSTEM 4: INTRAOPERATIVE MAPPING ENGINE
# =========================================================
elif app_mode == "4. Intraoperative Mapping Engine":
    st.title("BCI Surgical Mapping Engine")
    
    st.sidebar.subheader("Instrument Mechanics")
    probe_pos = st.sidebar.slider("Micro-Probe Linear Axis Position", 0.0, 1.0, 0.22)
    
    if probe_pos < 0.35:
        zone_name = "Core Neoplasm"
        gamma_power = "12.4 uV²/Hz"
        safety_metric = "100%"
    elif probe_pos < 0.70:
        zone_name = "Peritumoral Margin"
        gamma_power = "48.2 uV²/Hz"
        safety_metric = "Cautious Boundary"
    else:
        zone_name = "Eloquent Parenchyma"
        gamma_power = "98.1 uV²/Hz"
        safety_metric = "CRITICAL RESECTION HALT"

    h1, h2, h3, h4 = st.columns(4)
    h1.metric("CURRENT TISSUE DOMAIN", zone_name)
    h2.metric("HIGH-GAMMA SYNCHRONIZATION", gamma_power)
    h3.metric("SAFETY PROFILE VALIDATION", safety_metric)
    h4.metric("TELEMETRY LATENCY", "16.0 ms")
    
    st.markdown("#### Real-Time Spatial Verification Interface")
    fig_spatial = go.Figure()
    
    fig_spatial.add_vrect(x0=0.0, x1=0.35, fillcolor="rgba(214, 39, 40, 0.15)", layer="below", line_width=1, annotation_text="Core Neoplasm (Safe Excision Zone)")
    fig_spatial.add_vrect(x0=0.35, x1=0.70, fillcolor="rgba(255, 165, 0, 0.15)", layer="below", line_width=1, annotation_text="Peritumoral Margin Boundary")
    fig_spatial.add_vrect(x0=0.70, x1=1.0, fillcolor="rgba(44, 160, 44, 0.15)", layer="below", line_width=1, annotation_text="Eloquent Parenchyma (Functional Halt)")
    
    fig_spatial.add_vline(x=probe_pos, line_width=3, line_color="#FFFFFF")
    fig_spatial.add_trace(go.Scatter(x=[probe_pos], y=[0.5], mode='markers', marker=dict(size=20, color='#FFFFFF', symbol='diamond'), name='Probe Tip'))
    
    fig_spatial.update_layout(template='plotly_dark', height=250, xaxis=dict(range=[0, 1]), yaxis=dict(visible=False))
    st.plotly_chart(fig_spatial, width='stretch')
    
    st.markdown("#### Real-Time Live High-Gamma Subcortical Signal Trace")
    time_series = np.linspace(0, 10, 500)
    
    if zone_name == "Core Neoplasm":
        wave_stream = np.random.normal(0, 0.15, 500)
    elif zone_name == "Peritumoral Margin":
        wave_stream = np.sin(2 * np.pi * 2 * time_series) * 0.4 + np.random.normal(0, 0.2, 500)
    else:
        wave_stream = np.sin(2 * np.pi * 5 * time_series) * 0.9 + np.random.normal(0, 0.1, 500)
        
    fig_wave = go.Figure()
    fig_wave.add_trace(go.Scatter(x=time_series, y=wave_stream, mode='lines', line=dict(color='#5CE1E6', width=1.5)))
    fig_wave.update_layout(template='plotly_dark', height=220, xaxis_title="Time Frame Window (ms)", yaxis_title="Amplitude (μV)", margin=dict(t=10, b=10))
    st.plotly_chart(fig_wave, width='stretch')

# =========================================================
# SUBSYSTEM 5: FULL DASHBOARD SIMULATOR (THE MASTER MERGE)
# =========================================================
elif app_mode == "5. Full System Dashboard Simulator":
    st.title("🧠 Connectome-BCI-Human Triad")
    st.markdown("### Intraoperative Dashboard Simulator | SaMD Prototype v1.0")
    st.markdown("---")

    st.sidebar.subheader("🎛️ Operative Controls")
    stunning_percent = st.sidebar.slider("Surgical Stunning (%)", min_value=0, max_value=100, value=15, step=5)
    diathermy_active = st.sidebar.toggle("Inject Diathermy EMI", value=False)
    probe_depth = st.sidebar.slider("Micro-Probe Depth (mm)", min_value=0, max_value=50, value=0)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📡 Dynamic Connectome-Weighted Priors")
        st.markdown("Real-time redistribution of feature-extraction weights.")
        
        m1_weight = max(85 - stunning_percent, 5)
        distributed_weight = (85 - m1_weight) / 2
        pmc_weight = 8 + distributed_weight
        sma_weight = 7 + distributed_weight

        fig_weights = go.Figure(data=[
            go.Bar(name='Primary Motor (M1)', x=['M1', 'PMC', 'SMA'], y=[m1_weight, 0, 0], marker_color='#FF6B6B'),
            go.Bar(name='Premotor (PMC)', x=['M1', 'PMC', 'SMA'], y=[0, pmc_weight, 0], marker_color='#4ECDC4'),
            go.Bar(name='Supp. Motor (SMA)', x=['M1', 'PMC', 'SMA'], y=[0, 0, sma_weight], marker_color='#45B7D1')
        ])
        
        fig_weights.update_layout(barmode='stack', yaxis=dict(title='Weight (%)', range=[0, 100]), template="plotly_dark", margin=dict(l=0, r=0, t=30, b=0), height=300)
        st.plotly_chart(fig_weights, width='stretch')

    with col2:
        st.subheader("⚡ SaMD Artifact Scrubbing")
        st.markdown("Continuous High-Gamma extraction amidst OR noise.")
        
        time = np.linspace(0, 1, 500)
        baseline_gamma = np.sin(2 * np.pi * 80 * time) * 0.5 + np.random.normal(0, 0.1, 500)
        raw_signal = baseline_gamma.copy()
        
        if diathermy_active:
            raw_signal[200:250] += np.random.normal(0, 5, 50) 
            raw_signal[350:400] += np.random.normal(0, 5, 50)
            
        fig_signal = go.Figure()
        fig_signal.add_trace(go.Scatter(x=time, y=raw_signal, mode='lines', name='Raw Feed', line=dict(color='#FF9999', width=1), opacity=0.6))
        fig_signal.add_trace(go.Scatter(x=time, y=baseline_gamma, mode='lines', name='Scrubbed Telemetry', line=dict(color='#2CA02C', width=2)))
        
        fig_signal.update_layout(xaxis_title="Time (ms)", yaxis_title="Amplitude (μV)", template="plotly_dark", margin=dict(l=0, r=0, t=30, b=0), height=300, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig_signal, width='stretch')

    st.markdown("---")
    st.subheader("⏱️ System Telemetry & Safety Margins")
    m1, m2, m3 = st.columns(3)

    current_latency = np.random.uniform(14.2, 18.7)
    m1.metric("Closed-Loop Latency Budget", f"{current_latency:.1f} ms", "-180 ms vs Human Reaction")
    handshake_status = "Active (White Matter)" if probe_depth > 15 else "Inactive (Cortical Surface)"
    m2.metric("Subcortical DTI Handshake", handshake_status)
    m3.metric("Infrastructure Overhead", "$0.00", "Utilizes Standard Bedside Amplifiers")

    st.caption("Developed by Dr. Md Ahasanul Al Hasib Ayon | Translational Computational Neuroscience")