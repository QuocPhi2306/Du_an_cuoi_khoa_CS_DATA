import streamlit as st
import os
st.set_page_config(page_title="Bảng show dữ liệu", layout="wide")
st.title("📊Thống kê, phân tích lượt mua hàng vào Black Friday")

chart_structure = {
    "Xem thống kê": {
        "Thống kê giới tính": "./Chart/TK_gender.png",
        "Thống kê nhóm tuổi": "./Chart/TK_age.png",
        "Thống kê thành phố": "./Chart/TK_city_category.png",
        "Thống kê thời gian ở trong thành phố": "./Chart/TK_stay_in_curent_city_years.png",
        "Thống kê nghề nghiệp": "./Chart/TK_occupation.png",
        "Thống kê tình trạng hôn nhân": "./Chart/TK_marital_status.png",
        "Thống kê sản phẩm 1": "./Chart/TK_pro_1.png",
        "Thống kê sản phẩm 2": "./Chart/TK_pro_2.png",
        "Thống kê sản phẩm 3": "./Chart/TK_pro_3.png",
    },

    "Phân phối giá trị mua hàng": {
        "Base": "./Chart/PP.png",
        "Theo giới tính": "./Chart/PP_gender.png",
        "Theo nhóm tuổi": "./Chart/PP_age.png",
        "Theo thành phố": "./Chart/PP_city_category.png",
    },

    "Tương quan": {
        "Heatmap": "./Chart/Heatmap.png",
        
    },
    "Giá trị trung bình mặt hàng": {
        "Mặt hàng 1": "./Chart/AVG_1.png",
        "Mặt hàng 2": "./Chart/AVG_2.png",
        "Mặt hàng 3": "./Chart/AVG_3.png",
    }
}
chart_descriptions = {
    "Base":
    """
    Biểu đồ cho thấy:
    - Phân phối không phải dạng chuẩn (không normal).
    - Có rất nhiều đỉnh (multimodal) — không chỉ 2–3 đỉnh mà tới 8–10 đỉnh rõ rệt.
    - Trải dài từ khoảng 0 đến hơn 20,000.
    - Phần đuôi bên phải dài (right-skewed).
    - Mật độ biến động mạnh → không mượt như các phân phối đơn lẻ.
    - Có các cụm giá trị “tập trung” tại nhiều nhóm giá mua khác nhau.

    -> Đó là dấu hiệu điển hình của:
    - Nhiều loại sản phẩm khác nhau có mức giá trung bình khác nhau.
    - Nhiều phân khúc khách hàng có hành vi chi tiêu khác nhau.
    - Có thể tồn tại chính sách giá / mức giảm giá theo hạng mức cố định, tạo ra “đỉnh”
    """,
    "Theo giới tính":
    """
    - Giá trị mua hàng có xu hướng tập trung ở các khoảng cố định: Biểu đồ thể hiện sự phân bố đa đỉnh (multimodal distribution) rõ rệt, cho thấy người mua hàng (cả nam và nữ) thường thực hiện các giao dịch có giá trị tập trung tại một số khoảng nhất định (ví dụ: khoảng 5.000, 7.500, 10.000, 15.000, và 20.000), thay vì phân bố đều. Điều này có thể phản ánh giá niêm yết của các sản phẩm phổ biến hoặc các mức khuyến mãi cố định.

    - Nam giới (M) có tần suất mua hàng cao hơn Nữ giới (F) ở hầu hết các mức giá:

    - Các thanh biểu đồ màu cam (Nam/M) nhìn chung cao hơn các thanh màu xanh (Nữ/F) tại hầu hết các khoảng giá trị mua hàng, đặc biệt là ở các đỉnh phổ biến (khoảng 5.000 đến 10.000). Điều này cho thấy số lượng giao dịch (tần suất) do nam giới thực hiện nhiều hơn nữ giới.

    - Mặc dù đường cong ước tính mật độ (KDE) của nam giới (M) có vẻ cao hơn và trải rộng hơn, đường cong của nữ giới (F) cũng thể hiện các đỉnh tại các khoảng giá trị tương tự.

    - Đỉnh phân phối tập trung lớn nhất: Cả hai giới tính đều có tần suất mua hàng cao nhất tại khoảng giá trị mua hàng trong vùng 7.500. Nam giới có số lượng giao dịch tại đỉnh này lớn hơn đáng kể so với nữ giới.

    - Sự khác biệt ở phân khúc giá cao: Ở các phân khúc giá trị mua hàng lớn hơn 15.000, tần suất mua hàng của cả hai giới tính đều giảm mạnh, nhưng nam giới (M) vẫn giữ tần suất cao hơn so với nữ giới (F) ở hầu hết các điểm.
    """,
    "Theo nhóm tuổi":
    """
    1. Nhóm tuổi thống trị (26-35):
    - Tần suất mua hàng cao nhất: Nhóm tuổi 26-35 (màu xanh lá cây) thể hiện tần suất/số lượng giao dịch áp đảo so với tất cả các nhóm tuổi khác ở hầu hết mọi mức giá.

    - Các thanh biểu đồ màu xanh lá cây cao hơn đáng kể, và đường cong ước tính mật độ (KDE) của nhóm này cũng cao nhất.

    - Điều này cho thấy nhóm tuổi 26-35 là nhóm khách hàng cốt lõi và thực hiện số lượng giao dịch lớn nhất. Đây thường là nhóm đã ổn định về mặt tài chính và có nhu cầu tiêu dùng cao.
 
    - Đỉnh giao dịch: Nhóm 26-35 có đỉnh tần suất lớn nhất tập trung rõ rệt trong khoảng 7.500.

    2. Hành vi mua hàng ở các nhóm tuổi khác:
    - Nhóm tuổi 18-25 và 36-45: Đây là hai nhóm có tần suất mua hàng cao thứ hai, nhưng thấp hơn nhiều so với nhóm 26-35.

    - Nhóm 18-25 (màu cam) và 36-45 (màu hồng nhạt) có đường phân phối và các đỉnh tương tự nhau, theo sát sau nhóm 26-35.

    - Tần suất của nhóm 18-25 có xu hướng cao hơn nhóm 36-45 tại hầu hết các điểm.

    - Các nhóm tuổi còn lại (trẻ và lớn tuổi):

    - Các nhóm tuổi 0-17 (màu xanh dương nhạt), 46-50 (màu tím), 51-55 (màu nâu), và 55+ (màu hồng) đều có tần suất giao dịch rất thấp và tương đương nhau. Đường cong KDE của các nhóm này hầu như nằm sát trục hoành.

    - Điều này chỉ ra rằng các nhóm rất trẻ hoặc lớn tuổi hơn có mức độ tham gia vào việc mua sắm này thấp hơn nhiều.

    3. Phân phối và Điểm tập trung:
    - Phân phối đa đỉnh đồng nhất: Tương tự như biểu đồ theo giới tính, biểu đồ theo nhóm tuổi cũng có cấu trúc đa đỉnh rõ ràng.

    - Các điểm tập trung chính: Tất cả các nhóm tuổi đều có xu hướng tập trung các giao dịch ở cùng các khoảng giá trị cố định, chủ yếu là xung quanh: 5.000, 7.500, 10.000, 15.000, và 20.000.

    - Điều này củng cố giả định rằng các đỉnh này không phải do hành vi cá nhân mà do cấu trúc giá sản phẩm/dịch vụ hoặc các chương trình khuyến mãi/combo cụ thể.

    --> Tóm lại: Nhóm tuổi 26-35 là nhóm khách hàng quan trọng nhất về mặt số lượng giao dịch. Các chiến lược kinh doanh và tiếp thị nên tập trung mạnh vào nhóm này, đồng thời nghiên cứu lý do tại sao các giao dịch lại tập trung vào các mức giá cố định (5.000, 7.500, 10.000, etc.) để tối ưu hóa sản phẩm và khuyến mãi.
    """,
    "Theo thành phố":
    """
    1. Thành phố B có Tần suất giao dịch cao nhất:
    - Thống lĩnh thị trường: Thành phố B (màu cam) thể hiện tần suất giao dịch cao nhất ở hầu hết các mức giá trị mua hàng. Các thanh biểu đồ màu cam thường là phần cao nhất trong tổng thể, và đường cong ước tính mật độ (KDE) của thành phố B luôn nằm trên hoặc gần như nằm trên cùng so với A và C.

    - Đỉnh giao dịch: Giống như các phân tích trước, đỉnh tần suất lớn nhất của thành phố B tập trung mạnh mẽ ở khoảng 7.500.

    2. Sự khác biệt về Đỉnh giao dịch giữa các Thành phố:
    - Thành phố A (Xanh dương):

    - Thành phố A có tần suất giao dịch thấp nhất trong ba loại thành phố.

    - Đường phân phối của A có xu hướng tập trung tương đối đều hơn các thành phố khác ở các mức giá trung bình.

    - Thành phố C (Xanh lá cây):

    - Thành phố C có tần suất giao dịch ở mức trung bình (cao hơn A, thấp hơn B).

    - Điểm nổi bật: Thành phố C là nơi có tần suất giao dịch cao nhất so với A và B ở mức giá trị mua hàng lớn nhất (khoảng 20.000). Điều này cho thấy khách hàng ở Thành phố C có thể có xu hướng thực hiện các giao dịch lớn, đắt tiền hơn hoặc mua số lượng lớn hơn ở một số thời điểm.

    3. Cấu trúc Phân phối Giá trị Mua hàng:
    - Phân phối đa đỉnh đồng nhất: Cả ba loại thành phố A, B, và C đều tuân theo cấu trúc phân phối đa đỉnh tương tự nhau.

    - Các mức giá cố định: Hành vi mua sắm ở cả ba thành phố đều tập trung vào các mức giá trị mua hàng cố định: 5.000, 7.500, 10.000, 15.000, và 20.000. Điều này cho thấy chính sách giá hoặc các loại sản phẩm phổ biến là yếu tố chính định hình giá trị giao dịch, không bị ảnh hưởng nhiều bởi loại thành phố.

    - Tóm lại: Thành phố B là thị trường quan trọng nhất về mặt số lượng giao dịch. Thành phố C có hành vi mua sắm khác biệt ở phân khúc giá cao, với tần suất mua hàng ở mức 20.000 nổi bật hơn so với A và B. Thành phố A có mức độ giao dịch thấp nhất.
    """,
    "Heatmap":
    """
 
    """
}
st.sidebar.header("Chọn nhóm biểu đồ")
category = st.sidebar.selectbox(
    "Chọn loại:",
    options=list(chart_structure.keys())
)

subcharts = chart_structure[category]    
chart_name = st.sidebar.selectbox(
    "Biểu đồ:",
    options=list(subcharts.keys())
)

image_path = subcharts[chart_name]


st.subheader(f"🧷{chart_name}")

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)


    if chart_name in chart_descriptions:
        st.markdown(chart_descriptions[chart_name])

else:
    st.error(f"Không tìm thấy file ảnh: {image_path}")

