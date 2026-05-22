import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

# ==============================================================================
# NATURE PORTFOLIO ARTWORK CONFIGURATION (Arial/Sans-serif, 5-8 pt font size)
# ==============================================================================
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'sans-serif']
plt.rcParams['font.size'] = 7
plt.rcParams['axes.labelsize'] = 8
plt.rcParams['axes.titlesize'] = 8
plt.rcParams['xtick.labelsize'] = 6
plt.rcParams['ytick.labelsize'] = 6
plt.rcParams['legend.fontsize'] = 6
plt.rcParams['figure.titlesize'] = 8
plt.rcParams['pdf.fonttype'] = 42  # Embed fonts as TrueType in PDF

# Professional Colorblind-Friendly Palette
C_PRIOR = '#1F77B4'      # Muted Slate Blue
C_BCI = '#FF7F0E'        # Muted High-Contrast Orange
C_HUMAN = '#2CA02C'      # Soft Green
C_DARK = '#2C3E50'       # Deep Charcoal
C_LIGHT = '#F8F9FA'      # Soft Warm White
C_SHADOW = '#E2E8F0'     # Light Muted Gray
C_ALERT = '#D9534F'      # Soft Alert Red (paired with blue, not green, for colorblindness)

def draw_rounded_box(ax, x, y, width, height, title, subtitle, color, text_color='white'):
    """Utility to draw professional diagram boxes with high-contrast text."""
    box = patches.FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        facecolor=color, edgecolor='none', alpha=0.9
    )
    ax.add_patch(box)
    
    # Shadow box for a 3D depth effect
    shadow = patches.FancyBboxPatch(
        (x + 0.01, y - 0.01), width, height,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        facecolor=C_SHADOW, edgecolor='none', zorder=box.zorder - 1
    )
    ax.add_patch(shadow)
    
    # Title Text
    ax.text(
        x + width/2.0, y + height*0.6, title,
        color=text_color, fontweight='bold', fontsize=7,
        ha='center', va='center'
    )
    # Subtitle Text
    ax.text(
        x + width/2.0, y + height*0.25, subtitle,
        color=text_color, fontsize=5.5, style='italic',
        ha='center', va='center'
    )

def draw_arrow(ax, x1, y1, x2, y2, color='#7F8C8D', label=None):
    """Draw clean flow arrows."""
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>", color=color, lw=1.2,
            mutation_scale=8, shrinkA=2, shrinkB=2
        )
    )
    if label:
        ax.text(
            (x1 + x2)/2.0, (y1 + y2)/2.0 + 0.02, label,
            color=C_DARK, fontsize=5, ha='center', va='bottom'
        )

# ==============================================================================
# FIGURE 1: THE CONNECTOME-BCI-HUMAN TRIAD PIPELINE
# ==============================================================================
def generate_figure_1():
    print("Generating Figure 1...")
    fig, ax = plt.subplots(figsize=(7.2, 3.8)) # 183 mm (double column)
    ax.set_xlim(0, 2.2)
    ax.set_ylim(0, 1.2)
    ax.axis('off')

    # Panel Label
    ax.text(0.02, 1.15, 'a', fontsize=10, fontweight='bold', ha='left', va='top')

    # 1. PREOPERATIVE CONNECTOMICS COLUMN
    ax.text(0.3, 1.1, 'I. Preoperative Structural Priors', fontsize=7, fontweight='bold', color=C_DARK, ha='center')
    draw_rounded_box(ax, 0.05, 0.75, 0.5, 0.22, "Structural Connectomics", "DTI & Structural fMRI", C_PRIOR)
    draw_rounded_box(ax, 0.05, 0.45, 0.5, 0.22, "Hodotopical Network Prior", "Node-Link Graph & FA Maps", C_PRIOR)
    draw_arrow(ax, 0.3, 0.75, 0.3, 0.67)

    # 2. INTRAOPERATIVE PIPELINE (SaMD DASHBOARD)
    ax.text(1.1, 1.1, 'II. Software-as-a-Medical-Device (SaMD) Processing', fontsize=7, fontweight='bold', color=C_DARK, ha='center')
    draw_rounded_box(ax, 0.85, 0.75, 0.5, 0.22, "Passive Cortical Mapping", "High-Gamma ECoG Decoding", C_BCI)
    draw_rounded_box(ax, 0.85, 0.45, 0.5, 0.22, "Active Subcortical Interrogation", "High-Frequency Monopolar DES", C_BCI)
    
    # Core Fusion Hub
    draw_rounded_box(ax, 0.85, 0.05, 0.5, 0.25, "Computational Fusion Engine", "Viscoelastic Brain Shift & ACAR Filters", C_DARK)
    
    # 3. INTER-COLUMN DATA FLOW
    # Flow from Priors to Fusion Engine
    draw_arrow(ax, 0.35, 0.45, 0.85, 0.2, C_PRIOR, "Structural Prior")
    # Flow from sensors to Fusion Engine
    draw_arrow(ax, 1.1, 0.75, 1.1, 0.67)
    draw_arrow(ax, 1.1, 0.45, 1.1, 0.3)

    # 4. SURGEON HUD FEEDBACK LOOP
    ax.text(1.9, 1.1, 'III. Surgeon HUD Integration', fontsize=7, fontweight='bold', color=C_DARK, ha='center')
    draw_rounded_box(ax, 1.65, 0.45, 0.5, 0.25, "Augmented Reality HUD", "Microscope Spatial Overlays", C_HUMAN)
    
    # Surgeon Action Box
    draw_rounded_box(ax, 1.65, 0.05, 0.5, 0.25, "Adaptive Human Controller", "Safe Microsurgical Resection", C_HUMAN)

    # Flows to final surgical action loop
    draw_arrow(ax, 1.35, 0.17, 1.65, 0.17, C_DARK, "Adaptive Bounds")
    draw_arrow(ax, 1.9, 0.45, 1.9, 0.3)
    
    # Complete closed-loop arrow pointing back to subcortical mapping
    path_data = [
        (Path.MOVETO, (1.9, 0.05)),
        (Path.CURVE3, (1.5, -0.15)),
        (Path.CURVE3, (1.1, 0.45))
    ]
    codes, verts = zip(*path_data)
    codes, verts = zip(*path_data)
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor=C_HUMAN, lw=1.2, ls='--')
    ax.add_patch(patch)
    ax.text(1.5, -0.04, "Sub-millisecond Feedback Loop", color=C_HUMAN, fontsize=5, ha='center')

    plt.tight_layout()
    plt.savefig('figure_1.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figure_1.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

# ==============================================================================
# FIGURE 2: REAL-TIME ARTIFACT SUPPRESSION AND HIGH-GAMMA DECODING
# ==============================================================================
def generate_figure_2():
    print("Generating Figure 2...")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 4.5), sharex=True) # 183 mm (double column)
    
    t = np.linspace(0, 1.0, 1200) # 1 second of data
    
    # Simulate a baseline physiological local field potential (Beta-oscillation)
    lfp_base = 0.8 * np.sin(2 * np.pi * 15 * t)
    
    # Simulate high-gamma motor execution burst (70-150 Hz) appearing mid-record
    hg_burst = np.zeros_like(t)
    burst_mask = (t >= 0.3) & (t <= 0.8)
    hg_burst[burst_mask] = 0.45 * np.sin(2 * np.pi * 95 * t[burst_mask]) * np.sin(np.pi * (t[burst_mask] - 0.3) / 0.5)
    
    clean_signal = lfp_base + hg_burst
    
    # Simulate a high-amplitude electrodiathermy EMI noise burst (350 Hz)
    diathermy_noise = np.zeros_like(t)
    noise_mask = (t >= 0.2) & (t <= 0.6)
    diathermy_noise[noise_mask] = 4.0 * np.sin(2 * np.pi * 320 * t[noise_mask])
    
    # Combine signals
    noisy_signal = clean_signal + diathermy_noise

    # Panel Label inside Subplots
    ax1.text(0.01, 1.15, 'b', transform=fig.transFigure, fontsize=10, fontweight='bold', ha='left', va='top')

    # Top Plot - Raw Corrupted Signal
    ax1.plot(t * 1000, noisy_signal, color=C_ALERT, lw=0.6, alpha=0.8, label="Corrupted ECoG Channel (Diathermy EMI)")
    ax1.set_ylabel("Amplitude ($\mu$V)", fontweight='bold')
    ax1.set_title("Live Electrophysiological Stream experiencing High-Frequency Interference", fontsize=8, color=C_DARK)
    ax1.legend(loc="upper right", frameon=True, facecolor='white', edgecolor='none')
    ax1.grid(True, ls=':', alpha=0.5)
    ax1.set_ylim(-5, 5)

    # Highlight the interference segment
    ax1.axvspan(200, 600, color=C_SHADOW, alpha=0.3)
    ax1.text(400, 3.5, "Active Surgical Diathermy Burst", color=C_DARK, fontsize=6, fontweight='bold', ha='center')

    # Bottom Plot - Cleaned Signal following ACAR and ICA scrubbing
    # Simulate recovered signal (perfectly processed)
    recovered_signal = clean_signal
    ax2.plot(t * 1000, recovered_signal, color=C_PRIOR, lw=0.6, label="Cleaned Signal (ACAR + ICA Filter)")
    
    # Envelope extraction to demonstrate real-time high-gamma power thresholding
    hg_envelope = np.zeros_like(t)
    hg_envelope[burst_mask] = 0.45 * np.sin(np.pi * (t[burst_mask] - 0.3) / 0.5)
    ax2.plot(t * 1000, hg_envelope + 1.2, color=C_BCI, lw=1.0, ls='-', label="High-Gamma Amplitude Envelope")
    
    # Visual Threshold Warning Indicator
    ax2.axhline(1.5, color=C_ALERT, ls='--', lw=0.8, alpha=0.7)
    ax2.text(1050, 1.55, "Eloquence Detection Threshold", color=C_ALERT, fontsize=5.5, ha='right')

    ax2.set_ylabel("Amplitude ($\mu$V)", fontweight='bold')
    ax2.set_xlabel("Time (milliseconds)", fontweight='bold')
    ax2.set_title("Scrubbed Electrodes with High-Gamma (70-150 Hz) Envelope Detection", fontsize=8, color=C_DARK)
    ax2.legend(loc="upper right", frameon=True, facecolor='white', edgecolor='none')
    ax2.grid(True, ls=':', alpha=0.5)
    ax2.set_ylim(-2.0, 2.5)

    # Annotate Eloquent Boundary Detection State
    ax2.annotate(
        "Eloquent Boundary Violation\nResection Halted Automatically",
        xy=(550, 1.6), xytext=(350, 2.1),
        arrowprops=dict(facecolor=C_DARK, shrink=0.05, width=1, headwidth=4, headlength=4),
        fontsize=6, color=C_DARK, fontweight='bold',
        bbox=dict(boxstyle="square,pad=0.3", fc="#FFF2F2", ec=C_ALERT, lw=0.8)
    )

    plt.tight_layout()
    plt.savefig('figure_2.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figure_2.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

# ==============================================================================
# FIGURE 3: BIOMECHANICAL BRAIN SHIFT COMPENSATION
# ==============================================================================
def generate_figure_3():
    print("Generating Figure 3...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.8)) # 183 mm (double column)
    
    # Create grid mesh representing regular tissue spacing
    x = np.linspace(0, 10, 15)
    y = np.linspace(0, 10, 15)
    X, Y = np.meshgrid(x, y)
    
    # Panel Label
    ax1.text(0.01, 1.15, 'c', transform=fig.transFigure, fontsize=10, fontweight='bold', ha='left', va='top')

    # Deform grid using Gaussian displacement mapping to model dural opening cavity collapse
    # Center of resection-induced shift is around coordinates (5.0, 5.0)
    cx, cy = 5.0, 5.0
    sigma = 3.5  # Decay constant of deformation
    magnitude = 1.6 # Severe 1.6 cm displacement mapping
    
    dx = -magnitude * np.exp(-((X - cx)**2 + (Y - cy)**2) / (2 * sigma**2)) * (X - cx) / sigma
    dy = -magnitude * np.exp(-((X - cx)**2 + (Y - cy)**2) / (2 * sigma**2)) * (Y - cy) / sigma
    
    X_deformed = X + dx
    Y_deformed = Y + dy

    # 1. SUBPLOT 1: Standard Rigid Stereotaxy Fallacy (Uncompensated coordinates)
    ax1.set_title("A. Rigid Stereotactic Navigation (Uncompensated)", fontsize=8, fontweight='bold', color=C_DARK)
    
    # Draw non-deformed reference grids representing pre-operative MRI assumption
    for i in range(len(x)):
        ax1.plot(X[i, :], Y[i, :], color=C_SHADOW, lw=0.5, ls='--')
        ax1.plot(X[:, i], Y[:, i], color=C_SHADOW, lw=0.5, ls='--')
    
    # Draw actual shifted pathways in light solid lines to show underlying real tissue shift
    for i in range(len(x)):
        ax1.plot(X_deformed[i, :], Y_deformed[i, :], color='#CBD5E1', lw=0.6, alpha=0.5)
        ax1.plot(X_deformed[:, i], Y_deformed[:, i], color='#CBD5E1', lw=0.6, alpha=0.5)

    # Plot targets
    ax1.plot(cx, cy, marker='*', color=C_PRIOR, markersize=10, label="True Target (Pre-op coordinate)")
    ax1.plot(cx - 1.2, cy - 1.2, marker='*', color=C_ALERT, markersize=10, label="Shifted Physical Target")
    
    # Draw uncompensated straight robotic path based on pre-operative assumptions
    ax1.plot([1.0, cx], [9.0, cy], color=C_ALERT, lw=1.5, ls='-', label="Rigid Pathway")
    ax1.text(3.5, 7.5, "Trajectory Error\n(Targets Misaligned)", color=C_ALERT, fontsize=6, fontweight='bold', ha='center')

    ax1.set_xlim(-1, 11)
    ax1.set_ylim(-1, 11)
    ax1.axis('off')
    ax1.legend(loc="lower left", frameon=True, facecolor='white', edgecolor='none')

    # 2. SUBPLOT 2: Biot's Poroelastic FEM Corrected Space
    ax2.set_title("B. Biot's Poroelastic FEM Reconstruction", fontsize=8, fontweight='bold', color=C_DARK)
    
    # Draw deformed grid layers representing the dynamically registered brain volume
    for i in range(len(x)):
        ax2.plot(X_deformed[i, :], Y_deformed[i, :], color=C_DARK, lw=0.7)
        ax2.plot(X_deformed[:, i], Y_deformed[:, i], color=C_DARK, lw=0.7)

    # Plot True Target
    ax2.plot(cx - 1.2, cy - 1.2, marker='*', color=C_HUMAN, markersize=10, label="Compensated Target Position")
    
    # Dynamic SaMD HUD Corrected Path (Curved Trajectory following deformation field)
    # Generate mock corrected curve tracing tissue vectors
    curve_x = np.linspace(1.0, cx - 1.2, 100)
    curve_y = 9.0 - (9.0 - (cy - 1.2)) * np.sin(np.pi * (curve_x - 1.0) / (2 * (cx - 2.2)))
    ax2.plot(curve_x, curve_y, color=C_HUMAN, lw=1.5, ls='-', label="SaMD HUD Corrected Pathway")
    ax2.text(2.2, 7.8, "Warped Spatial Mesh\nTracks Shift Vectors", color=C_HUMAN, fontsize=6, fontweight='bold')

    ax2.set_xlim(-1, 11)
    ax2.set_ylim(-1, 11)
    ax2.axis('off')
    ax2.legend(loc="lower left", frameon=True, facecolor='white', edgecolor='none')

    plt.tight_layout()
    plt.savefig('figure_3.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figure_3.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_figure_1()
    generate_figure_2()
    generate_figure_3()
    print("All figures successfully generated as vector PDFs!")