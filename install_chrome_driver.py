# INSTALL PYTHON GOOGLE CHROME - CHROME DRIVER - SELENIUM

# Cài đặt Google Chrome
sudo apt-get update

# Cài đặt một số gói phần mềm
sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4

# Tải xuống Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Cài đặt Google Chrome
sudo apt install ./google-chrome-stable_current_amd64.deb

# Kiểm tra phiên bản Google Chrome
google-chrome --version



# Tải xuống Chrome Driver - phiên bản 127
wget https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.119/linux64/chromedriver-linux64.zip

# Giải nén file tải xuống
unzip chromedriver_linux64.zip

# Di chuyển ChromeDriver vào thư mục 
/usr/bin 
# để có thể truy cập từ bất kỳ đâu trong hệ thống
# Phân quyền cho ChromeDriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

# Kiểm tra phiên bản ChromeDriver
chromedriver --version

# GỠ CÀI ĐẶT
# Gỡ cài đặt Google Chrome
sudo apt-get purge google-chrome-stable

# Xóa file cấu hình cá nhân
rm -rf ~/.config/google-chrome
rm -rf ~/.cache/google-chrome

# Gỡ cài đặt Chrome Driver
sudo apt-get purge chromium-chromedriver
# hoặc
sudo apt-get remove chromium-chromedriver
sudo apt-get remove --auto-remove chromium-chromedriver