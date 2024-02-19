from Home import CalculatorHome
from Rhombus import Rhombus
from Risttahukas import Risttahukas
from Silinder import Silinder
from Koonus import Koonus
from Puramiid import Puramiid
from Kolmnurk import Kolmnurk
from Staadion import Staadion
from Hulknurk import Hulknurk
from Ristkulik import Ristkulik


def switch_page_callback(new_page):
    if new_page == "Peamine lehekülg":
        home = CalculatorHome(switch_page_callback)
        home.main()

    elif new_page == "Rhombus":
        rhombus = Rhombus(switch_page_callback)
        rhombus.main()

    elif new_page == "Silinder":
        sil = Silinder(switch_page_callback)
        sil.main()

    elif new_page == "Koonus":
        koonus = Koonus(switch_page_callback)
        koonus.main()

    elif new_page == "Risttahukas":
        risttahukas = Risttahukas(switch_page_callback)
        risttahukas.main()

    elif new_page == "Püramiid ruudu põhjaga":
        pyramid = Puramiid(switch_page_callback)
        pyramid.main()

    elif new_page == "Täisnurkne kolmnurk":
        kolmnurk = Kolmnurk(switch_page_callback)
        kolmnurk.main()

    elif new_page == "Staadion":
        staadion = Staadion(switch_page_callback)
        staadion.main()

    elif new_page == "Korrapärane hulknurk":
        hulknurk = Hulknurk(switch_page_callback)
        hulknurk.main()

    else:
        ristkulik = Ristkulik(switch_page_callback)
        ristkulik.main()

class GeoCalculator:
    def __init__(self):
        self.home = CalculatorHome(switch_page_callback)

    def main(self):
        self.home.main()

if __name__ == "__main__":
    shape = GeoCalculator()
    shape.main()