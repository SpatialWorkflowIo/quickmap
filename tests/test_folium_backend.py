from quickmap.backends.folium_backend import _extract_points, _infer_bounds, _walk_coordinates, create_map


def test_walk_coordinates_skips_non_numeric_entries() -> None:
    points = []

    _walk_coordinates(["a", "b"], points)

    assert points == []


def test_extract_points_supports_nested_geometry_coordinates() -> None:
    feature_collection = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [1.0, 2.0]]],
                },
            }
        ],
    }

    points = _extract_points(feature_collection)

    assert (1.0, 2.0) in points
    assert (5.0, 6.0) in points


def test_infer_bounds_returns_none_when_no_points_are_present() -> None:
    feature_collection = {
        "type": "FeatureCollection",
        "features": [{"type": "Feature", "properties": {}, "geometry": {"type": "Point", "coordinates": []}}],
    }

    assert _infer_bounds(feature_collection) is None


def test_create_map_applies_bounds_when_points_exist() -> None:
    feature_collection = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {"type": "LineString", "coordinates": [[2.0, 48.0], [13.0, 52.0]]},
            }
        ],
    }

    fmap = create_map(feature_collection)

    assert fmap.get_bounds() == [[48.0, 2.0], [52.0, 13.0]]

