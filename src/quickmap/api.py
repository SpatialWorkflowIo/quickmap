from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .backends import create_map


def _load_geojson(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"GeoJSON file was not found: {path}")

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in file: {path}") from exc

    if not isinstance(raw, dict) or raw.get("type") != "FeatureCollection":
        raise ValueError("GeoJSON input must be a FeatureCollection object")

    return raw


def quickmap(
    data_geojson: str | Path,
    output_html: str | Path | None = None,
    *,
    tiles: str = "OpenStreetMap",
    zoom_start: int = 2,
) -> Path:
    """Generate a shareable HTML map from a GeoJSON file path."""
    input_path = Path(data_geojson)
    feature_collection = _load_geojson(input_path)

    if output_html is None:
        output_path = input_path.with_name(f"{input_path.stem}_map.html")
    else:
        output_path = Path(output_html)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fmap = create_map(feature_collection, tiles=tiles, zoom_start=zoom_start)
    fmap.save(str(output_path))

    return output_path

