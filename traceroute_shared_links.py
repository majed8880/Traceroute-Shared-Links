import subprocess
import re
import platform
import tkinter as tk
from tkinter import messagebox
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def run_traceroute(hostname):
    if platform.system() == "Windows":
        command = ['tracert', hostname]
        hop_regex = r'\s+(\d+\.\d+\.\d+\.\d+)'
    else:
        command = ['traceroute', hostname]
        hop_regex = r'\s+(\d+\.\d+\.\d+\.\d+)'

    hops = []
    try:
        traceroute_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        for line in iter(traceroute_process.stdout.readline, ''):
            hops += re.findall(hop_regex, line)
            trace_output.insert(tk.END, line)
            trace_output.see(tk.END)
            trace_output.update_idletasks()

        traceroute_process.stdout.close()
        traceroute_process.wait()

    except Exception as e:
        logging.error("Error running traceroute command: %s", e)
        return []

    return hops

def find_shared_links(traceroutes):
    shared_links = set(traceroutes[0])
    for traceroute in traceroutes[1:]:
        shared_links.intersection_update(traceroute)
    return shared_links

def on_submit():
    hostname = entry_hostname.get()
    num_traceroutes_str = entry_num_traceroutes.get()

    if not hostname or not num_traceroutes_str:
        messagebox.showerror("Error", "Please fill in both fields.")
        return

    try:
        num_traceroutes = int(num_traceroutes_str)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for the number of traceroutes. Please enter an integer.")
        return
    def run_traceroutes_and_show_results():
        traceroutes = [run_traceroute(hostname) for _ in range(num_traceroutes)]
        shared_links = find_shared_links(traceroutes)

        result = "Shared links between multiple traceroute responses:\n"
        if shared_links:
            result += "\n".join(shared_links)
        else:
            result += "No shared links found."

        messagebox.showinfo("Result", result)

    traceroute_thread = threading.Thread(target=run_traceroutes_and_show_results)
    traceroute_thread.start()

def create_gui():
    global entry_hostname, entry_num_traceroutes, trace_output
    root = tk.Tk()
    root.title("Traceroute Shared Links")

    tk.Label(root, text="Hostname:").grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="e")
    entry_hostname = tk.Entry(root)
    entry_hostname.grid(row=0, column=1, padx=(0, 20), pady=(20, 0))

    tk.Label(root, text="Number of Traceroutes:").grid(row=1, column=0, padx=(20, 0), pady=(10, 0), sticky="e")
    entry_num_traceroutes = tk.Entry(root)
    entry_num_traceroutes.grid(row=1, column=1, padx=(0, 20), pady=(10, 0))

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=(20, 20))

    trace_output = tk.Text(root, wrap=tk.WORD)
    trace_output.grid(row=3, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
