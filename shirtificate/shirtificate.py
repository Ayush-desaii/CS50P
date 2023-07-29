from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 10, 70, 190)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 33)
        # Printing title:
        self.cell(0, 50, "CS50 shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

a = input("Name: ")

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(False)
pdf.set_font("helvetica", size=20)
pdf.set_text_color(250,250,250)
pdf.cell(0, 225, f"{a} took CS50", align="C")
pdf.output("shirtificate.pdf")