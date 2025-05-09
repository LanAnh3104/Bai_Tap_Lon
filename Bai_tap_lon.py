import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import scheduleimport requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 3. Bấm tìm kiếm(nếu trang web tin tức không có Button tìm kiếm thì có thể bỏ qua).
def click_search(driver, keyword="Giải trí"):
    try:
        search_input = driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm...']")
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.RETURN)
        print("Đã bấm nút tìm kiếm với từ khóa:", keyword)
    except Exception as e:
        print("Không tìm thấy ô tìm kiếm:", e)
        
# 1. Vào website đã chọn.
def search_data():
    print(" Bắt đầu thu thập dữ liệu...")
    data = []

# 5. Lấy tất cả dữ liệu của các trang.
    page = 1
    while True:
        print(f"\n Đang xử lý trang {page}...")
        if page == 1:
# 2. Click chọn một mục tin tức bất kì(Công nghệ, Kinh doanh, Giải trí, Sức khỏe, Thế giới, ... ). 
            url = "https://kenh14.vn/star.chn"
        else:
            url = f"https://kenh14.vn/timeline/Star/trang-{page}.chn"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Tìm tất cả các bài viết trong trang hiện tại
        articles = soup.find_all("h3", class_="knswli-title")
        if not articles:
            print(" Không tìm thấy bài viết nào nữa. Dừng lại.")
            break

# 4. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Hình ảnh, Nội dung bài viết) hiển thị ở bài viết.
        for article in articles:
            try:
                # Lấy tiêu đề và link
                title = article.text.strip()
                link = article.find("a")["href"]
                if not link.startswith("http"):
                    link = "https://kenh14.vn" + link

                print(f" Đang xử lý: {title}")
                
                # Lấy nội dung bài viết
                article_response = requests.get(link)
                article_soup = BeautifulSoup(article_response.content, "html.parser")

                # Lấy tóm tắt
                summary = article_soup.find("h2", class_="knc-sapo")
                summary = summary.text.strip() if summary else ""

                # Lấy nội dung
                content = article_soup.find("div", id="ContentDetail")
                content_html = content.decode_contents() if content else ""

                # Lấy hình ảnh
                image = content.find("img")["src"] if content and content.find("img") else ""

                # Thêm vào danh sách
                data.append(["Star", title, summary, content_html, image])
                print(f" Đã thu thập: {title}")

                time.sleep(1)

            except Exception as e:
                print(f" Lỗi: {e}")
                continue

        page += 1

# 6. Lưu dữ liệu đã lấy được vào file excel hoặc csv.
    if data:
        df = pd.DataFrame(data, columns=["Category", "Title", "Summary", "Content", "Image"])
        df.to_excel("kenh14_news.xlsx", index=False)
        print(f"\n Đã lưu {len(data)} bài viết vào 'kenh14_news.xlsx'")
    else:
        print(" Không có dữ liệu để lưu")
if __name__ == "__main__":
    search_data()
# 7. Set lịch chạy vào lúc 6h sáng hằng ngày.
def job():
    print(" Đang chạy job lúc 6h sáng...")
    search_data()

schedule.every().day.at("16:58").do(job)
print(" Đã lên lịch chạy lúc 6h sáng hàng ngày...")
while True:
    schedule.run_pending()
    time.sleep(60) 
# 8. Tạo project github chế độ public.

# 9. Viết file README.md hướng dẫn cài đặt cho project github đầy đủ rõ ràng.

# 10. Push(file code, README.md, requirements.txt) lên project và nộp link project github vào classroom.
  



# 1. Vào website đã chọn.
# 2. Click chọn một mục tin tức bất kì(Công nghệ, Kinh doanh, Giải trí, Sức khỏe, Thế giới, ... ).
# 3. Bấm tìm kiếm(nếu trang web tin tức không có Button tìm kiếm thì có thể bỏ qua).

def search_data():
    print(" Bắt đầu thu thập dữ liệu...")
    data = []

# 5. Lấy tất cả dữ liệu của các trang.
    page = 1
    while True:
        print(f"\n Đang xử lý trang {page}...")
        if page == 1:
            url = "https://kenh14.vn/star.chn"
        else:
            url = f"https://kenh14.vn/timeline/Star/trang-{page}.chn"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Tìm tất cả các bài viết trong trang hiện tại
        articles = soup.find_all("h3", class_="knswli-title")
        if not articles:
            print(" Không tìm thấy bài viết nào nữa. Dừng lại.")
            break

# 4. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Hình ảnh, Nội dung bài viết) hiển thị ở bài viết.
        for article in articles:
            try:
                # Lấy tiêu đề và link
                title = article.text.strip()
                link = article.find("a")["href"]
                if not link.startswith("http"):
                    link = "https://kenh14.vn" + link

                print(f" Đang xử lý: {title}")
                
                # Lấy nội dung bài viết
                article_response = requests.get(link)
                article_soup = BeautifulSoup(article_response.content, "html.parser")

                # Lấy tóm tắt
                summary = article_soup.find("h2", class_="knc-sapo")
                summary = summary.text.strip() if summary else ""

                # Lấy nội dung
                content = article_soup.find("div", id="ContentDetail")
                content_html = content.decode_contents() if content else ""

                # Lấy hình ảnh
                image = content.find("img")["src"] if content and content.find("img") else ""

                # Thêm vào danh sách
                data.append(["Star", title, summary, content_html, image])
                print(f" Đã thu thập: {title}")

                time.sleep(1)

            except Exception as e:
                print(f" Lỗi: {e}")
                continue

        page += 1

# 6. Lưu dữ liệu đã lấy được vào file excel hoặc csv.
    if data:
        df = pd.DataFrame(data, columns=["Category", "Title", "Summary", "Content", "Image"])
        df.to_excel("kenh14_news.xlsx", index=False)
        print(f"\n Đã lưu {len(data)} bài viết vào 'kenh14_news.xlsx'")
    else:
        print(" Không có dữ liệu để lưu")
if __name__ == "__main__":
    search_data()
# 7. Set lịch chạy vào lúc 6h sáng hằng ngày.
def job():
    print(" Đang chạy job lúc 6h sáng...")
    search_data()

schedule.every().day.at("06:00").do(job)
print(" Đã lên lịch chạy lúc 6h sáng hàng ngày...")
while True:
    schedule.run_pending()
    time.sleep(60) 
# 8. Tạo project github chế độ public.

# 9. Viết file README.md hướng dẫn cài đặt cho project github đầy đủ rõ ràng.

# 10. Push(file code, README.md, requirements.txt) lên project và nộp link project github vào classroom.
  

