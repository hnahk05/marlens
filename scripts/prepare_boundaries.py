import glob
import json
from pathlib import Path

RAW_DIR = Path("data/raw/thanglequoc/geojson")
OUT_PROVINCES = Path("data/raw/provinces_merged.geojson")
OUT_WARDS_HN = Path("data/processed/wards_hanoi.geojson")


def merge_provinces() -> None:
    features = []
    for path in sorted(glob.glob(str(RAW_DIR / "*" / "*.geojson"))):
        with open(path, encoding="utf-8") as f:
            feat = json.load(f)["features"][0]
        p = feat["properties"]
        loai = p["fullName"].removesuffix(p["name"]).strip()
        features.append(
            {
                "type": "Feature",
                "geometry": feat["geometry"],
                "properties": {
                    "ma_tinh": str(p["code"]).zfill(2),
                    "ten": p["name"],
                    "loai": loai,
                },
            }
        )
    OUT_PROVINCES.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PROVINCES, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": features}, f, ensure_ascii=False)
    print(f"Đã gộp {len(features)} tỉnh -> {OUT_PROVINCES}")


def merge_hanoi_wards() -> None:
    features = []
    for path in sorted(glob.glob(str(RAW_DIR / "01_ha_noi" / "wards" / "*.geojson"))):
        with open(path, encoding="utf-8") as f:
            feat = json.load(f)["features"][0]
        p = feat["properties"]
        loai = p["fullName"].removesuffix(p["name"]).strip()
        features.append(
            {
                "type": "Feature",
                "geometry": feat["geometry"],
                "properties": {
                    "ma_xa": str(p["code"]).zfill(5),
                    "ten": p["name"],
                    "loai": loai,
                    "ma_tinh": "01",
                },
            }
        )
    OUT_WARDS_HN.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_WARDS_HN, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": features}, f, ensure_ascii=False)
    print(f"Đã gộp {len(features)} xã/phường Hà Nội -> {OUT_WARDS_HN}")


if __name__ == "__main__":
    merge_provinces()
    merge_hanoi_wards()
    