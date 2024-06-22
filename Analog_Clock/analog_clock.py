import tkinter as tk
import time
import math

class AnalogClock(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize the main window properties
        self.title("Analog Clock")
        self.geometry("400x450")  # Extra height for digital clock
        self.resizable(False, False)
        self.configure(bg='black')

        # Create a canvas to draw the clock
        self.canvas = tk.Canvas(self, width=400, height=400, bg='black')
        self.canvas.pack()

        # Create a label to display digital time
        self.digital_time_label = tk.Label(self, font=('Arial', 18), bg='black', fg='white')
        self.digital_time_label.pack()

        # Set the center and radius of the clock
        self.center_x = 200
        self.center_y = 200
        self.clock_radius = 180

        # Start updating the clock
        self.update_clock()

    def draw_clock_face(self):
        # Draw the clock face (circle)
        self.canvas.create_oval(self.center_x - self.clock_radius, self.center_y - self.clock_radius,
                                self.center_x + self.clock_radius, self.center_y + self.clock_radius,
                                outline="white", width=4)

        # Draw the hour marks and numbers on the clock face
        for hour in range(12):
            angle = math.radians(hour * 30)  # Convert hour to angle (30 degrees per hour)
            x_outer = self.center_x + self.clock_radius * 0.9 * math.sin(angle)
            y_outer = self.center_y - self.clock_radius * 0.9 * math.cos(angle)
            x_inner = self.center_x + self.clock_radius * 0.8 * math.sin(angle)
            y_inner = self.center_y - self.clock_radius * 0.8 * math.cos(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill="white", width=3)
            x_num = self.center_x + self.clock_radius * 0.7 * math.sin(angle)
            y_num = self.center_y - self.clock_radius * 0.7 * math.cos(angle)
            self.canvas.create_text(x_num, y_num, text=str(hour if hour != 0 else 12), fill="white", font=('Arial', 14))

    def draw_hand(self, length, angle, width, color):
        # Draw a clock hand based on length, angle, width, and color
        angle_rad = math.radians(angle)  # Convert angle to radians
        x_end = self.center_x + length * math.sin(angle_rad)
        y_end = self.center_y - length * math.cos(angle_rad)
        self.canvas.create_line(self.center_x, self.center_y, x_end, y_end, fill=color, width=width)

    def update_clock(self):
        # Clear the canvas to redraw the clock
        self.canvas.delete("all")

        # Draw the clock face
        self.draw_clock_face()

        # Get the current local time
        current_time = time.localtime()
        hours = current_time.tm_hour
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Calculate the angles for the hands
        hour_angle = (hours % 12 + minutes / 60) * 30  # 30 degrees per hour
        minute_angle = (minutes + seconds / 60) * 6    # 6 degrees per minute
        second_angle = seconds * 6                     # 6 degrees per second

        # Draw the clock hands
        self.draw_hand(self.clock_radius * 0.5, hour_angle, 6, "white")  # Hour hand
        self.draw_hand(self.clock_radius * 0.75, minute_angle, 4, "white")  # Minute hand
        self.draw_hand(self.clock_radius * 0.9, second_angle, 2, "red")  # Second hand

        # Display digital time
        digital_time = time.strftime("%H:%M:%S", current_time)
        self.digital_time_label.config(text=digital_time)

        # Schedule the update more frequently for smooth second hand
        self.after(100, self.update_clock)

if __name__ == "__main__":
    clock = AnalogClock()
    clock.mainloop()
