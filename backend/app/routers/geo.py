from fastapi import APIRouter

from app.db import get_conn

router = APIRouter()

SQL_TINH = """
SELECT json_build_object('type', 'FeatureCollection', 'features',
  COALESCE(json_agg(json_build_object(
    'type', 'Feature',
    'geometry', ST_AsGeoJSON(ST_SimplifyPreserveTopology(geom, 0.005))::json,
    'properties', json_build_object('ma_tinh', ma_tinh, 'ten', ten,
      'dan_so', dan_so, 'mat_do', ROUND(dan_so / NULLIF(dien_tich_km2, 0), 1))
  )), '[]'::json)) AS fc
FROM tinh"""


@router.get("/geo/provinces")
def geo_provinces():
    with get_conn() as conn:
        return conn.execute(SQL_TINH).fetchone()["fc"]
