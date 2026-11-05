#!/usr/bin/env python3
"""Contrato mínimo de publicación segura del dashboard exploratorio Recoleta."""
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
payload = json.loads((ROOT / "data/indicadores_publicos.json").read_text(encoding="utf-8"))
html = (ROOT / "index.html").read_text(encoding="utf-8")
r = re.search(
    r'<script id="snapshot" type="application/json">([\s\S]*?)</script>',
    html,
)
assert r, "Falta snapshot JSON local"
inline = json.loads(r.group(1))
assert inline == payload, "HTML y JSON deben actualizarse juntos"
assert len(payload["inventario"]["unidades"]) == 8
assert payload["inventario"]["unidades_visibles"] == 8
assert payload["inventario"]["unidades_con_reporte_segun_foto"] == 1
assert (
    payload["inventario"]["escolares_rbd_historicos"]
    + payload["inventario"]["vtf_historicos"]
    == payload["inventario"]["referencias_historicas_educacion"]
    == 24
)
assert payload["base_normativa"]["inicio"] == "2024-11-01"
assert payload["base_normativa"]["fin"] == "2025-10-31"
assert payload["energia"]["kwh_total_2025_publicable"] is None
assert abs(
    sum(x["m3"] for x in payload["agua"]["categorias_originales_2025"])
    - payload["agua"]["consumo_m3_2025_nombre"]
) < 0.00001
assert payload["agua"]["consumo_m3_2025_nombre"] == 492410.56
assert payload["agua"]["consumo_m3_2025_rut"] == 454464.56
assert payload["agua"]["consumo_m3_2026_ene_jul_nombre"] == 391019.62
assert len({x["ref"] for x in payload["inventario"]["unidades"]}) == 8
assert all(x["ubicacion"] and x["sector"] and x["estado"] for x in payload["inventario"]["unidades"])
assert all(
    f'data-view="{v}"' in html
    for v in ("inicio", "mi-unidad", "gestion-unidad", "reportes", "configuracion")
)
assert "Gestión de Unidad" in html and "Mi Unidad" in html
assert "Gestión del agua" in html
assert "No equivale a agua reportada en Gestiona Energía" in html

public_data = (ROOT / "data/indicadores_publicos.json").read_text(encoding="utf-8")
for field in ("numero_cuenta", "cuenta_original", "serie_medidor", "numero_serie_medidor", "rut_titular", "telefono", "correo_personal", "folio_individual"):
    assert field not in public_data.lower(), f"Campo contractual prohibido: {field}"
assert not re.search(r"(?<!\d)\d{1,2}\.\d{3}\.\d{3}-[\dKk](?!\d)", public_data)
assert not re.search(r"(?<!\d)\d{7,8}-[\dKk](?!\d)", public_data)

scripts = re.findall(r"<script(?:\s+[^>]*)?>([\s\S]*?)</script>", html)
assert len(scripts) == 2, "HTML debe tener snapshot y un script de interfaz"
js = scripts[-1]
if shutil.which("node"):
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "dashboard_check.js"
        path.write_text(js, encoding="utf-8")
        subprocess.run(["node", "--check", str(path)], check=True)
else:
    print("AVISO: Node.js no disponible, omito análisis sintáctico JS")
print("OK: contrato público, cortes, suma SISS, HTML/JSON, datos privados y menú verificados")
