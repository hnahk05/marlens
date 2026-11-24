# MarLens

MarLens là ứng dụng bản đồ hỗ trợ shop mỹ phẩm online chọn xã/phường ở Hà Nội để mở điểm giao nhận. Nhóm dùng WeMap để hiển thị 34 tỉnh và thí điểm phân tích 126 xã/phường Hà Nội. Người dùng có thể đối chiếu nguồn số liệu và điều chỉnh trọng số của chỉ số MPI để so sánh các khu vực. Đây là phạm vi dự kiến của sản phẩm.

## Chạy lần đầu

Cài Git, Node.js 22 LTS, Python 3.12 và Docker Desktop. Các lệnh dưới đây dùng PowerShell. Chạy sau khi nhánh `develop` có Docker Compose, backend và frontend do TV2 và TV3 bàn giao. Repo khởi tạo mới chỉ có cấu trúc thư mục.

```powershell
git clone https://github.com/hnahk05/marlens.git
cd marlens
git checkout develop
docker compose up -d
```

Trong terminal thứ nhất, từ thư mục gốc của repo, khởi động backend.

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload --port 8000 --env-file .env
```

Trong terminal thứ hai, cũng từ thư mục gốc, chuẩn bị frontend.

```powershell
cd frontend
npm install
Copy-Item .env.example .env
```

Điền token WeMap của nhóm vào `VITE_WEMAP_TOKEN` trong `frontend/.env`. Đặt `VITE_API_URL=http://localhost:8000/api`, rồi chạy `npm run dev`. Mở [MarLens](http://localhost:5173) và [tài liệu API](http://localhost:8000/docs). Sau khi sửa biến môi trường của Vite, khởi động lại frontend.

Trên macOS/Linux, kích hoạt môi trường bằng `source .venv/bin/activate` và dùng `cp .env.example .env` trong từng thư mục. Nếu dùng PostGIS chung, bỏ qua bước Docker và điền `DATABASE_URL` do TV2 cung cấp vào `backend/.env`. Khi chạy cục bộ, PostGIS dùng cổng 5432 và `CORS_ORIGINS` của backend là `http://localhost:5173`.

## Làm việc cùng nhóm

| Phần việc | Thành viên | Vị trí chính |
| --- | --- | --- |
| Dữ liệu và GIS | Huệ · TV1 | `data/`, `scripts/` |
| Backend và PostGIS | Linh · TV2 | `backend/`, Docker Compose |
| Giao diện và bản đồ | Thư · TV3 | `frontend/` |
| Chỉ số MPI | Mai · TV4 | `analysis/`, `backend/app/mpi/`, trang Phân tích |
| Tích hợp và kiểm thử | Khánh · TV5 | `docs/`, cấu hình repo, trang Nguồn dữ liệu |

Để thử quyền Write, mỗi thành viên clone repo bằng tài khoản của mình, chuyển sang `develop`, chạy `git pull`, rồi tạo nhánh riêng (ví dụ `docs/thu-pr-tv1`). Thêm một dòng xác nhận tạm trong thư mục mình phụ trách, commit, đẩy nhánh và mở **draft PR vào develop**. Gửi link cho TV5 xác nhận và đóng PR thử.

Với công việc thật, mở PR vào `develop`, ghi cách thử và chọn một người duyệt. TV5 đưa `develop` vào `main` cuối giai đoạn. Cả nhóm dùng PR kể cả khi GitHub chưa bật bảo vệ nhánh. Xem [checklist nghiệm thu](docs/checklist.md).
