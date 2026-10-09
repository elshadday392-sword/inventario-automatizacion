import subprocess
import os
import time

# --- Colores para la terminal ---
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
RESET = "\033[0m"


def ejecutar(nombre_script):
    print(f"\n{AMARILLO}▶ Ejecutando {nombre_script}...{RESET}")
    inicio = time.time()
    resultado = subprocess.run(["python", nombre_script], capture_output=True, text=True)
    duracion = round(time.time() - inicio, 2)

    if resultado.returncode == 0:
        print(f"{VERDE}✅ {nombre_script} completado en {duracion}s{RESET}")
        if resultado.stdout.strip():
            print(resultado.stdout.strip())
    else:
        print(f"{ROJO}❌ Error en {nombre_script}{RESET}")
        print(resultado.stderr)
        raise SystemExit(1)


# --- Verificar archivos de entrada ---
archivos_requeridos = ["inventario.csv", "ventas.xlsx", "reporte.docx"]
faltantes = [a for a in archivos_requeridos if not os.path.exists(a)]

if faltantes:
    print(f"{ROJO}Faltan archivos: {', '.join(faltantes)}{RESET}")
    raise SystemExit(1)

print(f"{VERDE}🚀 Iniciando pipeline completo...{RESET}")

# --- Ejecutar en orden ---
ejecutar("reponer.py")
ejecutar("cruzar.py")
ejecutar("csv_a_pdf.py")

print(f"\n{VERDE}🎉 Pipeline completado. Archivo final: reporte.pdf{RESET}")
import shutil
try:
    shutil.copy("reporte.pdf", os.path.expanduser("~/storage/downloads/reporte.pdf"))
    print(f"{VERDE}📤 Copiado a Descargas.{RESET}")
except Exception as e:
    print(f"{AMARILLO}⚠ No se pudo copiar a Descargas: {e}{RESET}")
