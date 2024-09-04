import tkinter as tk
GRID_SIZE = 100
PIXEL_SIZE = 10  
COLORS = ["#FF0000", "#FF8C00", "#FFA500", "#FFD700", "#FFFF00", "#7FFF00", "#00FF00", "#00FF7F", "#00FFFF", "#87CEEB", "#1E90FF", "#0000FF", "#4169E1", "#9370DB", "#800080", "#EE82EE", "#9400D3"]
class RPlace:
    def __init__(self, root):
        self.root = root
        self.root.title("b/placem")
        self.canvas = tk.Canvas(root, width=GRID_SIZE * PIXEL_SIZE, height=GRID_SIZE * PIXEL_SIZE)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.grid = [['#FFFFFF' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.selected_color = "#000000"
        self.color_frame = tk.Frame(root)
        self.color_frame.grid(row=0, column=1, padx=10, pady=10)
        self.create_color_buttons()
    def draw_grid(self):
        """Draw the grid on the canvas."""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x1 = col * PIXEL_SIZE
                y1 = row * PIXEL_SIZE
                x2 = x1 + PIXEL_SIZE
                y2 = y1 + PIXEL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.grid[row][col], outline="black")
    def on_canvas_click(self, event):
        """Handle canvas click to change pixel color."""
        col = event.x // PIXEL_SIZE
        row = event.y // PIXEL_SIZE
        self.grid[row][col] = self.selected_color
        x1 = col * PIXEL_SIZE
        y1 = row * PIXEL_SIZE
        x2 = x1 + PIXEL_SIZE
        y2 = y1 + PIXEL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_color, outline="black")
    def create_color_buttons(self):
        """Create buttons for each color in the palette."""
        for color in COLORS:
            button = tk.Button(self.color_frame, bg=color, width=3, height=2, command=lambda c=color: self.set_color(c))
            button.pack(side=tk.TOP, pady=2)
    def set_color(self, color):
        """Set the selected color."""
        self.selected_color = color
if __name__ == "__main__":
    root = tk.Tk()
    app = RPlace(root)
    root.mainloop()