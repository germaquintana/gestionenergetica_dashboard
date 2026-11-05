# Dashboard de Gestión Energética Municipal · Recoleta

**Versión pública inicial 0.1 | Corte 05-11-2026 | Exploratoria, no oficial.** Sitio estático construido siguiendo la **estructura de información** de la plataforma [Gestiona Energía, Ministerio de Energía](https://gestionaenergia.minenergia.cl/). **No sustituye ni sincroniza** la plataforma institucional ni acredita cumplimiento de la Ley 21.305.

**[Abrir archivo HTML](index.html)** · [Datos públicos resumidos](data/indicadores_publicos.json) · [Modelo y controles de publicación](METODOLOGIA_Y_PUBLICACION.md)

## Objetivo y organización visual
En vez de organizar el tablero solo como una auditoría de boletas, sigue los módulos de la capacitación de Gestiona Energía de **10-09-2026** y su concepto **Edificio → Unidad → Energéticos y suministros → Consumos**. Navegación:

| Pantalla pública | Relación con esquema ministerial | Qué se presenta |
|---|---|---|
| **Inicio** | Indicadores y unidades a cargo | 8 referencias de unidades visibles en la plataforma (corte 14-10-2026); 1 unidad reportable en esa fotografía, no un estado vigente; 24 referencias educacionales históricas |
| **Mi Unidad** | Información General, Energéticos, Sistemas | Tabla de 8 referencias, búsqueda y filtro por sector; exportación CSV sin datos contractuales; muestra brechas de atributos |
| **Gestión de Unidad** | Consumos por energético y compras | Tipos de combustible/energía a corroborar, consumo energético 2025 explícitamente **sin serie publicada validada**, módulo diferenciado de agua con indicadores agregados |
| **Reportes y cobertura** | Calidad, integridad, criterios de alcance | Matriz de información faltante y cortes legales, sin inferir reportes o cumplimiento |
| **Configuración y fuentes** | Usuarios, unidades, catastro | Explicación de quién puede gestionar los datos realmente, metodología y fuentes, sin datos personales |

### Modelo de datos
1. **Edificio:** infraestructura y domicilio físico (puede contener varias unidades).
2. **Unidad:** dependencia/espacio de la plataforma (no equivale automáticamente a edificio).
3. **Energético:** electricidad, gas, combustibles, etc. La existencia de una fuente por unidad requiere confirmación.
4. **Suministro/medidor:** relación con unidad/edificio con posibles medidores compartidos; **ID cliente y serie medidor no se publican**.
5. **Consumo:** fuente, período, unidad física, cantidad y validación; **2025 energético de reporte 2026: 01-11-2024 a 31-10-2025** (art. 7, Reglamento Ley 21.305).
6. **Gestión hídrica:** m³ de agua separados en módulo complementario. Para el Sistema Estado Verde existen mecanismos de reporte de agua, pero **estas cifras públicas NO acreditan carga en plataforma**.

### Cifras de demostración 0.1
- **8** unidades vistas en plataforma a corte histórico ministerial 14-10-2026; no universo total de recintos. De ellas **1** identificada como reportable en ese corte; la situación de reportes/validación institucional posterior no está comprobada.
- **24** referencias históricas de educación (19 RBD escolares en fichas MIME, 5 códigos JUNJI VTF), que **no equivalen a 24 unidades ni a padrón vigente validado**.
- Agua 2025 calendario: **492.410,56 m³** en 269 cuentas asociadas al nombre municipal; subconjunto por RUT municipal, **264 cuentas y 454.464,56 m³**. Diferencia de titularidad en cinco cuentas por verificar. Los valores no describen el universo oficial de unidades de la plataforma ni están adscritos a edificios.
- 2025 según `USO` original SISS: áreas verdes 229.707 m³; educación 143.392 m³; salud 19.434 m³; administración 99.877,56 m³. **Clasificación original no certificada:** contiene divergencias por dirección, se mantiene como categoría de fuente.
- Agua enero–julio 2026 **391.019,62 m³** (parcial), nunca proyectar sin aviso ni comparar directamente contra 2025 completo.
- **No se presentan** consumos de energía 2025 o gastos por medidor, porque su conciliación con suministros, vigencia, unidades y facturas originales continúa abierta.

## Seguridad y gobernanza
**Repositorio público:** solamente HTML, indicadores agregados o referencias documentales públicas y validadores. No subir RUT, número de cuenta/cliente, serie de medidor, facturas, datos de proveedores por inmueble, correos personales, expediente ministerial ni documentación interna. No trasladar borradores o archivos completos desde el repositorio privado. El histórico de GitHub público puede conservar datos incluso si se borran posteriormente.

**Repositorio privado de trabajo:** `germaquintana/Gestionambientaltrabajo_recoleta`, expediente `GA-T-2026-0008`, conserva las fuentes originales, evidencias, Trello, responsables y estados. Este repositorio público **no** se convierte en fuente de verdad de otra dirección ni habilita instrucciones a DAEM, DESAL o DAF.

**Lista blanca de actualización:** solo campos ya aprobados en `data/indicadores_publicos.json`, agregados sin identificación contractual y con fecha/fuente/advertencias. Antes de publicar una versión de datos, validar autorización de difusión, sumatorias y riesgo de identificación indirecta en grupos pequeños. No automatizar traslado de datos desde Drive o GitHub privado sin un paso de revisión humana.

## Publicación mediante GitHub Pages (sin infraestructura compleja)
Este repo es **público**. El archivo `index.html` está en la raíz y no requiere compilación, servicios, APIs ni frameworks.

1. En el repositorio abrir **Settings → Pages**.
2. Elegir **Build and deployment → Source: Deploy from a branch**.
3. Seleccionar **Branch: main** y **Folder: /(root)**, guardar.
4. Comprobar en **Visit site** cuando el despliegue figure exitoso; revisar con navegador normal e incógnito.
5. URL prevista, **no darla por confirmada hasta verificar Pages**: `https://germaquintana.github.io/gestionenergetica_dashboard/`.

**El repositorio público y el archivo HTML pueden existir antes de habilitar Pages.** Subir un `index.html` no prueba que el hosting web esté activo.

## Verificación y mantenimiento
- `python3 validar_publicacion.py`: comprueba 8 unidades, suma hídrica, corte, categorías, concordancia entre JSON e HTML y ausencia de ciertos campos contractuales.
- Abrir `index.html` descargado en navegador: menú cinco módulos, filtro sector/búsqueda, exportación CSV, gráfico de agua y versión móvil.
- Para actualizar: preparar datos agregados, revisarlos, modificar JSON y el snapshot embebido en HTML en el mismo commit; ejecutar validador y verificar GitHub Pages. **No** conecta ni envía información a Gestiona Energía.

## Fuentes normativas y metodológicas
- [Ministerio de Energía: Ley 21.305, reglamento y artículo 7 sector público](https://sectorpublico.gestionaenergia.cl/?page_id=6818).
- [Biblioteca oficial: capacitación Ley 21.305 año 2026 y «Uso de la Plataforma»](https://sectorpublico.gestionaenergia.cl/?page_id=15).
- La fotografía local 14-10-2026 y consolidados hídricos son **antecedentes técnicos internos resumidos y no certificados para difusión institucional**. El dashboard no reproduce esos documentos privados.

---
**Advertencia:** Esta visualización es exploratoria, no oficial; no certifica consumo energético, número definitivo de inmuebles, presentación de reportes, cumplimientos ni actos administrativos.
