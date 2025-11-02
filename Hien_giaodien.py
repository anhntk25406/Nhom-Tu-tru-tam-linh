import sys
from PyQt6.QtWidgets import QDialog, QApplication
from thansohoc import Ui_dialog


class MainApp(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        # Kết nối nút bấm
        self.ui.pushButton.clicked.connect(self.xu_ly_giai_ma)

    def tinh_so_chu_dao(self, a, b, c):
        chuoi_so = str(a) + str(b) + str(c)
        tong = 0
        for chu in chuoi_so:
            tong = tong + int(chu)

        while tong > 9 and tong != 11 and tong != 22:
            chuoi_so_tam = str(tong)
            tong_tam_thoi = 0
            for chu in chuoi_so_tam:
                tong_tam_thoi = tong_tam_thoi + int(chu)
            tong = tong_tam_thoi

        return tong

    def giai_ma_y_nghia(self, so_chu_dao):
        giai_ma = {
            "1": "Số 1: Người Tiên Phong - đại diện cho ý chí độc lập, tinh thần tiên phong và khả năng lãnh đạo bẩm sinh, nhưng cần tiết chế xu hướng độc đoán và coi mình là trung tâm.",
            "2": "Số 2: Người Hòa Giải - có khả năng ngoại giao, thấu hiểu và kết nối người khác một cách tinh tế, nhưng dễ bị phụ thuộc cảm xúc và thiếu quyết đoán khi gặp áp lực.",
            "3": "Số 3: Người Truyền Cảm Hứng - giỏi giao tiếp, tư duy sáng tạo và lan tỏa năng lượng tích cực, tuy nhiên cần rèn luyện tính kỷ luật để hoàn thành mục tiêu thay vì bị phân tán.",
            "4": "Số 4: Người Xây Dựng - tượng trưng cho sự ổn định, kỷ luật và khả năng tổ chức công việc thực tế, nhưng nên tránh việc trở nên quá cứng nhắc, bảo thủ và tham công tiếc việc.",
            "5": "Số 5: Người Tìm Kiếm Tự Do - linh hoạt, thông minh và yêu thích tự do phiêu lưu trải nghiệm, nhưng dễ bị phân tán bởi nhiều mối quan tâm và cần học cách cam kết kiên định.",
            "6": "Số 6: Người Chăm Sóc - giàu tình yêu thương, có trách nhiệm cao với gia đình và cộng đồng, song cần cẩn thận để không hy sinh quá mức và trở nên bao đồng, thích kiểm soát.",
            "7": "Số 7: Nhà Thông Thái - có nội tâm sâu sắc, khả năng phân tích tri thức và chiêm nghiệm, nhưng có xu hướng tự cô lập bản thân, xa cách và đôi khi quá hoài nghi thực tế.",
            "8": "Số 8: Người Điều Hành - có tham vọng lớn, tư duy điều hành và khả năng quản lý tài chính vượt trội, nhưng dễ bị quyền lực và chủ nghĩa vật chất chi phối, dẫn đến sự độc đoán.",
            "9": "Số 9: Người Nhân Đạo - sống có lý tưởng nhân đạo, giàu lòng bao dung và trí tuệ sâu sắc, tuy nhiên cần cân bằng giữa việc cho đi và học cách buông bỏ quá khứ.",
            "11": "Số 11: Người Truyền Cảm Hứng Trực Giác - sở hữu trực giác cực kỳ nhạy bén và khả năng truyền cảm hứng tâm linh mạnh mẽ, nhưng dễ bị căng thẳng thần kinh và khó cân bằng với cuộc sống vật chất.",
            "22": "Số 22: Bậc Thầy Kiến Tạo - có khả năng phi thường để biến những lý tưởng lớn thành hiện thực mang tầm ảnh hưởng, nhưng phải đối mặt với áp lực tinh thần cực lớn và cần tránh lạm dụng quyền lực."
        }


        return giai_ma.get(str(so_chu_dao), 'Không có dữ liệu cho số này.')


    def xu_ly_giai_ma(self):
        try:
            # Lấy dữ liệu
            ngay_str = self.ui.comboBox.currentText()
            thang_str = self.ui.comboBox_2.currentText()
            nam_str = self.ui.lineEdit_2.text()

            # Convert
            ngay = int(ngay_str)
            thang = int(thang_str)
            nam = int(nam_str)

            if nam <= 0:
                self.ui.textEdit.setText("Lỗi: Năm sinh phải là số dương.")
                return

            # Tính toán
            so_cd = self.tinh_so_chu_dao(ngay, thang, nam)
            y_nghia = self.giai_ma_y_nghia(so_cd)

            # Xuất kết quả
            ket_qua_hien_thi = f"SỐ CHỦ ĐẠO CỦA BẠN LÀ: {so_cd}\n\nÝ NGHĨA:\n{y_nghia}"
            self.ui.textEdit.setText(ket_qua_hien_thi)

        except ValueError:
            # Bắt lỗi nếu nhập chữ vào ô "Năm"
            self.ui.textEdit.setText("Lỗi: Vui lòng nhập Năm sinh là SỐ. \nNgày/Tháng phải được chọn.")
        except Exception as e:
            self.ui.textEdit.setText(f"Đã có lỗi xảy ra: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
