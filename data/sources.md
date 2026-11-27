# Nguồn dữ liệu – MarLens

## 1. Ranh giới hành chính (Giai đoạn 1)

### 1.1. Ranh giới 34 tỉnh/thành phố và 126 xã/phường Hà Nội
- **Tên bộ dữ liệu:** Vietnamese Provinces Database (GIS Dataset, phiên bản `v5.2.0`)
- **Link nguồn:** https://github.com/thanglequoc/vietnamese-provinces-database
- **Nguồn gốc tham chiếu:** Cổng thông tin sắp xếp đơn vị hành chính (`https://sapnhap.bando.com.vn` – Bộ Nông nghiệp và Môi trường), cập nhật địa giới hành chính 2 cấp theo QĐ 19/2025/QĐ-TTg (34 tỉnh/TP, 3.321 xã/phường/đặc khu).
- **Ngày tải:** 27/11/2026
- **Giấy phép:** MIT License
- **Các bước đã xử lý:**
  1. Gộp 34 file GeoJSON cấp tỉnh và 126 file GeoJSON xã/phường của Hà Nội (`ma_tinh = "01"`) bằng `scripts/prepare_boundaries.py`.
  2. Chuẩn hóa tên thuộc tính theo quy ước hệ thống:
     - `data/processed/provinces.geojson`: `ma_tinh` (chuỗi 2 ký tự), `ten`, `loai` (`Tỉnh` / `Thành phố`).
     - `data/processed/wards_hanoi.geojson`: `ma_xa` (chuỗi 5 ký tự), `ten`, `loai` (`Phường` / `Xã`), `ma_tinh`.
  3. Kiểm tra trên QGIS: hệ tọa độ `EPSG:4326` (WGS 84), đủ 34 tỉnh/TP (đã bao gồm quần đảo Hoàng Sa thuộc Đà Nẵng `48` và quần đảo Trường Sa thuộc Khánh Hòa `56`), đủ 126 xã/phường Hà Nội.
  4. Kiểm tra dung lượng: `provinces.geojson` đạt dưới 5 MB 
### 1.2. Dữ liệu đối chiếu ranh giới tỉnh và hải đảo
- **Tên bộ dữ liệu:** Vietnam Administrative Divisions (Post-2025) – `Provinces.geojson`
- **Link nguồn:** https://github.com/nguyenduy1133/Free-GIS-Data
- **Ngày tải:** 27/11/2026
- **Giấy phép:** Public / Ghi nhận trích dẫn tác giả (Nguyễn Duy Liêm, 2025)
- **Mục đích sử dụng:** Đối chiếu hình học 34 tỉnh/TP và kiểm tra vị trí quần đảo Hoàng Sa, Trường Sa trên QGIS.