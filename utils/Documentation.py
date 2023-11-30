import streamlit as st
from modules import *
from pathlib import Path


def sidebarConfig(sidebar):
    with sidebar:
        pass


def customsGroup(current_dir):
    css__custom = f'{current_dir}/assets/styles/custom.css'
    Custom_CSS(st, css__custom)
    Custom_Code(st, """
            <div class="main__title"> 
                <h3> Documentation <h3>
            <div/>        
        """)


def main(sidebar):
    # DataReview().view(DataReview.Model(), sidebar)
    st.markdown(
"""
    # **<h1 style="text-align: center;">ỨNG DỤNG THUẬT TOÁN KHỬ NHIỄU ẢNH MRI DỰA TRÊN LÝ THUYẾT MAXIMUM A POSTERIORI VÀ MARKOV RANDOM FIELD</h1>**
## **1. MRI**
### **1.1. Tổng quan**
<div style="display: flex; gap: 2rem; ">
    <div>
        <p style="text-align: justify;">
        MRI là viết tắt của Magnetic Resonance Imaging, hay "Chụp ảnh cộng hưởng từ". Đây là một phương pháp hình ảnh y tế mà không sử dụng tia X hoặc tia gamma, mà thay vào đó sử dụng từ trường từ và sóng radiofrequent để tạo ra hình ảnh của cơ thể bên trong.
        </p>
        <p style="text-align: justify;">
        Công nghệ MRI lần đầu tiên được phát minh bởi Paul C. Lauterbur dựa trên các kết quả nghiên cứu về hiện tượng từ hạt nhân (Nuclear Magnetic Resonance - NMR). Vào đầu những năm 1980 chiếc máy MRI lâm sàng đầu tiên đã được lắp đặt và công nghệ ấy đã được liên tục phát triển sau đó, dẫn đến việc sử dụng rộng rãi trong y học ngày nay.
        </p>
    </div>
<img src="https://www.nobelprize.org/images/lauterbur-13686-portrait-medium.jpg" width="520" height="250">
</div>

### **1.2. Công nghệ**
<p style="text-align: justify">
Như ai cũng biết, cơ thể chúng ta được cấu thành từ các hợp chất hữu cơ và nước vì vậy cơ thể chúng ta được cấu thành từ các nguyên tử Hidrogen là nhiều. Các nhà khoa học đã tận dụng một tính chất lượng tử của nguyên tử Hidrogen để tạo ra hình ảnh MRI
</p>
<p style="text-align: justify">
    Bên trong hạt nhân của các nguyên tử, vật lý lượng tử nói rằng các proton không đứng yên mà xoay quanh trục của chính nó, điều này tạo nên một từ trường nhỏ dọc theo trục <text style="color: red; font-weight: bold">bắc</text> - <text style="color: blue; font-weight: bold">nam</text>. Các vector từ trường tuân theo một phân phối xác suất và ở điều kiện thường sẽ triệt tiêu lẫn nhau.

![Screenshot 2023-11-22 192025](https://hackmd.io/_uploads/HyiVfdoNT.png)

<p style="text-align: justify">
Máy MRI hoạt động bằng cách cho một từ trường cực mạnh đi qua các nguyên tử ấy và sau đó các vector từ trưởng ở bản thân mỗi nguyên tử sẽ được điều chỉnh theo từ trường của chiếc máy.
</p>

    
![Screenshot 2023-11-22 193928](https://hackmd.io/_uploads/By48tdi4T.png)

<p style="text-align: justify">
Sau đó chiếc máy sẽ có bộ phận tạo các xung RF (Radiofrequency), khiến vector của các proton bị lệch 90° so với từ trường của máy.
</p>

![Screenshot 2023-11-22 215732](https://hackmd.io/_uploads/S1ffw9iNT.png)

<div style="display: flex; gap: 2rem; ">

<p style="text-align: justify; width: 300rem">
Và theo lẽ tự nhiên, các proton ấy sẽ muốn quay vector từ trường của bản thân về lại cùng hướng với vector từ trường của máy. Tuy nhiên chúng không quay trở về hướng cũ liền tức khắc mà sẽ theo một chuyển động quay với một khoảng trễ nhất định, đồng thời sự biến thiên từ trường ấy có thể được đo lường, sử dụng biến đổi Fourier (Fourier Transform) để tạo nên tấm ảnh MRI của các mô và tế bào.
</p>

![Screenshot 2023-11-22 220900](https://hackmd.io/_uploads/SyKhtcsVp.png)
    
</div>

### **1.3. Tầm quan trọng của khử nhiễu**

Trên thực tế, để cho ra được các tấm ảnh MRI tốt nhất đòi hỏi thỏa mãn một số điều kiện nhất định. Độ nhiễu của các tấm ảnh thường bị gây ra bởi các nguyên nhân sau:

* Do lõi dây siêu dẫn bên trong máy (Superconductive Coil)
* Do các mạch tiền khuếch đại (Preamplifier)
* Do cường độ của trường điện từ
* Do bản thân bệnh nhân (sinh học trong cơ thể / có cấy ghép kim loại)
* Một số yếu tố bên ngoài ngẫu nhiên không điều khiển được

<p style="text-align: justify">
Vì thế để giảm thiểu chi phí, giảm thời gian quét MRI của bệnh nhân, việc khử nhiễu tốt đối với các tấm ảnh MRI là điều cần thiết để các bác sĩ có thể đưa ra các chuẩn đoán chính xác nhất và đưa ra các phương pháp điều trị hợp lý.
</p>

## **2. SẢN PHẨM**
### **2.1. Giao diện**
### **2.2. Quy trình hoạt động**

### **2.3. Quá trình phát triển**
1. Quá trình phát triển của dự án bao gồm các bước sau:
1. Tìm hiểu về thuật toán và các kiến thức cần thiết.
1. Xây dựng phần xử lý ảnh nhiễu và phần giao diện.
1. Chỉnh sửa và công bố cho mọi người cùng xài.

## **3. Kết luận**

""", unsafe_allow_html=True
    )
    pass


def Documentation(sidebar):
    current_dir = Path(".")
    sidebarConfig(sidebar)
    customsGroup(current_dir)
    main(sidebar)
