import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import csv
import ctypes
import sys

class PortManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Port Manager")
        
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        self.get_ports_button = tk.Button(button_frame, text="Get Open Ports", command=self.get_open_ports)
        self.get_ports_button.pack(side=tk.LEFT, padx=5)
        
        self.close_app_button = tk.Button(button_frame, text="Close Application", command=self.close_application)
        self.close_app_button.pack(side=tk.LEFT, padx=5)
        
        text_frame = tk.Frame(root)
        text_frame.pack(pady=10)
        
        self.ports_display = scrolledtext.ScrolledText(text_frame, width=150, height=50, wrap=tk.NONE)
        self.ports_display.pack(side=tk.LEFT)
        
        h_scrollbar = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL, command=self.ports_display.xview)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.ports_display.config(xscrollcommand=h_scrollbar.set)
        
        self.port_descriptions = self.load_port_descriptions("resources\\tcp.csv")
        self.service_descriptions = self.load_service_descriptions("resources\\windows.csv")
    
    def load_port_descriptions(self, csv_file):
        port_descriptions = {}
        try:
            with open(csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    port_descriptions[row['port']] = {
                        'description': row['description']
                    }
        except FileNotFoundError:
            messagebox.showerror("Error", f"CSV file {csv_file} not found.")
        return port_descriptions
    
    def load_service_descriptions(self, csv_file):
        service_descriptions = {}
        try:
            with open(csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    service_descriptions[row['Executable Name']] = {
                        'type': row['Type'],
                        'description': row['Description']
                    }
        except FileNotFoundError:
            messagebox.showerror("Error", f"CSV file {csv_file} not found.")
        return service_descriptions
    
    def fetch_service_for_port(self, port):
        return self.port_descriptions.get(port, {"description": "Unknown"})
    
    def get_open_ports(self):
        self.ports_display.delete(1.0, tk.END)
        try:
            result = subprocess.check_output("netstat -ano", shell=True).decode()
            self.add_close_buttons(result)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to get open ports: {e}")
    
    def add_close_buttons(self, result):
        lines = result.splitlines()
        self.ports_display.insert(tk.END, f"{'        Local Address':<25} {'      Foreign Address':<25} {'            State':<15} {'          PID':<10} {'            Service':<20}\n")
        self.ports_display.insert(tk.END, "-"*125 + "\n")
        for line in lines:
            if "LISTENING" in line:
                parts = line.split()
                local_address = parts[1]
                foreign_address = parts[2]
                state = parts[3]
                pid = parts[4]
                port = local_address.split(':')[-1]
                service_info = self.fetch_service_for_port(port)
                service = self.get_service_name_by_pid(pid)
                
                close_button = tk.Button(self.ports_display, text=f"Close {port}", command=lambda p=pid: self.close_port(p), width=10)
                self.ports_display.window_create(tk.END, window=close_button)
                self.ports_display.insert(tk.END, f"{local_address:<25} {foreign_address:<25} {state:<15} {pid:<10} {service:<20}\n")
        
    def get_service_name_by_pid(self, pid):
        try:
            result = subprocess.check_output(f"tasklist /FI \"PID eq {pid}\"", shell=True).decode()
            lines = result.splitlines()
            if len(lines) > 3:
                executable_name = lines[3].split()[0]
                service_info = self.service_descriptions.get(executable_name, {"type": "Unknown", "description": "Unknown"})
                return f"{service_info['type']}: {service_info['description']}"
            else:
                return "(Unknown)"
        except subprocess.CalledProcessError:
            return "(Unknown)"

    def close_port(self, pid):
        try:
            result = subprocess.run(f"taskkill /PID {pid} /F", shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, result.args, output=result.stdout, stderr=result.stderr)
            messagebox.showinfo("Success", f"Successfully closed port with PID {pid}")
            self.get_open_ports()
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to close port with PID {pid}: {e}")
    
    def close_application(self):
        self.root.quit()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        root = tk.Tk()
        app = PortManager(root)
        root.mainloop()
