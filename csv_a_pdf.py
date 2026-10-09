import csv
from datetime import date
from fpdf import FPDF


class ReportePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Reporte de Inventario", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "I", 10)
        self.cell(0, 6, f"Fecha: {date.today().strftime('%d/%m/%Y')}", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")


pdf = ReportePDF()
pdf.add_page()
pdf.set_font("Helvetica", size=11)

anchos = [55, 20, 25, 25, 45]
encabezados = ["Producto", "Stock", "Vendidos", "Precio", "Estado"]

# --- Encabezados ---
pdf.set_font("Helvetica", "B", 11)
pdf.set_fill_color(60, 60, 60)
pdf.set_text_color(255, 255, 255)
for i, titulo in enumerate(encabezados):
    pdf.cell(anchos[i], 8, titulo, border=1, align="C", fill=True)
pdf.ln()

# --- Filas desde el CSV ---
pdf.set_font("Helvetica", size=10)
pdf.set_text_color(0, 0, 0)

total = 0
criticos = 0

with open("reporte_final.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        total += 1
        estado = fila["estado"]

        # Color de fondo según estado
        if estado == "CRÍTICO":
            pdf.set_fill_color(255, 200, 200)  # rojo claro
            criticos += 1
        elif estado == "OK":
            pdf.set_fill_color(200, 255, 200)  # verde claro
        else:
            pdf.set_fill_color(240, 240, 240)  # gris claro

        pdf.cell(anchos[0], 8, fila["producto"], border=1, fill=True)
        pdf.cell(anchos[1], 8, str(fila["stock"]), border=1, align="C", fill=True)
        pdf.cell(anchos[2], 8, str(fila["vendidos"]), border=1, align="C", fill=True)
        pdf.cell(anchos[3], 8, f"{float(fila['precio']):.2f}", border=1, align="C", fill=True)
        pdf.cell(anchos[4], 8, estado, border=1, align="C", fill=True)
        pdf.ln()

# --- Resumen ---
pdf.ln(5)
pdf.set_font("Helvetica", "B", 11)
pdf.cell(0, 8, f"Total de productos: {total}", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 8, f"Productos críticos: {criticos}", new_x="LMARGIN", new_y="NEXT")

pdf.output("reporte.pdf")
print(f"PDF creado: reporte.pdf ({total} productos, {criticos} críticos)")
