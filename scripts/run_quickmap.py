from pathlib import Path

from quickmap import quickmap

if __name__ == "__main__":
    input_file = Path("examples/data.geojson")
    output_file = quickmap(input_file)
    print(f"Map generated: {output_file}")

