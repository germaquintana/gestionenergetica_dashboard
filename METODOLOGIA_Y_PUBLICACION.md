# Modelo de interoperabilidad y control de publicación

**Proyecto:** tablero público exploratorio de Gestión Energética Municipal de Recoleta. **Fecha de corte:** 05-11-2026. **Control privado:** `GA-T-2026-0008`.

## 1. Alineamiento con Gestiona Energía (Ministerio de Energía)

Se emplean los nombres y relaciones de la capacitación ministerial del **10 de septiembre de 2026** [«3. Uso de la Plataforma» en Biblioteca](https://sectorpublico.gestionaenergia.cl/?page_id=15), junto al [manual de la plataforma](https://sectorpublico.gestionaenergia.cl/?page_id=6818):

| Estructura ministerial | Clave conceptual interna | Visualización pública |
|---|---|---|
| Edificio / complejo | `edificio_id`, dirección física, atributos técnicos | Dirección de referencia y estado, nunca identificador privado |
| Mi Unidad → Información General | `unidad_id`, relación edificio-unidad, uso, área y superficie | Catastro de 8 referencias y brechas; sin declarar completitud |
| Mi Unidad → Energéticos | `energetico_id`, fuente, vigencia y relación con unidad | Catálogo de fuentes posibles; no inferir que cada unidad las utiliza |
| Mi Unidad → Sistemas | Equipos, calefacción, agua caliente, FV, iluminación, envolvente | Campos pendientes; solo mostrar proyectos comprobados más adelante |
| Gestión de Unidad → Consumos | `suministro_id`, cuenta, medidor, lectura inicio/fin, cantidad, unidad, monto, factura, asignación y revisión | Totales agregados o «sin datos» hasta validar; nunca series/medidores por recinto sin autorización |
| Reportes | Alcance de unidades, período, estado de revisión y prueba del envío | Controles de completitud, **nunca declaración de cumplimiento sin evidencia ministerial** |
| Configuración → Unidades/Usuarios | Alta/edición/adscripción de unidades y gestores autorizados | Solo explicación; el dashboard no modifica registros ni define responsables |
| Estado Verde → Gestión de Agua, cuando aplique | m³ agua potable; otros campos SEV según requisito | **Módulo complementario separado** del consumo energético del art. 7 |

**Cardinalidad:** un edificio puede contener varias unidades; una unidad puede asociarse a varios suministros; un medidor puede ser compartido; una dirección puede corresponder a varias cuentas. La llave de consumo incluye suministro, período, fuente y documento. **No agregar los consumos de un mismo medidor compartido a cada unidad sin regla de distribución acreditada**.

## 2. Cortes y reportabilidad

- **Ley 21.305 / artículo 7 / DS 28:** para **reporte 2026**, período de consumos **01-11-2024 al 31-10-2025**. No confundir con año calendario 2025 del módulo de agua.
- Según la [guía ministerial del artículo 7](https://sectorpublico.gestionaenergia.cl/?page_id=6818) se revisan condiciones como superficie construida de 500 m² o más, carga de ocupación inferior a 10 m² por persona, salud y laboratorios. Existen exclusiones por medidor compartido o falta de acceso a facturas. Se requiere **evidencia por unidad y criterio de alcance**, no extrapolación por dirección.
- **Fotografía histórica** de Recoleta a 14-10-2026: ocho unidades visibles y una identificada como obligada a reportar. **No certifica hoy** total de inmuebles, carga anual, reporte exitoso, cumplimiento o situación de otras instalaciones.
- **24 referencias educativas:** agrupación histórica (19 escolares y cinco VTF), no son automáticamente 24 inmuebles ni 24 unidades actuales. El registro público no crea responsabilidades para DAEM.
- **Agua:** `USO` de la planilla SISS representa una clasificación de proveedor que se sabe contradictoria entre hojas para algunas cuentas; el panel muestra **categorías originales agregadas** con advertencias. No imputa la categoría a unidades de la plataforma.

## 3. Diccionario mínimo para futura integración privada
| Campo | Descripción y prueba | Publicable en 0.1 |
|---|---|---|
| `edificio_id` | Identificador estable de inmueble/sede; dirección y catastro físico | No |
| `unidad_id` | ID oficial Gestiona Energía cuando se corrobore con plataforma | No |
| `sector` | Área referencial del sitio | Sí, sin asignación jerárquica a terceros |
| `uso_unidad` | Uso acreditado por unidad y fecha | Cuando se valide |
| `superficie_m2`, `funcionarios` | Denominadores con fuente y período | No mientras no se validen |
| `energetico` | Fuente activada/consumida por unidad | No sin facturas |
| `cuenta_cliente`, `rut_titular`, `serie_medidor` | Identificadores contractuales | **No** |
| `fecha_inicio_lectura`, `fecha_fin_lectura`, `kwh`, `litros` | Consumos cuantitativos respaldados por boleta | Solo si agregados y autorizados |
| `importe_clp` | Cargo facturado del período (no confundir con pago ni obligación) | No hasta conciliación DAF |
| `calidad`, `corte`, `fuente` | Verificación y trazabilidad de observación | Sí, en forma no sensible |
| `consumo_agua_m3` | Serie separada, calendario anual o parcial por etiqueta SISS | Solo agregado público, con límites explícitos |
| `estado_reporte` | Resultado real de plataforma con acta o export oficial | No sin respaldo |

## 4. Contrato de datos para la web
- `data/indicadores_publicos.json` contiene un **snapshot de datos permitidos**, agregado e independiente del expediente. Se replica dentro del HTML solo para funcionar sin red (file://); ambas representaciones **deben coincidir**.
- La interfaz pública **no usa token, API privada, credenciales ni consulta Gmail, Drive o Trello**. No puede actualizar tareas institucionales ni alterar Gestona Energía.
- La ausencia de valor se representa mediante `null` o texto **Sin datos**, nunca como cero.
- Publicar solo datos con fuente, corte y estado; si se desconoce vigencia, usar expresiones «referencia histórica», «candidato» o «por verificar».
- Mantener el módulo de agua **dentro** de navegación Gestión de Unidad, pero claramente diferenciado del reporte energético legal. No convertir m³ a kWh.
- No publicar datos de grupos muy pequeños o identificadores que permitan reconstruir facturación de terceros. Revisión humana de difusión previa a nuevos detalles.

## 5. Criterios de aceptación
1. Menú operativo de cinco módulos (Inicio, Mi Unidad, Gestión de Unidad, Reportes, Configuración).
2. Ocho referencias en tabla pública y CSV con búsqueda/filtro; 24 DAEM solo como conjunto histórico independiente.
3. Período de reporte energético 2026 visible como **2024-11-01 a 2025-10-31**.
4. Consumo de energía anual **no visible como cero**.
5. Agua 2025: cuatro categorías suman exactamente **492.410,56 m³**; para 264 cuentas RUT son **454.464,56 m³**; enero-julio 2026 parcial.
6. Publicación solo incluye activos explicitados: HTML, JSON resumido, validador, documentación y configuración CI. No expedientes.
7. `python3 validar_publicacion.py` aprueba contrato; JS compila; al habilitar Pages se comprueba URL desde navegador humano.

## 6. Fuentes, límites y continuación
- [Portal Gestiona Energía, requisitos Ley 21.305 artículo 7](https://sectorpublico.gestionaenergia.cl/?page_id=6818).
- [Biblioteca oficial 2026](https://sectorpublico.gestionaenergia.cl/?page_id=15).
- La documentación privada de Recoleta y la fuente SISS **no se replican** en este repositorio. Sus cifras publicadas están calificadas como exploratorias y requieren validación de difusión.
- **Próxima fase:** tras confirmación humana de catastro DAEM/DESAL/DAF, publicación progresiva de consumos energéticos y factores de intensidad (kWh/m², kWh/funcionario), con denominadores y períodos idénticos; no crear indicadores artificiales desde boletas de agua o pagos contables.
- Publicación GitHub Pages a cargo del usuario administrador en `Settings > Pages > Deploy from a branch > main /(root)`; no declarar desplegado hasta que confirme `Visit site`.

**No se confiere autoridad sobre otras direcciones ni se certifica cumplimiento ministerial.**
