from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from Model import CalculatorModel
from Controller import CalculatorController

class Rhombus(Tk):
    def __init__(self, switch_page_callback):
        super().__init__()
        self.switch_page_callback = switch_page_callback
        self.model = CalculatorModel()
        self.CalculatorController = CalculatorController
        self.title("Rhombi Kalkulaator")
        self.width = 650
        self.height = 280

        self.main_Font = font.Font(family="Verdana", size=22)
        self.default_Font = font.Font(family="Verdana", size=14)

        self.center_window(self.width, self.height)
        self.selected_option = StringVar(self)

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        (self.btn_arvuta, self.lbl_info, self.lbl_info2, self.diag_entry1, self.diag_entry2, self.drop, self.btn_select,
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
                diag1 = float(self.diag_entry1.get())
                diag2 = float(self.diag_entry2.get())
                if diag1 <= 0 or diag2 <= 0:
                    raise ValueError("Diagonals peab olema positiivne arv")
                valid_input = True
            except ValueError as e:
                self.display_error(str(e))
                break

        if valid_input:
            diag1 = float(self.diag_entry1.get())
            diag2 = float(self.diag_entry2.get())
            area, perimeter, lng_diag = self.model.calculate_rhombus_values(diag1, diag2)

            if isinstance(area, float) and area.is_integer():
                area = int(area)
            if isinstance(perimeter, float) and perimeter.is_integer():
                perimeter = int(perimeter)
            if isinstance(lng_diag, float) and lng_diag.is_integer():
                lng_diag = int(lng_diag)

            diag1 = str(diag1).rstrip('.0')
            diag2 = str(diag2).rstrip('.0')

            # Display the calculated values in the text box
            self.text_box.config(state=NORMAL)
            self.text_box.delete(1.0, END)
            self.diag_entry1.delete(0, END)
            self.diag_entry2.delete(0, END)
            self.text_box.insert(END, f"Diagonaal 1: {diag1}\nDiagonaal 2: {diag2}\nPindala: {area}\nÜmbermõõt: {perimeter}\nPikkem Diagonal: {lng_diag}")
            self.text_box.config(state=DISABLED)

    def create_frame_widgets(self):
        # Creates the calculate (arvuta) button
        self.btn_arvuta = Button(self.top_frame, text="Arvuta", font=self.default_Font, bg="#664837",
                                 fg="white", width=10, height=1, command=self.calc_and_display)

        self.btn_arvuta.grid(row=1, column=3, padx=5, pady=5)

        self.lbl_info = Label(self.top_frame, text="Diagonaal 1", bg="orange", font=self.default_Font)
        self.lbl_info.grid(row=0, column=0, padx=5, pady=5)

        self.lbl_info2 = Label(self.top_frame, text="Diagonaal 2", bg="orange", font=self.default_Font)
        self.lbl_info2.grid(row=1, column=0, padx=5, pady=5)

        self.diag_entry1 = Entry(self.top_frame, font=self.default_Font)
        self.diag_entry1.grid(row=0, column=1, padx=5, pady=5)

        self.diag_entry2 = Entry(self.top_frame, font=self.default_Font)
        self.diag_entry2.grid(row=1, column=1, padx=5, pady=5)

        options = ["Peamine lehekülg", "Rhombus", "Silinder", "Koonus", "Risttahukas", "Püramiid ruudu põhjaga",
                   "Täisnurkne kolmnurk",
                   "Staadion", "Korrapärane hulknurk", "Ristnurk"]

        self.selected_option.set(options[1])  # Set the default option
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

        return (self.btn_arvuta, self.lbl_info, self.lbl_info2, self.diag_entry1,
                self.diag_entry2, self.drop, self.btn_select, self.text_box)

    def display_error(self, error):
        messagebox.showerror("Viga", f"Raadius on vigane. Diagonals peab olema positiivne arv. Error: {error}")

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
