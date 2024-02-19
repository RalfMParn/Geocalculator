from tkinter import *
import tkinter.font as font


class CalculatorHome(Tk):
    def __init__(self, switch_page_callback):
        super().__init__()

        self.title("Geokalkulaator")
        self.width = 550
        self.height = 280

        self.selected_option = StringVar(self)
        self.switch_page_callback = switch_page_callback

        self.main_Font = font.Font(family="Verdana", size=22)
        self.default_Font = font.Font(family="Verdana", size=14)

        self.center_window(self.width, self.height)
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        (lbl_main, drop_down, btn_select) = self.create_frame_widgets()

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_top_frame(self):
        frame = Frame(self, height=15, bg="orange")
        frame.pack(expand=False, fill=X)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg="#664837", highlightthickness=6, highlightbackground="black")
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self):
        lbl_main = Label(self.top_frame, text="Tere tulemast geokalkulaatorisse!", font=self.main_Font, bg="orange")
        lbl_main.pack()

        options = ["Peamine lehekülg", "Rhombus", "Silinder", "Koonus", "Risttahukas", "Püramiid ruudu põhjaga",
                   "Täisnurkne kolmnurk",
                   "Staadion", "Korrapärane hulknurk", "Ristkülik"]

        self.selected_option.set(options[0])  # Set the default option
        drop_down = OptionMenu(self.bottom_frame, self.selected_option, *options)
        drop_down.config(width=20, bg="#664837", fg="white", bd=5, highlightthickness=0)
        drop_down.pack(padx=5, pady=20)

        btn_select = Button(self.bottom_frame, text="Vali", bg="#664837", fg="white", width=5, command=lambda: self.switch_page())
        btn_select.pack()

        self.selected_option.trace_add("write", self.dropdown_option_selected)

        return lbl_main, drop_down, btn_select

    def dropdown_option_selected(self, *args):
        self.selected_option.set(self.selected_option.get())
        print(f"Selected option: {self.selected_option.get()}")

    def set_switch_page_callback(self, switch_page_callback):
        self.switch_page_callback = switch_page_callback

    def switch_page(self):
        option = self.selected_option.get()
        # This code gets the option selected and attatches it to the "option" variable
        print(f"Going to {option}....")

        if self.switch_page_callback: # Checks if the variable is empty or not
            self.destroy()
            self.switch_page_callback(option)  # Sends the selected option to the switch_page_callback function
