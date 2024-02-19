from cmath import sqrt, pi, tan

class CalculatorModel:
    def __init__(self):
        self.home = None

    @staticmethod
    def is_number(user_input):
        try:
            int(user_input)
            return True
        except ValueError:
            return False

    def calculate_rhombus_values(self, diag1, diag2):
        # Calculate area and perimeter of rhombus
        area = (diag1 * diag2) / 2
        perimeter = 2 * (sqrt(diag1 ** 2 + diag2 ** 2))
        #  lng_diag = sqrt(diag1 ** 2 + diag2 ** 2)
        if diag1 > diag2:
            lng_diag = diag1
        else:
            lng_diag = diag2

        # Rounds the number to 6 decimal places
        perimeter = round(perimeter.real, 6)
        lng_diag = round(lng_diag.real, 6)

        return area, perimeter, lng_diag

    def calculate_silinder_values(self, radius, height):
        # Calculate volume of the cylinder
        volume = pi * radius ** 2 * height

        # Calculate base area of the cylinder
        base_area = pi * radius ** 2

        # Calculate lateral (side) area of the cylinder
        side_area = 2 * pi * radius * height

        volume = round(volume, 6)
        base_area = round(base_area, 6)
        side_area = round(side_area, 6)

        return volume, base_area, side_area

    def calculate_koonus_values(self, radius, height):
        base_area = pi * radius ** 2

        # Calculate the length of the cone's slant height (hypotenuse)
        hypotenuse = sqrt(radius ** 2 + height ** 2)

        # Calculate lateral (side) area of the cone
        side_area = pi * radius * hypotenuse

        base_area = round(base_area, 6)
        hypotenuse = round(hypotenuse.real, 6)
        side_area = round(side_area.real, 6)

        return base_area, hypotenuse, side_area

    def calculate_risttahukas_values(self, length, width, height):
        # Calculate the diagonal of the rectangular prism
        diagonal = sqrt(length ** 2 + width ** 2 + height ** 2)

        # Calculate the volume of the rectangular prism
        volume = length * width * height

        # Calculate the total surface area of the rectangular prism
        total_surface_area = 2 * (length * width + length * height + width * height)

        diagonal = round(diagonal.real, 6)
        volume = round(volume.real, 6)
        total_surface_area = round(total_surface_area, 6)

        return diagonal, volume, total_surface_area

    def calculate_square_pyramid_values(self, side_length, height):
        # Calculate the base area of the square pyramid
        base_area = side_length ** 2

        # Calculate the volume of the square pyramid
        volume = (1 / 3) * base_area * height

        # Calculate the lateral (side) surface area of the square pyramid
        slant_height = sqrt(side_length ** 2 + height ** 2)

        lateral_surface_area = 4 * ((base_area + slant_height) / 2)

        base_area = round(base_area.real, 6)
        volume = round(volume.real, 6)
        lateral_surface_area = round(lateral_surface_area.real, 6)

        return base_area, volume, lateral_surface_area

    def calculate_rigth_triangle_values(self, base, height):
        # Calculate the hypotenuse of the right-angled triangle
        hypotenuse = sqrt(base ** 2 + height ** 2)

        # Calculate the perimeter of the right-angled triangle
        perimeter = base + height + hypotenuse

        # Calculate the area of the right-angled triangle
        area = 0.5 * base * height

        hypotenuse = round(hypotenuse.real, 6)
        perimeter = round(perimeter.real, 6)
        area = round(area.real, 6)

        return hypotenuse, perimeter, area

    def calculate_stadium_values(self, radius, length):
        # Calculate the perimeter of the stadium
        perimeter = 2 * pi * radius + 2 * length

        # Calculate the total area of the stadium
        total_area = pi * radius ** 2 + 2 * radius * length

        # Calculate the area of the center square without the ends
        square_area = length ** 2

        perimeter = round(perimeter.real, 6)
        total_area = round(total_area.real, 6)
        square_area = round(square_area.real, 6)

        return perimeter, total_area, square_area

    def calculate_polygon_values(self, side_length):
        # Calculate the perimeter of the regular pentagon
        perimeter = 5 * side_length

        # Calculate the apothem length of the regular pentagon
        apothem_length = side_length / (2 * tan(pi / 5))

        # Calculate the area of the regular pentagon
        area = (5 * side_length * apothem_length) / 2

        # Calculate the internal angle of the regular pentagon in degrees
        internal_angle_degrees = (180 * (5 - 2)) / 5

        perimeter = round(perimeter.real, 6)
        area = round(area.real, 6)
        internal_angle_degrees = round(internal_angle_degrees.real, 6)

        return perimeter, area, internal_angle_degrees

    def calculate_rectangle_values(self, length, width):
        diagonal_length = sqrt(length ** 2 + width ** 2)  # Calculate the diagonal length of the rectangle

        perimeter = 2 * (length + width)  # Calculate the perimeter of the rectangle

        area = length * width  # Calculate the area of the rectangle

        diagonal_length = round(diagonal_length.real, 6)
        perimeter = round(perimeter.real, 6)
        area = round(area.real, 6)

        return diagonal_length, perimeter, area
