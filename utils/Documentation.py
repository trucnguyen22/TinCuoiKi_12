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
r'''
# **<p style="text-align: center;">ỨNG DỤNG THUẬT TOÁN KHỬ NHIỄU ẢNH MRI DỰA TRÊN LÝ THUYẾT MAXIMUM A POSTERIORI VÀ MARKOV RANDOM FIELD</p>**
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

<img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/398317719_670690535190359_7161720157303394196_n.png?stp=dst-png_p403x403&_nc_cat=101&ccb=1-7&_nc_sid=510075&_nc_ohc=CkEnEFgBTwUAX9e2q9U&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdSCF0PCTkZ1nZojhIPm5rrp_cHKPy6p3hpGVQQIIi_e1Q&oe=658CDC07"/>

<p style="text-align: justify">
Máy MRI hoạt động bằng cách cho một từ trường cực mạnh đi qua các nguyên tử ấy và sau đó các vector từ trưởng ở bản thân mỗi nguyên tử sẽ được điều chỉnh theo từ trường của chiếc máy.
</p>

<img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/405311326_2348188465382282_9059383806414829632_n.png?stp=dst-png_p403x403&_nc_cat=104&ccb=1-7&_nc_sid=510075&_nc_ohc=vo94UHF970kAX9pRzeR&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdS1WWqfpL8Dligbh0PVa-7vHKchVySeSg8yrZfwGMZ8kg&oe=658CD1EA"/>

<p style="text-align: justify">
Sau đó chiếc máy sẽ có bộ phận tạo các xung RF (Radiofrequency), khiến vector của các proton bị lệch 90° so với từ trường của máy.
</p>

<img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/376575250_286358727169965_1391136998545280464_n.png?stp=dst-png_p403x403&_nc_cat=105&ccb=1-7&_nc_sid=510075&_nc_ohc=eDbHiCr7NIsAX9G38Im&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdT7497Rzhyd9PNB_IjOXGBSaFHQJ6hMD-4Ky_Wp0EX58Q&oe=658CE8A9"/>

<div style="display: flex; gap: 2rem; margin-top: 2rem">

<p style="text-align: justify; width: 300rem">
Và theo lẽ tự nhiên, các proton ấy sẽ muốn quay vector từ trường của bản thân về lại cùng hướng với vector từ trường của máy. Tuy nhiên chúng không quay trở về hướng cũ liền tức khắc mà sẽ theo một chuyển động quay với một khoảng trễ nhất định, đồng thời sự biến thiên từ trường ấy có thể được đo lường, sử dụng biến đổi Fourier (Fourier Transform) để tạo nên tấm ảnh MRI của các mô và tế bào.
</p>

<img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/405191151_327385960002866_1767613841322721919_n.png?stp=dst-png_s403x403&_nc_cat=111&ccb=1-7&_nc_sid=510075&_nc_ohc=R7pmlStWXs0AX8rcRI1&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdSLCbosrHZWNd1RdWiB9wn2S38BMljVJw0FKuzE2OUd1w&oe=658CCCF7" width="180">
    
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
<p style = "text-align: justify">
Để dự án có thể tiếp cận được người dùng một cách dễ dàng nhất, sản phẩm của chúng tôi không yêu cầu bất cứ sự đăng nhập nào, thay vào đó chỉ bao gồm hai trang chính là "Documentation" và "Dashboard":
</p>

<img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/403411749_1523605221805726_6593852555101871095_n.png?_nc_cat=106&ccb=1-7&_nc_sid=510075&_nc_ohc=HNcVUJeS_-AAX-1kxjD&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdR1asMgeITTNP7r5QFhAGS7hgJkMl9jrW_1IeIq-FxN9w&oe=65928B2C"/>

Trang "Documentation" có nhiệm vụ cung cấp cho người dùng những thông tin tổng quan về MRI và hướng dẫn sử dụng sản phẩm.

<img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/393937828_902614950803697_1576128706601258572_n.png?_nc_cat=102&ccb=1-7&_nc_sid=510075&_nc_ohc=NJfFIGUblywAX9Cy1Lf&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQSHljhOLmkK502S18Ts1M28Ur06_0k3GxMYcKF9QW7qA&oe=65959B6E" />

Trang "Dashboard" là nơi thao tác chính của người dùng, người dùng chỉ cần tải ảnh lên, hệ thống sẽ xử lý và trả ra kết quả là ảnh MRI đã qua khử nhiễu. Ngoài ra, sản phầm còn cung cấp cho người dùng tính năng so sánh ảnh MRI trước và sau khi khử nhiễu, nó sẽ giúp ích cho các bác sĩ trong công tác chuẩn đoán bệnh.

### **2.2. Tổng quan về thuật toán**
<p style="text-align: justify">
Đối với dự án này, do đặc thù của cơ sở toán học được sử dụng nên căn bản thuật toán không thuộc về phạm trù của Machine Learning mà chỉ đơn thuần dựa vào lí thuyết phân phối xác suất.
</p>

Source code thuật toán được chúng tôi dùng:
https://github.com/kaido975/Image-Denoising

<p style="text-align: justify">
Nền móng chính cho thuật toán của dự án chính là Maximum A Posteriori (MAP) - phương pháp tìm tham số của hàm mật độ xác suất sao cho khớp với bộ dữ liệu nhiều nhất có thể. Công thức của MAP được biểu diễn như sau:
</p>
<div style="display: flex;">
$$\hat{\theta}=\underset{\theta}{\mathrm{argmax}} \: \underbrace{p(\theta|x_1,...,x_n)}_{posterior}$$
</div>

Sử dụng quy tắc Bayes, chúng ta có thể phân tách được tiếp như sau:

$$\hat{\theta} = \underset{\theta}{\mathrm{argmax}} \: \left[ \frac{\overbrace{p(x_1,...x_n|\theta)}^{likelihood} \overbrace{p(\theta)}^{prior}}{p(x_1,...x_n)}\right]
$$

Do kết quả $\hat{\theta}$ không phụ thuộc vào $p(x_1,...x_n)$ nên chúng ta có thể lược bỏ mẫu số:

$$\hat{\theta} = \underset{\theta}{\mathrm{argmax}} \: p(x_1,..,x_n|\theta)p(\theta)$$

<p style="text-align: justify">
Đến đây, nghiệm của bài toán chỉ bao gồm tính toán likelihood và prior. Tuy nhiên ta không thể tìm trực tiếp một cách chính xác mà phải sử dụng phương pháp Gradient Descend.
</p>

<img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/385434782_1530375964387128_5026900675094713718_n.png?stp=dst-png_p403x403&_nc_cat=107&ccb=1-7&_nc_sid=510075&_nc_ohc=Zsb4QlPPQTgAX_e-2OQ&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdQmR0LVOnrq4MCHuGRKJqIrOJUAy8J2myIwHheGP3A3GA&oe=6596C8E1"/>

<p style="text-align: justify">
Ở mỗi epoch, ta tính likelihood theo xác suất có điều kiện của bức ảnh hiện tại theo bức ảnh của epoch trước. Còn đối với prior của từng pixel trên bức ảnh thì sẽ được tính dựa trên 4 pixel xung quanh (trái, phải, trên, dưới). Và posterior sau đó sẽ được tính dựa trên likelihood, prior và các hyperparameter.
</p>

<p style="text-aligh: justify">
Sau khi tính xong, chương trình sẽ tìm gradient của posterior và cập nhật lại posterior cũng như bức ảnh được khử nhiễu mới.
</p>

### **2.3. Quá trình phát triển**
<p style="text-align: justify">
Trong khoảng thời gian từ ngày 14/11 đến ngày 21/11, chúng tôi tìm hiểu sâu hơn về thuật toán và khảo sát nhiều trang mang để nghiên cứu và chọn ra các ứng dụng của Maximum A Posteriori. Chúng tôi đã tìm được nhiều ứng dụng như là khử nhiễu âm thanh, khử nhiễu hình ảnh,... và chúng tôi đã chọn khử nhiễu hình ảnh MRI bởi vì tính thiết thực của nó.

Sau đó, chúng tôi tiếp túc quá trình tìm kiếm và hoàn thiện thuật toán khử nhiễu hình ảnh MRI. Và trong khoảng thời gian cuối tháng 11 và đầu tháng 12, chúng tôi bắt đầu thiết kế trang web, hoàn thiện sản phẩm và triển khai nó đến với mọi người.
</p>

## **3. Tổng kết**
<p style="text-align: justify">
Maximum A Posteriori là một công cụ rất tốt, có thể được sử dụng cho các mô hình xác suất. Tuy nhiên , đối với các mô hình thông thường thì MAP lại cho hiệu quả kém hơn so với các thuật toán và phương pháp khác (chẳng hạn như Neural Network).
Ngoài ra MAP đa số được sử dụng để nâng cấp, tối ưu hóa các thuật toán Machine Learning có sẵn
</p>

<p style="text-align: justify">
Ngoài ra MAP đa số được sử dụng để nâng cấp, tối ưu hóa các thuật toán Machine Learning có sẵn và các lý thuyết, cơ sở toán học cần để thực hiện điều đó là vô cùng phức tạp mà dự án của chúng tôi không thể thể hiện hết toàn bộ. Chúng tôi mong rằng dự án này sẽ cho mọi người có cái nhìn tổng quan về ứng dụng và cách MAP hoạt động dưới một vấn đề Machine Learning.
</p>
''', unsafe_allow_html=True
    )
    pass


def Documentation(sidebar):
    current_dir = Path(".")
    sidebarConfig(sidebar)
    customsGroup(current_dir)
    main(sidebar)
