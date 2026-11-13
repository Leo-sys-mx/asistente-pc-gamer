import urllib.parse

def generar_enlaces_compra(componente, precio_estimado):
    busqueda = urllib.parse.quote(componente)
    link_ml = "https://listado.mercadolibre.com.mx/" + busqueda + "_OrderId_PRICE"
    link_ddtech = "https://ddtech.mx/productos/buscar?q=" + busqueda

    print(f"\n📦 Componente: {componente}")
    print(f"   Precio de referencia: ~${precio_estimado:,.2f} MXN")
    print(f"   🛒 Ver en Mercado Libre (Menor precio): {link_ml}")
    print(f"   🛒 Ver en DDTech: {link_ddtech}")

print("=== ASISTENTE LEO-SYS-MX: COTIZADOR PC GAMER ===")
presupuesto = float(input("¿Cuál es tu presupuesto en pesos mexicanos (MXN)?: "))

if presupuesto < 10000:
    print("\n💡 RECOMENDACIÓN: Gama de Entrada (Gráficos Integrados)")
    print("Por qué conviene: Ahorras el costo de una tarjeta de video dedicada hoy, pero puedes jugar en 1080p y mejorar la PC después.")
    generar_enlaces_compra("Procesador AMD Ryzen 5 5600G", 2400)
    generar_enlaces_compra("Memoria RAM DDR4 16GB 3200MHz", 750)
else:
    print("\n💡 RECOMENDACIÓN: Gama Media Calidad-Precio")
    print("Por qué conviene: Esta combinación mueve casi cualquier juego actual en gráficos altos a 1080p sin gastar de más.")
    generar_enlaces_compra("Procesador AMD Ryzen 5 5600", 2300)
    generar_enlaces_compra("Tarjeta de video Radeon RX 6600 8GB", 4500)
