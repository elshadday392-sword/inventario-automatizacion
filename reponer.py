import csv

with open('inventario.csv', 'r', encoding='utf-8') as archivo:
    inventario = list(csv.DictReader(archivo))

for fila in inventario:
    fila['stock'] = int(fila['stock'])
    fila['vendidos_semana'] = int(fila['vendidos_semana'])
    fila['precio'] = float(fila['precio'])

urgentes = []
for fila in inventario:
    if fila['stock'] < 10 and fila['vendidos_semana'] > 5:
        urgentes.append(fila)

for fila in urgentes:
    fila['urgencia'] = round((fila['vendidos_semana'] / fila['stock']) * 10, 1)

urgentes.sort(key=lambda x: x['urgencia'], reverse=True)

print("\n=== PRODUCTOS A REPONER ===")
for fila in urgentes:
    print(f"{fila['producto']:<18} | stock: {fila['stock']:<3} | vendidos: {fila['vendidos_semana']:<3} | urgencia: {fila['urgencia']}")

with open('criticos.csv', 'w', newline='', encoding='utf-8') as archivo:
    campos = ['producto', 'stock', 'vendidos_semana', 'precio', 'urgencia']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(urgentes)

print(f"\nTotal: {len(urgentes)} productos guardados en criticos.csv")

