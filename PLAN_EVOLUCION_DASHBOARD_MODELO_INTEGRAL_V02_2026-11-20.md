# Plan de evolución V0.2 — Dashboard Integral de Gestión Energética Municipal

**Fecha de incorporación:** 20-11-2026 (Chile).  
**Estado:** **backlog técnico aprobado como línea de desarrollo futuro; implementación pendiente**.  
**Expediente de gestión:** `GA-T-2026-0008` (control institucional, fuera de este repositorio público).  
**Repositorio de implementación:** este mismo `germaquintana/gestionenergetica_dashboard`, rama `main`.  
**Origen funcional:** modelo integral de Gestión Energética Municipal 2026–2027, con seis procesos; documento de referencia bajo custodia institucional, no replicado aquí.

## Decisión de continuidad

La prioridad material sigue siendo completar la regularización ministerial y la base energética: obligación y consumos 2025, catastro de unidades y suministros, conciliación de facturas con responsables y evidencia verificable. **Este plan no cambia esa prioridad ni declara cerradas las obligaciones.**

Se conservarán el sitio estático existente, su inventario, metodología, validador y datos públicos aprobados; el rediseño evoluciona la estructura de 5 módulos exploratorios a **Inicio + 6 subsistemas**. No crear otro dashboard ni otra fuente de verdad. La etapa de diseño y navegación puede avanzar en paralelo a la conciliación de consumos, mostrando datos faltantes explícitamente.

## Arquitectura funcional aprobada

**Inicio ejecutivo:** esquema interactivo de los seis subsistemas interconectados, navegación por clic y menú de pestañas, indicadores globales con fecha de corte y etiquetas de validación, alertas, próximos hitos y explicación de fuentes.

| Identificador | Pestaña | Contenido mínimo | Reutilización o dependencia |
|---|---|---|---|
| INI | **Inicio** | Flujo interactivo; tarjetas de unidades, suministros, cobertura, kWh, combustibles, CLP, cumplimiento, calidad, medidas; alertas ejecutivas | Inventario y agregados existentes; datos no validados se muestran sin cifra |
| S01 | **Cumplimiento** | Ley 21.305, obligaciones, períodos exigibles, gestores, aceptación documental, alcance y estado del reporte | Solo estados ministeriales que tengan evidencia y autorización de publicación |
| S02 | **Catastro** | Edificio → unidad → energético → suministro, sectores, responsables por rol, validación de cobertura | Reutilizar «Mi Unidad», 8 referencias históricas sin afirmar universo completo |
| S03 | **Consumos** | Electricidad, gas, combustibles y flota, comparaciones temporales; agua separada como componente complementario | Reutilizar «Gestión de Unidad» y sus agregados; kWh/gastos todavía pendientes |
| S04 | **Calidad de datos** | Fuentes, cobertura, diferencias, duplicados potenciales, estados pendiente/observado/validado/no aplica | Reutilizar «Reportes y cobertura», sin mostrar números contractuales |
| S05 | **Reportabilidad** | Cumplimiento documental, cronología de gestiones, reportes por período, brechas y comprobantes | Enlaces a evidencias públicas únicamente; no simular carga ministerial |
| S06 | **Eficiencia** | Oportunidades, tecnologías, medidas, seguimiento, estimaciones con supuestos y cartera 2027 | Proyectos solo cuando se verifique alcance, estado y permiso de difusión |

**Patrón de cada pestaña:** resumen, KPI, gráficos/tablas y filtros, gestiones, evidencias públicas, próximos pasos. El menú y los seis nodos del esquema llevan al mismo estado de navegación, con retorno fácil a Inicio y diseño móvil accesible.

## Unidades de trabajo futuras (E-07 / dashboard)

### D01 — Auditoría y diseño funcional
- Cotejar el sitio `index.html`, `README.md`, `METODOLOGIA_Y_PUBLICACION.md`, `data/indicadores_publicos.json` y `validar_publicacion.py` con los seis procesos del modelo integral.
- Elaborar matriz de equivalencias 5 módulos actuales ↔ 6 subsistemas nuevos; conservar funciones, filtros, CSV, advertencias y validación existentes.
- Definir estructura de información y estado de datos por indicador, sin conectar a fuentes privadas desde cliente.

**Aceptación:** inventario de componentes, mapa de navegación y matriz de fuentes/limitaciones comprobados contra archivos reales.

### D02 — Panel General navegable
- Rehacer portada con diagrama dinámico de seis procesos y tarjetas KPI de alcance global; los nodos activan la pestaña correspondiente.
- KPI sin respaldo: `PENDIENTE` o `NO VALIDADO` (nunca `0` ni dato inventado); indicar fecha y fuente.
- Preservar las ocho referencias históricas como registros visibles de corte específico, no total municipal validado.

**Aceptación:** 6/6 nodos y pestañas navegables, Inicio accesible desde cualquier subsistema, responsive, estado sin datos válido.

### D03 — Subsistemas, filtros y trazabilidad
- Migrar componentes existentes a S02, S03, S04 sin pérdida de capacidades.
- Construir S01, S05, S06 con estructura común; distinguir fase real del proyecto de resultado ya medido.
- Filtros por período, dependencia y fuente solo cuando existan claves públicas válidas; no asumir cardinalidad edificio=unidad=medidor.

**Aceptación:** 6/6 pestañas funcionales, sin duplicación de consumos de medidores compartidos; filtros y enlaces comprobados.

### D04 — QA, seguridad y entrega web
- Ejecutar y ampliar `validar_publicacion.py`, pruebas de navegación/teclado y responsive, revisión de rutas, consistencia JSON ↔ HTML y ausencia de datos restringidos.
- Actualizar versión, metodología, README y evidencias del despliegue; comprobar HTTP y versión servida antes de entregar URL.
- **No** habilitar Pages, enviar reportes ni publicar datos nuevos con acceso no autorizado.

**Aceptación:** QA documentado, commit y despliegue web distinguidos, sitio vivo verificado externamente o estado de publicación pendiente informado sin exageración.

## Secuencia e interdependencias

**Trabajo prioritario del expediente (E00–E06):** comprobantes de reportabilidad 2025, gestión de Profesor Zañartu 803, recepción/conciliación DAF, DAEM, DESAL, Servicios Generales, extracción de lecturas por períodos, validación de catastro y datos, sin duplicar requerimientos ya enviados.

**Posteriormente (E07):** D01 → D02 → D03 → D04. Se pueden preparar diseño y componentes con los datos públicos actuales sin esperar todos los consumos, pero **publicar cifras energéticas nuevas exige validación y autorización**.

**Producto clave esperado:** URL web viva del dashboard integral, **no** únicamente `index.html`, commit o archivo local. El enlace previsto de Pages en README no acredita por sí solo que esté activo.

## Controles permanentes
- Los valores sin fuente no son cero. Separar: `VALIDADO`, `PRELIMINAR`, `PENDIENTE`, `NO APLICA`.
- Período ministerial 2026: 01-11-2024 a 31-10-2025; agua calendario 2025 y agua 2026 parcial no se comparan sin normalización.
- No publicar RUT, cuentas, contratos, facturas, medidores, datos personales, contraseñas ni expediente privado.
- La coordinación institucional, GA-T, RUN y validación de origen residen en el repositorio privado. Este archivo es **plan técnico de implementación**, no reemplazo de la cola canónica ni prueba de despliegue.
- Cambios de código/datos solo con control SHA, comprobación de concurrencia y pruebas; actos de publicación sujetos a permisos y autorización institucional.

## Estado al 20-11-2026
- `README.md`: documenta v0.1 y cinco pantallas.
- `index.html`: ofrece navegación y filtros de cinco módulos, no el esquema interactivo integral.
- `data/indicadores_publicos.json`: ocho referencias históricas, energía 2025 y costo sin total publicable validado, agua como información complementaria.
- La activación y funcionamiento público de GitHub Pages **no están acreditados** en esta revisión.
- **D01–D04 quedan pendientes de implementación**; este registro no presenta una maqueta entregada.
