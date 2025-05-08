# Bai Tap Lon
# Web Scraping Tin Tức Chuyên Mục "Star" – Kenh14.vn

Script Python tự động thu thập bài viết từ chuyên mục **Star** trên trang [Kenh14.vn](https://kenh14.vn/star.chn), lưu dữ liệu vào file Excel và hỗ trợ chạy tự động lúc **06:00 sáng mỗi ngày**.

## Tính năng

- Thu thập toàn bộ bài viết từ chuyên mục Star
- Lấy các thông tin:
  - Tiêu đề bài viết
  - Tóm tắt / mô tả ngắn
  - Nội dung HTML của bài viết
  - Hình ảnh đầu tiên trong bài
- Duyệt qua nhiều trang tin (có phân trang)
- Tự động lưu dữ liệu vào file Excel
- Hỗ trợ thiết lập chạy tự động vào 06:00 sáng hàng ngày

## Yêu cầu hệ thống

- Python 3.x
- Các thư viện cần thiết (cài qua `requirements.txt`):

```bash
pip install -r requirements.txt
File requirements.txt gồm:

nginx
Sao chép mã
requests
beautifulsoup4
pandas
schedule
openpyxl
Cài đặt và sử dụng
Bước 1: Clone project từ GitHub
bash
Sao chép mã
git clone https://github.com/your-username/kenh14-news-scraper.git
cd kenh14-news-scraper
Bước 2: Cài đặt thư viện
bash
Sao chép mã
pip install -r requirements.txt
Bước 3: Chạy script chính
bash
Sao chép mã
python main.py
Dữ liệu đầu ra
File Excel: kenh14_news.xlsx

Gồm các cột:

Chuyên mục	Tiêu đề	Tóm tắt	Nội dung HTML	Hình ảnh

Thiết lập chạy tự động lúc 06:00 sáng
Sử dụng thư viện schedule như sau:

python
Sao chép mã
import schedule
import time

schedule.every().day.at("06:00").do(fetch_news_data)

while True:
    schedule.run_pending()
    time.sleep(60)
Có thể chạy thủ công bằng terminal, hoặc kết hợp với cron job (trên Linux) hoặc Task Scheduler (Windows)

  Sử dụng với Visual Studio Code
Mở VS Code

Tạo file main.py

Dán toàn bộ mã Python vào file

Mở terminal (Ctrl + `), chạy lệnh:
bash
Sao chép mã
pip install -r requirements.txt
Chạy script:
bash
Sao chép mã
python main.py
