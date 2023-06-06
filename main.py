import tkinter as tk
from tkinter import ttk
import math

LARGE_FONT_STYLE=('Arial', 40, 'bold')
SMALL_FONT_STYLE=('Arial',16)
DIGIT_FONT_STYLE=('Arial',24, 'bold')
DEFAULT_FONT_STYLE=('Arial',20)
OFF_WHITE="#f8faff"
WHITE="#ffffff"
LIGHT_GRAY="#f5f5f5"
LABEL_COLOR = "#25265E"
LIGHT_BLUE="#CCEDFF"
RED="#ff0000"



class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("600x700")
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.pack_propagate(0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Pysics Calculator", font=LARGE_FONT_STYLE)

        label.grid(row=0, column=2, padx=5, pady=10)

        button1=ttk.Button(self, text = "Free Fall",
        command = lambda : controller.show_frame(Page1))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2=ttk.Button(self, text = "Projectile",
        command = lambda : controller.show_frame(Page2))

        button2.grid(row=1, column=2, padx=10, pady=10)

# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        self.acc = tk.StringVar()
        self.initial_velocity = tk.StringVar()
        self.height = tk.StringVar()
        self.time_of_fall = tk.StringVar()
        self.velocity = tk.StringVar()
        tk.Frame.__init__(self, parent)
        self.warning = tk.Text(self,height=1, width=12, bg=RED, fg=WHITE, font=DEFAULT_FONT_STYLE)
        self.gravity_acc_entry = ttk.Entry(self, textvariable=self.acc)
        self.init_velocity_entry = ttk.Entry(self, textvariable=self.initial_velocity)
        self.height_entry = ttk.Entry(self, textvariable=self.height)
        self.time_of_fall_entry = ttk.Entry(self, textvariable=self.time_of_fall)
        self.velocity_entry = ttk.Entry(self, textvariable=self.velocity)

        label = ttk.Label(self, text ="Free Fall", font = LARGE_FONT_STYLE)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)  

        self.create_entries()

    def create_entries(self):
        self.create_gravity_entry()
        self.create_init_velocity_entry()
        self.create_height_entry()
        self.create_time_of_fall_entry()
        self.create_velocity_entry()
        self.create_calculate_button()

    def create_gravity_entry(self):
        # textbox for gravitational force
        gravity_acc_label = ttk.Label(self, text="Gravitational accelaration(m/s^2): ")
        gravity_acc_label.grid(row=2, column=1, padx=5, pady=5)

        self.gravity_acc_entry.insert(index=0, string='9.80665')
        self.gravity_acc_entry.grid(row=2, column=2, padx=5, pady=5)
        self.gravity_acc_entry.focus()

    def create_init_velocity_entry(self):
        # textbox for initial velcity
        init_velocity_label = ttk.Label(self, text="Initial velocity(m/s): ")
        init_velocity_label.grid(row=3, column=1, padx=5, pady=5)
      
        self.init_velocity_entry.grid(row=3, column=2, padx=5, pady=5)

    def create_height_entry(self):
        # textbox for height
        height_label = ttk.Label(self, text="Height(m): ")
        height_label.grid(row=4, column=1, padx=5, pady=5)

        self.height_entry.grid(row=4, column=2, padx=5, pady=5)

    def create_time_of_fall_entry(self):
        # textbox for time of fall
        time_of_fall_label = ttk.Label(self, text="Time of fall(s): ")
        time_of_fall_label.grid(row=5, column=1, padx=5, pady=5)

        self.time_of_fall_entry.grid(row=5, column=2, padx=5, pady=5)

    def create_velocity_entry(self):
        # textbox for velocity
        velocity_label = ttk.Label(self, text="Velocity(m/s): ")
        velocity_label.grid(row=6, column=1, padx=5, pady=5)

        self.velocity_entry.grid(row=6, column=2, padx=5, pady=5)

    def create_warning(self):
        text = "Fill first 3 fields!"
        self.warning.insert(tk.END, text)
        self.warning.grid(row = 8, column = 1, padx = 10, pady = 10)

    def remove_warning(self):
        self.warning.grid_forget()


    def create_calculate_button(self):
        calculate_button = ttk.Button(self, text ="Calculate",
                            command = lambda : self.calculate())
        # putting the button in its place
        # by using grid
        calculate_button.grid(row = 7, column = 1, padx = 10, pady = 10)

    def calculate(self):
        try:
            init_vel = float(self.init_velocity_entry.get())
            height = float(self.height_entry.get())
            acc = float(self.gravity_acc_entry.get())
        except ValueError:
            self.create_warning()
            return

        if(init_vel == None or height == None or acc == None):
            self.create_warning()
            return
        self.remove_warning()
        determinant = math.sqrt(init_vel**2 + 2*acc*height)
        time = round((-init_vel + determinant)/acc, 5)

        velocity = round(((init_vel) + acc*time), 5)

        self.time_of_fall_entry.delete(first=0, last=tk.END)
        self.time_of_fall_entry.insert(0, time)

        self.velocity_entry.delete(first=0, last=tk.END)
        self.velocity_entry.insert(0, velocity)
        
        

# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        self.angle = tk.StringVar()
        self.init_velocity = tk.StringVar()
        self.init_height = tk.StringVar()
        self.time_of_flight = tk.StringVar()
        self.distance = tk.StringVar()
        self.max_height = tk.StringVar()
        tk.Frame.__init__(self, parent)
        self.warning = tk.Text(self,height=1, width=12, bg=RED, fg=WHITE, font=DEFAULT_FONT_STYLE)
        self.angle_entry = ttk.Entry(self, textvariable=self.angle)
        self.init_velocity_entry = ttk.Entry(self, textvariable=self.init_velocity)
        self.init_height_entry = ttk.Entry(self, textvariable=self.init_height)
        self.time_of_flight_entry = ttk.Entry(self, textvariable=self.time_of_flight)
        self.distance_entry = ttk.Entry(self, textvariable=self.distance)
        self.max_height_entry = ttk.Entry(self, textvariable=self.max_height)

        label = ttk.Label(self, text ="Projectile Motion", font = LARGE_FONT_STYLE)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)  

        self.create_entries()

    def create_entries(self):
        self.create_init_velocity_entry()
        self.create_angle_entry()
        self.create_init_height_entry()
        self.create_time_of_flight_entry()
        self.create_distance_entry()
        self.create_max_height_entry()
        self.create_calculate_button()

    def create_init_velocity_entry(self):
        init_velocity_label = ttk.Label(self, text="Initial velocity(m/s): ")
        init_velocity_label.grid(row=2, column=1, padx=5, pady=5)
      
        self.init_velocity_entry.grid(row=2, column=2, padx=5, pady=5)

    def create_angle_entry(self):
        angle_label = ttk.Label(self, text="Angle of launch(deg): ")
        angle_label.grid(row=3, column=1, padx=5, pady=5)
      
        self.angle_entry.grid(row=3, column=2, padx=5, pady=5)

    def create_init_height_entry(self):
        init_height_label = ttk.Label(self, text="Initial height(m): ")
        init_height_label.grid(row=4, column=1, padx=5, pady=5)
      
        self.init_height_entry.grid(row=4, column=2, padx=5, pady=5)

    def create_time_of_flight_entry(self):
        time_of_flight_label = ttk.Label(self, text="Time of flight(s): ")
        time_of_flight_label.grid(row=5, column=1, padx=5, pady=5)
      
        self.time_of_flight_entry.grid(row=5, column=2, padx=5, pady=5)
    
    def create_distance_entry(self):
        distance_label = ttk.Label(self, text="Distance(m): ")
        distance_label.grid(row=6, column=1, padx=5, pady=5)
      
        self.distance_entry.grid(row=6, column=2, padx=5, pady=5)

    def create_max_height_entry(self):
        max_height_label = ttk.Label(self, text="Maximum height(m): ")
        max_height_label.grid(row=7, column=1, padx=5, pady=5)
      
        self.max_height_entry.grid(row=7, column=2, padx=5, pady=5)

    def create_calculate_button(self):
        calculate_button = ttk.Button(self, text ="Calculate",
                            command = lambda : self.calculate())
        # putting the button in its place
        # by using grid
        calculate_button.grid(row = 8, column = 1, padx = 10, pady = 10)

    def create_warning(self):
        text = "Fill first 3 fields!"
        self.warning.insert(tk.END, text)
        self.warning.grid(row = 9, column = 1, padx = 10, pady = 10)

    def remove_warning(self):
        self.warning.grid_forget()
        
    def calculate(self):
        try:
            init_vel = float(self.init_velocity.get())
            init_height = float(self.init_height.get())
            angle = float(self.angle.get())
        except ValueError:
            self.create_warning()
            return

        if(init_vel == None or init_height == None or angle == None):
            self.create_warning()
            return      
        
        g = 9.80665
        v_x = init_vel*math.cos(math.radians(angle))
        v_y = init_vel*math.sin(math.radians(angle))
        max_height = round(init_height + (v_y**2)/(2*g), 5)
        t_to_max_height = v_y/g
        t_to_ground = math.sqrt(((max_height)*2)/g)
        print(t_to_max_height, init_height, max_height, t_to_ground)
        print((max_height+init_height), (max_height+init_height)*2, ((max_height+init_height)*2)/g)
        t_flight = round(t_to_max_height + t_to_ground, 5)
        distance = round((v_x * t_flight), 5)

        self.max_height_entry.delete(first=0, last=tk.END)
        self.max_height_entry.insert(0, max_height)

        self.time_of_flight_entry.delete(first=0, last=tk.END)
        self.time_of_flight_entry.insert(0, t_flight)
        
        self.distance_entry.delete(first=0, last=tk.END)
        self.distance_entry.insert(0, distance)

        
        

if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()

