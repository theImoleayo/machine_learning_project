import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Data for the animation
milestones = [
    {"year": "1960s", "achievement": "First LED dot matrix displays"},
    {"year": "1970s", "achievement": "First fiber optic transmitters and receivers\n"},
    {"year": "1990s", "achievement": "First single-chip DOCSIS cable modem"},
    {"year": "2008", "achievement": "World’s smallest RF amplifier with WaferCap technology"},
    {"year": "2023", "achievement": "First 5nm 100G/lane Optical \n PAM-4 DSP PHY and neural network switch"}
]

# Setting up the figure
fig, ax = plt.subplots()
fig.set_facecolor("#1e1e2f")
ax.set_facecolor("#282c34")
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
        # text.set_text("-------------------------\nBroadcom Inc Dateback to 1961\n-------------------------\n")
        text.set_text(f"{milestone['year']}:\n{milestone['achievement']}")
        text.set_alpha(1)
        text.set_fontsize(14)
        text.set_color("#FFFFFF")
        text.set_position((5, 9 - frame * 2.0))  # Staggered placement for readability
    return text_elements

# Create the animation
ani = FuncAnimation(
    fig, update, frames=len(milestones), init_func=init, interval=2000, repeat=False
)

# Save as a GIF or MP4
ani.save('/home/theimoleayo/ProjectEnvironment/ML Project/animation.gif', writer='imagemagick')
# ani.save('/home/theimoleayo/ProjectEnvironment/ML Project/animation.mp4', writer='ffmpeg')

# Display the animation
plt.show()
