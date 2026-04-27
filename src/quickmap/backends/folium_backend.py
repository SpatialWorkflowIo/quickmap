from __future__ import annotations

from typing import Any

import folium


def _walk_coordinates(node: Any, points: list[tuple[float, float]]) -> None:
    if isinstance(node, (list, tuple)):
        if len(node) >= 2 and all(isinstance(value, (int, float)) for value in node[:2]):
            points.append((float(node[0]), float(node[1])))
            return
        for child in node:
            _walk_coordinates(child, points)


def _extract_points(feature_collection: dict[str, Any]) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for feature in feature_collection.get("features", []):
        geometry = feature.get("geometry") or {}
        coordinates = geometry.get("coordinates")
        _walk_coordinates(coordinates, points)
    return points


def _infer_bounds(feature_collection: dict[str, Any]) -> list[list[float]] | None:
    points = _extract_points(feature_collection)
    if not points:
        return None

    lons = [point[0] for point in points]
    lats = [point[1] for point in points]
    return [[min(lats), min(lons)], [max(lats), max(lons)]]


def create_map(
    feature_collection: dict[str, Any],
    tiles: str = "OpenStreetMap",
    zoom_start: int = 2,
) -> folium.Map:
    """Create a Folium map for a GeoJSON feature collection."""
    fmap = folium.Map(location=[0.0, 0.0], tiles=tiles, zoom_start=zoom_start)
    folium.GeoJson(feature_collection, name="quickmap-data").add_to(fmap)

    bounds = _infer_bounds(feature_collection)
    if bounds:
        fmap.fit_bounds(bounds)

    return fmap

