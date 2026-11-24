# Nghiệm thu MVP MarLens

Ghi commit, bộ dữ liệu/kỳ, trình duyệt, người thử và ngày thử trước mỗi lượt. Chỉ đánh dấu khi đã quan sát được kết quả. Gắn ảnh, video hoặc issue vào cột minh chứng.

| Đạt | Tiêu chí | Thao tác và kết quả mong đợi | Minh chứng / lỗi |
| --- | --- | --- | --- |
| ☐ | 1. Bản đồ và địa phương | Mở Bản đồ, chọn Hà Nội rồi chọn một xã/phường. WeMap hiển thị đúng vùng và thông tin địa phương vừa chọn. | |
| ☐ | 2. Ít nhất hai lớp hợp lệ | Lần lượt bật rồi tắt lớp ranh giới và lớp điểm bán. Đối chiếu một vùng, một điểm với bộ dữ liệu thử. Mỗi lớp xuất hiện và ẩn độc lập. | |
| ☐ | 3. Tìm theo tên và địa chỉ | Tìm “Ba Đình” và “ba dinh”, chọn đúng kết quả hành chính. Tìm thêm một địa chỉ qua WeGeocoder và kiểm tra vị trí trên bản đồ. | |
| ☐ | 4. Nguồn và kỳ số liệu | Mở popup một địa phương, ghi nguồn và kỳ của một chỉ tiêu. Đối chiếu với dòng tương ứng ở màn hình Nguồn dữ liệu. | |
| ☐ | 5. Trọng số và thứ hạng MPI | Đổi trọng số, bấm Tính. Kiểm tra tổng trọng số sau chuẩn hóa bằng 1, bảng có thứ hạng và kết quả khớp lớp màu MPI. | |
| ☐ | 6. Kịch bản shop mỹ phẩm | Chọn Hà Nội, chỉnh trọng số, chọn xã/phường hạng đầu, so sánh với hai phương án khác và xem thời gian tới bưu cục bằng WeRouting. Ghi lý do chọn điểm giao nhận. | |

Trong các ca có liên quan, thử thêm một giá trị thiếu và một số liệu mô phỏng. Giá trị thiếu hiện “Chưa có dữ liệu”, tô xám trên bản đồ và không tự nội suy. Số mô phỏng có nhãn “Mô phỏng”.

**Biên bản lượt thử:** Commit ___ · Bộ dữ liệu/kỳ ___ · Trình duyệt ___ · Người thử ___ · Ngày ___ · Số tiêu chí đạt ___/6.

Nếu gặp lỗi, ghi bước tái hiện, kết quả thực tế, ảnh và người phụ trách vào GitHub Issue. Sau khi sửa, ghi commit và kết quả thử lại.
