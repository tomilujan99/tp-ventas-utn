
# =============================================================================
# ANÁLISIS DE VENTAS - INDUMENTARIA Y ACCESORIOS DE FÚTBOL 2026
# =============================================================================
# Trabajo Práctico: Gestión Colaborativa, Control de Versiones y
# Organización Empresarial (Git, GitHub y Jira)
# Escenario B: Análisis de Ventas de una Pequeña Empresa
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE RUTAS
# Se usan rutas relativas para garantizar la reproducibilidad en Colab
# -----------------------------------------------------------------------------
BASE_DIR        = "/content/tp-ventas-utn"
RUTA_DATOS      = os.path.join(BASE_DIR, "datos", "ventas.csv")
RUTA_RESULTADOS = os.path.join(BASE_DIR, "resultados")
os.makedirs(RUTA_RESULTADOS, exist_ok=True)

# -----------------------------------------------------------------------------
# 2. IMPORTACIÓN Y VALIDACIÓN DEL DATASET
# -----------------------------------------------------------------------------
print("=" * 60)
print("  ANÁLISIS DE VENTAS - INDUMENTARIA DE FÚTBOL 2026")
print("=" * 60)

df = pd.read_csv(RUTA_DATOS, parse_dates=["fecha"])

columnas_requeridas = {"fecha", "producto", "cantidad", "precio_unitario"}
columnas_faltantes = columnas_requeridas - set(df.columns)
if columnas_faltantes:
    raise ValueError(f"Columnas faltantes: {columnas_faltantes}")

print(f"\n✔ Dataset cargado: {len(df)} registros.\n")

# -----------------------------------------------------------------------------
# 3. TRANSFORMACIÓN DE DATOS
# Se calcula el total por venta multiplicando cantidad por precio unitario
# -----------------------------------------------------------------------------
df["total_venta"] = df["cantidad"] * df["precio_unitario"]
df["mes"]         = df["fecha"].dt.to_period("M")
df["mes_nombre"]  = df["fecha"].dt.strftime("%b %Y")

# -----------------------------------------------------------------------------
# 4. INDICADORES GENERALES
# -----------------------------------------------------------------------------
ventas_totales      = df["total_venta"].sum()
cantidad_total      = df["cantidad"].sum()
ticket_promedio     = df["total_venta"].mean()
total_transacciones = len(df)

print("─" * 60)
print("  INDICADORES GENERALES")
print("─" * 60)
print(f"  Ingresos totales:            $ {ventas_totales:>12,.2f}")
print(f"  Unidades vendidas:           {cantidad_total:>12,}")
print(f"  Ticket promedio por venta:   $ {ticket_promedio:>12,.2f}")
print(f"  Total de transacciones:      {total_transacciones:>12,}")

# -----------------------------------------------------------------------------
# 5. PRODUCTO MÁS VENDIDO
# Se agrupa por producto para identificar los de mayor volumen e ingreso
# -----------------------------------------------------------------------------
ventas_por_producto = (
    df.groupby("producto")
    .agg(
        unidades_vendidas=("cantidad", "sum"),
        ingresos_generados=("total_venta", "sum")
    )
    .sort_values("unidades_vendidas", ascending=False)
)

producto_mas_vendido   = ventas_por_producto["unidades_vendidas"].idxmax()
producto_mayor_ingreso = ventas_por_producto["ingresos_generados"].idxmax()

print("\n" + "─" * 60)
print("  RANKING DE PRODUCTOS")
print("─" * 60)
print(ventas_por_producto.to_string())
print(f"\n  🏆 Producto con más unidades: {producto_mas_vendido}")
print(f"  💰 Producto de mayor ingreso: {producto_mayor_ingreso}")

# -----------------------------------------------------------------------------
# 6. VENTAS POR MES
# Permite identificar estacionalidad y meses pico de ventas
# -----------------------------------------------------------------------------
ventas_por_mes = (
    df.groupby("mes")
    .agg(
        ingresos=("total_venta", "sum"),
        unidades=("cantidad", "sum"),
        transacciones=("id", "count")
    )
    .reset_index()
    .sort_values("mes")
)
ventas_por_mes["periodo"] = ventas_por_mes["mes"].astype(str)

print("\n" + "─" * 60)
print("  VENTAS MENSUALES")
print("─" * 60)
print(ventas_por_mes[["periodo","ingresos","unidades","transacciones"]].to_string(index=False))

mes_pico  = ventas_por_mes.loc[ventas_por_mes["ingresos"].idxmax(), "periodo"]
mes_valle = ventas_por_mes.loc[ventas_por_mes["ingresos"].idxmin(), "periodo"]
print(f"\n  📈 Mes con mayor ingreso: {mes_pico}")
print(f"  📉 Mes con menor ingreso: {mes_valle}")

# -----------------------------------------------------------------------------
# 7. EXPORTAR RESUMEN MENSUAL
# Se guarda en /resultados para consulta sin re-ejecutar el análisis
# -----------------------------------------------------------------------------
ruta_resumen = os.path.join(RUTA_RESULTADOS, "resumen_mensual.csv")
ventas_por_mes.to_csv(ruta_resumen, index=False)
print(f"\n✔ Resumen exportado → {ruta_resumen}")

# -----------------------------------------------------------------------------
# 8. GENERACIÓN DE GRÁFICOS
# Tres visualizaciones: evolución mensual, ranking de productos y categorías
# -----------------------------------------------------------------------------
plt.rcParams.update({
    "font.family"       : "DejaVu Sans",
    "axes.spines.top"   : False,
    "axes.spines.right" : False,
    "axes.grid"         : True,
    "grid.alpha"        : 0.3,
    "grid.linestyle"    : "--",
})

etiquetas_mes = ventas_por_mes["periodo"].tolist()
ingresos_mes  = ventas_por_mes["ingresos"].tolist()

fig, axes = plt.subplots(3, 1, figsize=(12, 16))
fig.suptitle(
    "Análisis de Ventas — Indumentaria de Fútbol 2026",
    fontsize=16, fontweight="bold", y=0.98
)

# (a) Evolución mensual de ingresos
ax1 = axes[0]
ax1.fill_between(etiquetas_mes, ingresos_mes, alpha=0.15, color="#16a34a")
ax1.plot(etiquetas_mes, ingresos_mes, marker="o", color="#16a34a",
         linewidth=2.5, markersize=7)
for x, y in zip(etiquetas_mes, ingresos_mes):
    ax1.annotate(f"${y/1000:.0f}k", xy=(x, y), xytext=(0, 8),
                 textcoords="offset points", ha="center", fontsize=8)
ax1.set_title("Evolución de Ingresos por Mes", fontsize=13, pad=10)
ax1.set_ylabel("Ingresos ($)")
ax1.tick_params(axis="x", rotation=45)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:,.0f}"))

# (b) Top productos por unidades vendidas
ax2 = axes[1]
top5 = ventas_por_producto["unidades_vendidas"].sort_values(ascending=True).tail(5)
colores = ["#bbf7d0","#86efac","#4ade80","#22c55e","#16a34a"]
bars = ax2.barh(top5.index, top5.values, color=colores)
ax2.bar_label(bars, padding=4, fontsize=9)
ax2.set_title("Top 5 Productos — Unidades Vendidas", fontsize=13, pad=10)
ax2.set_xlabel("Unidades")
ax2.set_xlim(0, top5.max() * 1.15)

# (c) Participación por categoría
ax3 = axes[2]
ingresos_cat = df.groupby("categoria")["total_venta"].sum()
colores_pie  = ["#16a34a","#facc15","#3b82f6"]
wedges, texts, autotexts = ax3.pie(
    ingresos_cat, labels=ingresos_cat.index,
    autopct="%1.1f%%", colors=colores_pie,
    startangle=140, wedgeprops={"edgecolor":"white","linewidth":2}
)
for at in autotexts:
    at.set_fontsize(10)
ax3.set_title("Participación en Ingresos por Categoría", fontsize=13, pad=10)

plt.tight_layout(rect=[0, 0, 1, 0.97])

ruta_grafico = os.path.join(RUTA_RESULTADOS, "grafico_ventas.png")
plt.savefig(ruta_grafico, dpi=150, bbox_inches="tight")
plt.show()

print(f"\n✔ Gráfico guardado → {ruta_grafico}")
print("\n" + "=" * 60)
print("  ANÁLISIS COMPLETADO EXITOSAMENTE")
print("=" * 60)
