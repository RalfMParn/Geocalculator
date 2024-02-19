class CalculatorController:
    def __init__(self):
        pass


'''
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

    def switch_page_callback(self, new_page):
        if new_page == "Peamine lehekülg":
            home = CalculatorHome(switch_page_callback)
            home.main()

        elif new_page == "Rhombus":
            rhombus = Rhombus(switch_page_callback)
            rhombus.main()

        elif new_page == "Silinder":
            sil = Silinder(self.switch_page_callback)
            sil.main()

        elif new_page == "Koonus":
            koonus = Koonus(self.switch_page_callback)
            koonus.main()

        elif new_page == "Risttahukas":
            risttahukas = Risttahukas(self.switch_page_callback)
            risttahukas.main()

        elif new_page == "Püramiid ruudu põhjaga":
            pyramid = Puramiid(self.switch_page_callback)
            pyramid.main()

        elif new_page == "Täisnurkne kolmnurk":
            kolmnurk = Kolmnurk(self.switch_page_callback)
            kolmnurk.main()

        elif new_page == "Staadion":
            staadion = Staadion(self.switch_page_callback)
            staadion.main()

        elif new_page == "Korrapärane hulknurk":
            hulknurk = Hulknurk(self.switch_page_callback)
            hulknurk.main()

        else:
            ristkulik = Ristkulik(self.switch_page_callback)
            ristkulik.main()

        self.Rhombus = Rhombus(self, CalculatorController)


    def switch_page(self, option):
        #option = self.Rhombus.selected_option.get()
        print(f"Going to CONTROLLER{option}....")
        '''

