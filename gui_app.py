import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
from backend import ISPProcessor

class ISPToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IFSO IP Letter Generator")
        self.root.geometry("600x450")
        
        # Style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variables
        self.html_path = tk.StringVar()
        self.status_var = tk.StringVar(value="Ready")
        self.progress_var = tk.DoubleVar(value=0)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self.root, padding="10")
        header_frame.pack(fill=tk.X)
        
        ttk.Label(header_frame, text="ISP Request Generator", font=("Helvetica", 16, "bold")).pack(side=tk.LEFT)
        
        # File Selection Block
        file_frame = ttk.LabelFrame(self.root, text="Source File", padding="10")
        file_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Entry(file_frame, textvariable=self.html_path, width=50).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        ttk.Button(file_frame, text="Browse HTML", command=self.browse_file).pack(side=tk.LEFT)
        
        # Actions Block
        action_frame = ttk.Frame(self.root, padding="10")
        action_frame.pack(fill=tk.X)
        
        self.start_btn = ttk.Button(action_frame, text="Generate Letters", command=self.start_processing_thread, state=tk.NORMAL)
        self.start_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Progress Block
        progress_frame = ttk.Frame(self.root, padding="10")
        progress_frame.pack(fill=tk.X)
        
        ttk.Label(progress_frame, textvariable=self.status_var).pack(anchor=tk.W)
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill=tk.X, pady=5)
        
        # Log Block
        log_frame = ttk.LabelFrame(self.root, text="Process Log", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.log_text = tk.Text(log_frame, height=10, state=tk.DISABLED, font=("Consolas", 9))
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
    def log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html"), ("All Files", "*.*")])
        if filename:
            self.html_path.set(filename)
            self.log(f"Selected file: {os.path.basename(filename)}")

    def start_processing_thread(self):
        path = self.html_path.get()
        if not path:
            messagebox.showwarning("Input Required", "Please select an HTML file first.")
            return
            
        self.start_btn.config(state=tk.DISABLED)
        self.progress_var.set(0)
        self.log("Starting process...")
        
        # Run in thread
        t = threading.Thread(target=self.run_process, args=(path,))
        t.start()
        
    def run_process(self, html_path):
        try:
            processor = ISPProcessor(
                output_dir="Generated_Letters",
                cache_file="isp_cache.json"
            )
            
            self.status_var.set("Parsing HTML...")
            metadata, raw_data = processor.parse_html(html_path)
            
            suspect_name = metadata.get("name", "Unknown").replace(" ", "_")
            self.log(f"Suspect: {metadata.get('name')}")
            self.log(f"Found {len(raw_data)} login records.")
            
            if not raw_data:
                self.log("No data found! Aborting.")
                self.finalize(success=False)
                return

            self.status_var.set("Identifying ISPs...")
            
            # Callback to update progress bar
            def update_progress(current, total):
                percent = (current / total) * 100
                self.progress_var.set(percent)
                # Force UI update occasionally (not thread safe strictly but usually ok for vars, ideally use queue)
                
            def log_msg(msg):
                # We need to schedule this on main thread ideally, but Tkinter is somewhat forgiving for simple text appends.
                # For robustness, we mostly log major steps.
                pass 

            grouped_data = processor.process_data(raw_data, progress_callback=update_progress, log_callback=log_msg)
            
            self.status_var.set("Generating Documents...")
            self.log(f"ISPs identified: {', '.join(grouped_data.keys())}")
            
            # Generate JIO
            if "JIO" in grouped_data:
                self.log("Creating JIO documents...")
                success, msg = processor.fill_jio_excel(grouped_data["JIO"], "JIO IP.xlsx", f"{suspect_name}_JIO_Data.xlsx")
                if success: self.log(f"Created {os.path.basename(msg)}")
                else: self.log(f"Failed JIO Excel: {msg}")
                
                success, msg = processor.fill_word_letter(grouped_data["JIO"], "JIO", "IP Letter.docx", f"{suspect_name}_JIO_Request_Letter.docx", metadata=metadata)
                if success: self.log(f"Created {os.path.basename(msg)}")
                else: self.log(f"Failed JIO Letter: {msg}")

            # Generate AIRTEL
            if "AIRTEL" in grouped_data:
                self.log("Creating Airtel documents...")
                success, msg = processor.fill_airtel_excel(grouped_data["AIRTEL"], "Airtel Format.xlsx", f"{suspect_name}_Airtel_Data.xlsx")
                if success: self.log(f"Created {os.path.basename(msg)}")
                
                success, msg = processor.fill_word_letter(grouped_data["AIRTEL"], "AIRTEL", "IP Letter.docx", f"{suspect_name}_AIRTEL_Request_Letter.docx", metadata=metadata)
                if success: self.log(f"Created {os.path.basename(msg)}")

            # Generate VI
            if "VI" in grouped_data:
                 self.log("Creating VI documents...")
                 success, msg = processor.fill_word_letter(grouped_data["VI"], "VI", "IP Letter.docx", f"{suspect_name}_VI_Request_Letter.docx", metadata=metadata)
                 if success: self.log(f"Created {os.path.basename(msg)}")

            self.finalize(success=True)

        except Exception as e:
            self.log(f"Error: {e}")
            self.finalize(success=False)

    def finalize(self, success):
        self.status_var.set("Completed" if success else "Failed")
        self.start_btn.config(state=tk.NORMAL)
        if success:
            messagebox.showinfo("Success", "Letters generated successfully in 'Generated_Letters' folder.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ISPToolApp(root)
    root.mainloop()
