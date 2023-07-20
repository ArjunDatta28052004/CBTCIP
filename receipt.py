# import reportlab library for creating pdf
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# creating the dataset to be displayed in the pdf

info = [["Date", "Product Name", "Quantity", "Price"],
        ["12/05/2023", "Chair", "10", "20000/-"],
       ["13/05/2023", "Sofa", "10", "200000/-"],
       ["14/06/2023", "Bed", "20", "1000000/-"],
       ["Total","", "", "1220000/-"],
       ["CGST", "", "1.25%", "15250/-"],
       ["SGST", "", "1.25%", "15250/-"],
       ["Discount", "", "", "-200000/-"],
       ["Total Amount", "", "", "1050000/-"]]

# initializing the name of the pdf and the size in which it has to be saved

pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

styles = getSampleStyleSheet()


title_style = styles["Heading1"]


title_style.alignment = 1

# defining the heading of the PDF
title = Paragraph("Receipt of Retail Store", title_style)

# creating the table and designing it 

style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (4, 4), 1, colors.black),
        ("BACKGROUND", (0, 0), (3, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)])


table = Table(info, style = style)

# building the PDF 

pdf.build([title, table])

# lets run the code