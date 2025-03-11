import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

# Data for the animation
milestones = [
    {"year": "1960s", "achievement": "First LED dot matrix displays"},
    {"year": "1970s", "achievement": "First fiber optic transmitters and receivers"},
    {"year": "1990s", "achievement": "First single-chip DOCSIS cable modem"},
    {"year": "2008", "achievement": "World’s smallest RF amplifier with WaferCap technology"},
    {"year": "2023", "achievement": "First 5nm 100G/lane Optical PAM-4 DSP PHY and neural network switch"}
]

# Colors for dynamic styling
colors = ["#ff6f61", "#6b5b95", "#88b04b", "#f7cac9", "#92a8d1"]
background_colors = ["#1e1e2f", "#282c34", "#2c3e50", "#34495e", "#212f3d"]

# Setting up the figure
fig, ax = plt.subplots()
fig.set_facecolor(random.choice(background_colors))
ax.set_facecolor(random.choice(background_colors))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

text_elements = []

# Initialize the animation
def init():
    for _ in milestones:
        text = ax.text(5, 5, "", color="white", fontsize=12, ha="center", va="center", alpha=0)
        text_elements.append(text)
    return text_elements

# Update function for animation
def update(frame):
    if frame < len(milestones):
        milestone = milestones[frame]
        text = text_elements[frame]
        text.set_text(f"{milestone['year']}:\n{milestone['achievement']}")
        text.set_alpha(1)
        text.set_fontsize(14)
        text.set_color(random.choice(colors))
        text.set_position((5 + random.uniform(-1, 1), 7 - frame * 1.5))  # Dynamic placement
        ax.set_facecolor(random.choice(background_colors))  # Dynamic background change
    return text_elements

# Create the animation
ani = FuncAnimation(
    fig, update, frames=len(milestones), init_func=init, interval=2000, repeat=False
)

# Save as a GIF or display
plt.show()
