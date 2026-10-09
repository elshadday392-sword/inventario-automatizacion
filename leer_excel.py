import openpyxl

wb = openpyxl.load_workbook("ventas.xlsx")
ws = wb.active

print("=== CONTENIDO DEL EXCEL ===")
for fila in ws.iter_rows(values_only=True):
    print(fila)
