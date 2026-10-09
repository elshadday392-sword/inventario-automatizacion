# Automatización de Reporte de Inventario

Pipeline en Python que toma datos de **Excel**, **Word** y **CSV**, los cruza automáticamente y genera un **PDF profesional** listo para enviar al cliente.

## 🎯 Problema que resuelve

Un negocio pierde horas semanales cruzando manualmente datos de Excel con un reporte en Word para saber qué productos reponer. Este pipeline lo hace en segundos.

## 🚀 Cómo funciona

inventario.csv ──┐
│
ventas.xlsx ─────┼──► cruzar.py ──► reporte_final.csv ──► csv_a_pdf.py ──► reporte.pdf
│
reporte.docx ────┘


## 📦 Archivos

| Archivo | Función |
|---|---|
| `reponer.py` | Filtra productos urgentes desde CSV |
| `leer_excel.py` | Extrae datos de Excel |
| `leer_word.py` | Extrae tablas de Word |
| `cruzar.py` | Une datos por nombre de producto |
| `csv_a_pdf.py` | Genera el PDF final con colores y resumen |
| `ejecutar.py` | Ejecuta todo el pipeline en un comando |

## ⚙️ Instalación

```bash
pkg install libjpeg-turbo libpng freetype libxml2 libxslt
pip install openpyxl python-docx fpdf2

python ejecutar.py

Genera reporte.pdf con:

· Fecha automática
· Filas coloreadas según estado (rojo = crítico)
· Resumen final

🛠️ Tecnologías

· Python 3.13
· openpyxl (Excel)
· python-docx (Word)
· fpdf2 (PDF)
· Termux (entorno Android)

👤 Autor

elshadday392-sword

