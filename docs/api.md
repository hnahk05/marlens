# Hợp đồng API v1

Người giữ: TV2. Đổi hợp đồng phải báo TV3, TV4 và sửa file này trong cùng PR.

- Mọi đường dẫn bắt đầu bằng `/api`, trả JSON UTF-8. Tài liệu tự sinh: http://localhost:8000/docs
- Lỗi trả mã HTTP kèm `{"detail": "..."}` (mặc định của FastAPI).
- Mã hành chính là **chuỗi**: `ma_tinh` 2 ký tự (Hà Nội là `"01"`), `ma_xa` 5 ký tự.
- Thiếu dữ liệu: `null`, không bao giờ điền 0. Số liệu mô phỏng: `loai_du_lieu = "mo_phong"`.
- Tọa độ WGS 84, thứ tự `[kinh độ, vĩ độ]`. Đơn vị: km², người/km², km, phút.
- Khi API chưa xong, TV3 dùng JSON giả đúng dạng này trong `frontend/public/mock/`.

## Danh sách endpoint

| Phương thức | Đường dẫn | Tham số | Trả về | Có từ |
| --- | --- | --- | --- | --- |
| GET | `/api/health` | – | `{"status": "ok"}` | GĐ1 |
| GET | `/api/provinces` | – | Danh sách tỉnh: `ma_tinh, ten, loai, dien_tich_km2, dan_so, mat_do` | GĐ2 |
| GET | `/api/provinces/{ma_tinh}/wards` | – | Danh sách xã: `ma_xa, ten, loai, ma_tinh, dien_tich_km2, dan_so, mat_do` | GĐ2 |
| GET | `/api/geo/provinces` | – | GeoJSON FeatureCollection, properties như `/api/provinces` | GĐ2 |
| GET | `/api/geo/wards` | `ma_tinh` (bắt buộc) | GeoJSON xã/phường của tỉnh | GĐ2 |
| GET | `/api/statistics/{ma}` | mã tỉnh hoặc mã xã | `ma, cap ("tinh"\|"xa"), ten, chi_tieu: [{ma_chi_tieu, ten, gia_tri, don_vi, ky, nguon, loai_du_lieu}]` | GĐ2 |
| GET | `/api/search` | `q` (≥ 2 ký tự), `limit` = 10 | `[{ma, cap, ten, ten_tinh, bbox: [minLng, minLat, maxLng, maxLat]}]` | GĐ3 |
| GET | `/api/filter` | `ma_tinh, dan_so_min, mat_do_min, chua_co_buu_cuc` | `[{ma, ten, dan_so, mat_do}]` | GĐ3 |
| GET | `/api/pois` | `bbox`, `loai` (`cho, buu_cuc, my_pham, an_uong, ...`) | GeoJSON điểm, properties `id, ten, loai` | GĐ3 |
| GET | `/api/sources` | – | `[{lop, nguon, ky, ghi_chu}]` | GĐ3 |
| GET | `/api/nganh` | – | `[{ma_nganh, ten, trong_so_mac_dinh}]` | GĐ3 |
| POST | `/api/mpi` | body JSON có `nganh` | `trong_so_da_chuan_hoa, xep_hang, geojson` | GĐ3 bản đầu, GĐ4 đủ |
| GET | `/api/compare` | `ma` = 2–3 mã, cách nhau dấu phẩy | Thống kê và MPI từng khu vực | GĐ4 |

Trọng số gửi lên `/api/mpi` phải ≥ 0 và tổng > 0, nếu không trả 422. Mã không tồn tại trả 404.

## Ví dụ 1: một Feature trong `/api/geo/wards`

```json
{"type": "Feature",
 "geometry": {"type": "MultiPolygon", "coordinates": [...]},
 "properties": {"ma_xa": "00004", "ten": "Phường A", "ma_tinh": "01",
                "dan_so": 48200, "mat_do": 12400.5, "mpi": null}}
```

## Ví dụ 2: `POST /api/mpi`

Gửi lên (bỏ trống `trong_so` thì dùng trọng số mặc định của ngành):

```json
{"ma_tinh": "01", "nganh": "my_pham",
 "trong_so": {"dan_so": 3, "mat_do": 2, "so_diem_ban": 2,
              "khoang_cach_buu_cuc": 1.5, "so_doi_thu": 1.5}}
```

Nhận về (trọng số đã chia lại để tổng = 1):

```json
{"trong_so_da_chuan_hoa": {"dan_so": 0.3, "mat_do": 0.2, "so_diem_ban": 0.2,
                           "khoang_cach_buu_cuc": 0.15, "so_doi_thu": 0.15},
 "xep_hang": [
   {"ma": "00004", "ten": "Phường A", "mpi": 81.75, "hang": 1,
    "thanh_phan": {"dan_so": 0.9, "mat_do": 0.8}, "thieu_du_lieu": []}],
 "geojson": {"type": "FeatureCollection", "features": []}}
```

## Ví dụ 3: `GET /api/statistics/{ma}`

```json
{"ma": "01", "cap": "tinh", "ten": "Hà Nội",
 "chi_tieu": [{"ma_chi_tieu": "dan_so", "ten": "Dân số", "gia_tri": null,
               "don_vi": "người", "ky": "2025", "nguon": "...", "loai_du_lieu": "quan_sat"}]}
```
