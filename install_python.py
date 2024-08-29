# INSTALL PYTHON 3

#%% Kiểm tra phiên bản Python
python3 --version

#%% Gỡ cài đặt. Ví dụ phiên bản đang dùng là 3.10
sudo apt-get remove python3.10

#%% Gỡ các gói phụ thuộc
sudo apt-get autoremove

#%% Cài đặt python3
# 1. Cập nhật danh sách gói
sudo apt update

# 2. Cài đặt python3
sudo apt install python3

# 3. Cài đặt pip
sudo apt install python3-pip

# 4. Kiểm tra phiên bản pip
pip3 --version

#%% Sau khi cài đặt thì thiết lập biến môi trường và PATH
# Mở file bash.rc
nano ~/.bashrc

# Thêm vào
export PATH="/usr/bin:$PATH"

# Xác nhận thay đổi file
source ~/.bashrc