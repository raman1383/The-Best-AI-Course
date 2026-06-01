import tkinter as tk
import os
from PIL import Image, ImageDraw

class MNISTDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("MNIST Digit Drawer")
        self.root.resizable(False, False)
        
        # Configuration
        self.canvas_size = 280 
        self.output_size = 28  
        self.brush_size = 12   
        
        # Determine the directory where the script is running
        try:
            self.current_dir = os.path.dirname(os.path.abspath(__file__))
        except NameError:
            # Fallback for interactive environments like Jupyter
            self.current_dir = os.getcwd()
        
        # Create a Tkinter Canvas
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="black")
        self.canvas.pack(pady=10, padx=10)
        
        # Create an in-memory PIL image
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "black")
        self.draw = ImageDraw.Draw(self.image)
        
        # Bind mouse movement
        self.canvas.bind("<B1-Motion>", self.paint)
        
        # UI Buttons Frame
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)
        
        self.clear_btn = tk.Button(self.btn_frame, text="Clear Canvas", command=self.clear_canvas, width=12)
        self.clear_btn.grid(row=0, column=0, padx=5)
        
        self.save_btn = tk.Button(self.btn_frame, text="Quick Save", command=self.save_image, width=12)
        self.save_btn.grid(row=0, column=1, padx=5)
        
        # Status Label
        self.status_label = tk.Label(root, text="Ready to draw.", fg="gray")
        self.status_label.pack(pady=5)
        
    def paint(self, event):
        x, y = event.x, event.y
        r = self.brush_size
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill="white", outline="white")
        
    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "black")
        self.draw = ImageDraw.Draw(self.image)
        self.status_label.config(text="Canvas cleared.", fg="gray")
        
    def save_image(self):
        # Resize to 28x28
        resized_image = self.image.resize((self.output_size, self.output_size), Image.Resampling.LANCZOS)
        
        # Find a filename that doesn't exist yet
        counter = 0
        while True:
            filename = f"digit_{counter}.png"
            file_path = os.path.join(self.current_dir, filename)
            if not os.path.exists(file_path):
                break
            counter += 1
        
        try:
            resized_image.save(file_path)
            self.status_label.config(text=f"Saved as: {filename}", fg="green")
            print(f"Saved: {file_path}")
        except Exception as e:
            self.status_label.config(text="Error saving image", fg="red")
            print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MNISTDrawer(root)
    root.mainloop()
