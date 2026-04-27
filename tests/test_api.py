import json
from pathlib import Path

import pytest

from quickmap.api import _load_geojson, quickmap


def _write_geojson(path: Path) -> None:
    payload = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "One"},
                "geometry": {"type": "Point", "coordinates": [10.0, 20.0]},
            }
        ],
    }
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_quickmap_writes_default_html(tmp_path: Path) -> None:
    source = tmp_path / "data.geojson"
    _write_geojson(source)

    output = quickmap(source)

    assert output == tmp_path / "data_map.html"
    assert output.exists()
    html = output.read_text(encoding="utf-8")
    assert "leaflet" in html
    assert "fitBounds" in html


def test_quickmap_writes_custom_html_and_parent_directory(tmp_path: Path) -> None:
    source = tmp_path / "data.geojson"
    _write_geojson(source)
    output = tmp_path / "nested" / "custom.html"

    result = quickmap(source, output_html=output, zoom_start=4)

    assert result == output
    assert output.exists()


def test_load_geojson_raises_for_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        _load_geojson(tmp_path / "missing.geojson")


def test_load_geojson_raises_for_invalid_json(tmp_path: Path) -> None:
    broken = tmp_path / "broken.geojson"
    broken.write_text("not-json", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid JSON"):
        _load_geojson(broken)


def test_load_geojson_raises_for_non_feature_collection(tmp_path: Path) -> None:
    wrong = tmp_path / "wrong.geojson"
    wrong.write_text('{"type": "Point", "coordinates": [0, 0]}', encoding="utf-8")

    with pytest.raises(ValueError, match="FeatureCollection"):
        _load_geojson(wrong)

