from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from Model import CalculatorModel

class Koonus(Tk):
    def __init__(self, switch_page_callback):
        super().__init__()
        self.switch_page_callback = switch_page_callback
        self.model = CalculatorModel()
        self.title("Koonus Kalkulaator")

        self.width = 650
        self.height = 280

        self.main_Font = font.Font(family="Verdana", size=22)
        self.default_Font = font.Font(family="Verdana", size=14)

        self.center_window(self.width, self.height)
        self.selected_option = StringVar(self)

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        (self.btn_arvuta, self.lbl_info, self.lbl_info2, self.entry1, self.entry2, self.drop, self.btn_select,
         self.text_box) = self.create_frame_widgets()

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_top_frame(self):
        frame = Frame(self, bg="orange", height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg="#664837")
        frame.pack(expand=True, fill=BOTH)
        return frame

    def calc_and_display(self):
        valid_input = False
        while not valid_input:
            try:
                radius = float(self.entry1.get())
                height = float(self.entry2.get())
                if radius <= 0 or height <= 0:
                    raise ValueError("Raadius ja kõrgus peab olema positiivne arv")
                valid_input = True
            except ValueError as e:
                self.display_error(str(e))
                break

        if valid_input:
            radius = float(self.entry1.get())
            height = float(self.entry2.get())
            base_area, hypotenuse, side_area = self.model.calculate_koonus_values(radius, height)

            if isinstance(base_area, float) and base_area.is_integer():
                base_area = int(base_area)
            if isinstance(hypotenuse, float) and hypotenuse.is_integer():
                hypotenuse = int(hypotenuse)
            if isinstance(side_area, float) and side_area.is_integer():
                side_area = int(side_area)

            radius = str(radius).rstrip('.0')
            height = str(height).rstrip('.0')

            # Display the calculated values in the text box
            self.text_box.config(state=NORMAL)
            self.text_box.delete(1.0, END)  # Clear previous content
            self.entry1.delete(0, END)  # Takes .0 off the end of the entered number
            self.entry2.delete(0, END)
            self.text_box.insert(END, f"Raadius: {radius}\nKõrgus: {height}\nAluse pindala: {base_area}\n"
                                      f"Hüpotenuus: {hypotenuse}\nKülje pindala: {side_area}")
            self.text_box.config(state=DISABLED)

    def create_frame_widgets(self):
        self.btn_arvuta = Button(self.top_frame, text="Arvuta", font=self.default_Font, bg="#664837",
                                 fg="white", width=10, height=1, command=self.calc_and_display)

        self.btn_arvuta.grid(row=1, column=3, padx=5, pady=5)

        self.lbl_info = Label(self.top_frame, text="Raadius", bg="orange", font=self.default_Font)
        self.lbl_info.grid(row=0, column=0, padx=5, pady=5)

        self.lbl_info2 = Label(self.top_frame, text="Kõrgus", bg="orange", font=self.default_Font)
        self.lbl_info2.grid(row=1, column=0, padx=5, pady=5)

        self.entry1 = Entry(self.top_frame, font=self.default_Font)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.entry2 = Entry(self.top_frame, font=self.default_Font)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        options = ["Peamine lehekülg", "Rhombus", "Silinder", "Koonus", "Risttahukas", "Püramiid ruudu põhjaga",
                   "Täisnurkne kolmnurk",
                   "Staadion", "Korrapärane hulknurk", "Ristkülik"]

        self.selected_option.set(options[3])  # Set the default option
        self.drop = OptionMenu(self.top_frame, self.selected_option, *options)
        self.drop.config(width=20, bg="#664837", fg="white", bd=5, highlightthickness=0)
        self.drop.grid(row=0, column=3, padx=5, pady=5)

        self.btn_select = Button(self.top_frame, text="Vali", bg="#664837", fg="white",
                                 width=5, command=self.switch_page)

        self.btn_select.grid(row=0, column=4, padx=5, pady=5)

        self.text_box = Text(self.bottom_frame, font=self.default_Font, state=DISABLED)
        scrollbar = Scrollbar(self.bottom_frame, orient="vertical")
        scrollbar.config(command=self.text_box.yview)
        self.text_box.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)

        self.selected_option.trace_add("write", self.dropdown_option_selected)

        return (self.btn_arvuta, self.lbl_info, self.lbl_info2, self.entry1,
                self.entry2, self.drop, self.btn_select, self.text_box)

    def display_error(self, error):
        messagebox.showerror("Viga", f"Raadius on vigane. Raadius ja kõrgus peab olema positiivne arv. Error: {error}")

    def dropdown_option_selected(self, *args):
        self.selected_option.set(self.selected_option.get())
        print(f"Selected option: {self.selected_option.get()}")


    def set_switch_page_callback(self, switch_page_callback):
        self.switch_page_callback = switch_page_callback

    def switch_page(self):
        option = self.selected_option.get()
        print(f"Going to {option}....")

        if self.switch_page_callback:
            self.destroy()
            self.switch_page_callback(option)
