CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS unaccent;

CREATE TABLE tinh (
  ma_tinh CHAR(2) PRIMARY KEY, ten TEXT NOT NULL, loai TEXT,
  dien_tich_km2 NUMERIC, dan_so INTEGER, ky TEXT, nguon TEXT,
  geom geometry(MultiPolygon, 4326));

CREATE TABLE xa_phuong (
  ma_xa CHAR(5) PRIMARY KEY, ten TEXT NOT NULL, loai TEXT,
  ma_tinh CHAR(2) REFERENCES tinh(ma_tinh),
  dien_tich_km2 NUMERIC, dan_so INTEGER, ky TEXT, nguon TEXT,
  geom geometry(MultiPolygon, 4326));

CREATE TABLE poi (id SERIAL PRIMARY KEY, ten TEXT, loai TEXT, ma_xa CHAR(5),
  geom geometry(Point, 4326));

CREATE TABLE nguon_du_lieu (lop TEXT, nguon TEXT, ky TEXT, ghi_chu TEXT);

CREATE INDEX ON tinh USING GIST (geom);
CREATE INDEX ON xa_phuong USING GIST (geom);
CREATE INDEX ON poi USING GIST (geom);
