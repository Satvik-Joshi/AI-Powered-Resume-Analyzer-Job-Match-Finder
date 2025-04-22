# main.py

import tkinter as tk
from tkinter import messagebox, scrolledtext
from resume_analyzer import calculate_match_score

def analyze():
    resume_text = resume_input.get("1.0", tk.END)
    job_text = job_input.get("1.0", tk.END)

    if not resume_text.strip() or not job_text.strip():
        messagebox.showwarning("Input Error", "Please enter both Resume and Job Description.")
        return

    score, missing = calculate_match_score(resume_text, job_text)

    result_label.config(text=f"Match Score: {score}%")
    missing_label.config(text="Missing Keywords: " + ", ".join(missing))

# GUI Window
window = tk.Tk()
window.title("Resume Analyzer + Job Match")
window.geometry("700x600")

title = tk.Label(window, text="Resume Analyzer + Job Match", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Resume input
tk.Label(window, text="Paste Resume Text:", font=("Arial", 12)).pack()
resume_input = scrolledtext.ScrolledText(window, height=10, wrap=tk.WORD)
resume_input.pack(padx=10, pady=5, fill=tk.BOTH)

# Job description input
tk.Label(window, text="Paste Job Description:", font=("Arial", 12)).pack()
job_input = scrolledtext.ScrolledText(window, height=10, wrap=tk.WORD)
job_input.pack(padx=10, pady=5, fill=tk.BOTH)

# Analyze button
analyze_button = tk.Button(window, text="Analyze Match", command=analyze, bg="blue", fg="white", font=("Arial", 12))
analyze_button.pack(pady=10)

# Results
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

missing_label = tk.Label(window, text="", font=("Arial", 12), wraplength=650, justify="left")
missing_label.pack(pady=5)

window.mainloop()
