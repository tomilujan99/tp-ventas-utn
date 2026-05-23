#  Análisis de Ventas — Indumentaria de Fútbol 2026

**Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial**
Universidad Tecnológica Nacional · Tecnicatura Universitaria en Programación · 2026

---

##  Integrantes del Equipo

| Rol | Personaje | Responsabilidad |
|-----|-----------|-----------------||
| P1 — Líder y Organizador | Hugo | Gobernanza del repositorio, estructura de carpetas, README |
| P2 — Desarrollador Técnico | Paco | Script de análisis en Python, procesamiento del dataset |
| P3 — Revisor y QA | Luis | Peer Review, documentación interna, cierre de Pull Requests |

**Alumno:** Tomas Lujan
**Usuario GitHub:** tomilujan99
**Materia:** Organización Empresarial
**Institución:** UTN — Tecnicatura Universitaria en Programación (TUP)
**Año Lectivo:** 2026

---

##  Escenario Elegido

**Escenario B — Análisis de Ventas de una Pequeña Empresa**

El proyecto analiza un dataset simulado de ventas de indumentaria y accesorios de fútbol para generar indicadores básicos que permitan interpretar el desempeño comercial de la empresa durante el año 2026.

---

##  Estructura del Repositorio

- datos/ventas.csv — Dataset de ventas de fútbol (85 registros, 2026)
- scripts/analisis_ventas.py — Script principal de análisis en Python
- resultados/grafico_ventas.png — Gráficos generados por el análisis
- resultados/resumen_mensual.csv — Resumen de ventas por mes exportado
- README.md — Documentación del proyecto
- .gitignore — Exclusiones del repositorio

---

##  Dataset Utilizado

- **Archivo:** datos/ventas.csv
- **Origen:** Dataset simulado generado para fines educativos
- **Registros:** 85 transacciones de ventas
- **Período:** Enero — Diciembre 2026
- **Productos:** Camisetas, botines, pelotas y accesorios de fútbol

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | int | Identificador único de la transacción |
| fecha | date | Fecha de la venta (YYYY-MM-DD) |
| producto | string | Nombre del producto vendido |
| categoria | string | Categoría del producto |
| cantidad | int | Unidades vendidas |
| precio_unitario | float | Precio por unidad en pesos |

---

##  Indicadores Generados

- **Ingresos totales:** $39.220.500
- **Unidades vendidas:** 1.026
- **Producto más vendido:** Camiseta Selección Argentina (249 unidades)
- **Mes pico:** Diciembre 2026
- **Mes valle:** Enero 2026

---

##  Instrucciones para Ejecutar el Script

### En Google Colab

1. Clonar el repositorio:
   git clone https://github.com/tomilujan99/tp-ventas-utn.git

2. Ejecutar el script:
   python scripts/analisis_ventas.py

### En entorno local

1. Clonar el repositorio
2. Instalar dependencias: pip install pandas matplotlib
3. Ejecutar: python scripts/analisis_ventas.py

El script usa rutas relativas, ejecutarlo desde la raíz del repositorio.

---

##  Trazabilidad con Jira

| Commit | Issue Jira | Descripción |
|--------|------------|-------------|
| KAN-1 | Inicializar repositorio | Estructura de carpetas y README |
| KAN-2 | Desarrollar script | Dataset, análisis y gráficos |
| KAN-3 | Revisión QA | Peer Review y merge a main |

---

##  Seguridad

- El Personal Access Token nunca se expone en el código ni en el historial de commits.
- Se utilizó getpass para el ingreso seguro del token en Google Colab.
- El archivo .gitignore excluye archivos temporales y datos sensibles.

---

##  Dependencias

| Librería | Uso |
|----------|-----|
| pandas | Carga y procesamiento del dataset |
| matplotlib | Generación de gráficos |

---

*Organización Empresarial · UTN TUP · Año Lectivo 2026*
