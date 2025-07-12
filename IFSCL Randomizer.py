import random
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Game options
game_options = {
    "Startup": {
        "Aelita": ["Lyoko", "Code Earth", "Earth"],
        "Odd": ["Absent", "Normal", "PermaXanafied"],
        "Ulrich": ["Absent", "Normal", "PermaXanafied"],
        "Yumi": ["Absent", "Normal", "PermaXanafied"],
        "William": ["Absent", "Normal", "PermaXanafied"],
        "Fall Rescue": ["Yes", "No"],
        "Lyoko": ["Yes", "No"],
        "XANA Awakening": ["Direct Attack", "Half-Day Delay", "1 Day Delay", "2 Day Delay"],
        "Sector 5 Extras": ["Maze", "GarageSkid", "Skidbladnir"],
        "Virt/Devirt Codes Obtained": ["Yes", "No"],
        "Replika Discovered": ["Yes", "No"],
        "Franz Diary": ["Yes", "No"],
        "Auto Connection": ["None", "Lyoko", "Sector 5"],
        "Tower Program": ["Monoscan", "Superscan"],
        "Avatars": ["Basic", "Upgraded"]
    },
    "General": {
        "Difficulty": ["Relax", "Classic", "Expert"],
        "Battle Turn Speed": ["Low", "Medium", "High", "Very High"],
        "Earth Troubles": ["None", "Low", "Normal", "High"],
        "Simultanious Attacks": ["Yes", "No"],
        "Monster Preservation": ["Yes", "No"],
        "Future Flash": ["Yes", "No"],
        "DNA Fusion": ["None", "Low", "Normal", "High"],
        "DNA Alteration": ["None", "Low", "Normal", "High"]
    },
    "XANA Lyoko": {
        "GarageSkid Attacks": ["None", "Low", "Normal", "High"],
        "Heart of Lyoko Attacks": ["None", "Low", "Normal", "High"],
        "Sector Destruction": ["None", "Low", "Normal", "High"],
        "Virus Scyphozoa": ["None", "Low", "Normal", "High"],
        "DNA Scyphozoa": ["None", "Low", "Normal", "High"],
        "Draining Scyphozoa": ["None", "Low", "Normal", "High"],
        "Guardian": ["None", "Low", "Normal", "High"],
        "Polymorphic Clone": ["None", "Low", "Normal", "High"]
    },
    "XANA Earth": {
        "Tower Attacks": ["None", "Low", "Normal", "High"],
        "Xanification": ["None", "Low", "Normal", "High"],
        "Deadly Swarm": ["None", "Low", "Normal", "High"],
        "Meteor": ["None", "Low", "Normal", "High"],
        "Power Plant Overload": ["None", "Low", "Normal", "High"],
        "Suicide Bus": ["None", "Low", "Normal", "High"]
    }
}

def generate_randomized_settings():
    return {
        category: {
            param: random.choice(choices)
            for param, choices in options.items()
        }
        for category, options in game_options.items()
    }

def export_settings(settings):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    with open(file_path, "w", encoding="utf-8") as file:
        for category, params in settings.items():
            file.write(f"=== {category.upper()} ===\n")
            for param, value in params.items():
                file.write(f"{param}: {value}\n")
            file.write("\n")
    messagebox.showinfo("Export Complete", f"Settings exported to:\n{file_path}")

def show_settings_popup(settings):
    popup = tk.Toplevel(root)
    popup.title("Shuffled Settings")
    popup.geometry("500x600")
    text = tk.Text(popup, wrap="word")
    text.pack(expand=True, fill="both")
    for category, params in settings.items():
        text.insert("end", f"[{category}]\n")
        for param, value in params.items():
            text.insert("end", f"{param}: {value}\n")
        text.insert("end", "\n")
    text.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("IFSCL Randomizer")
root.geometry("400x200")

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

title = ttk.Label(frame, text="IFSCL Randomizer", font=("Arial", 18))
title.pack(pady=10)

def on_shuffle():
    global current_settings
    current_settings = generate_randomized_settings()
    show_settings_popup(current_settings)

def on_export():
    if current_settings:
        export_settings(current_settings)
    else:
        messagebox.showwarning("No Settings", "Please shuffle settings first.")

current_settings = {}

shuffle_btn = ttk.Button(frame, text="🎲 Shuffle Settings", command=on_shuffle)
shuffle_btn.pack(pady=5)

export_btn = ttk.Button(frame, text="💾 Export Settings", command=on_export)
export_btn.pack(pady=5)

exit_btn = ttk.Button(frame, text="❌ Exit", command=root.quit)
exit_btn.pack(pady=5)

root.mainloop()