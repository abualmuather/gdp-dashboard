import streamlit as st

# إضافة CSS لتعديل النصوص والتنسيق
st.markdown("""
    <style>
    .stApp {
        background-color: #2c3e50;
        font-family: 'Arial', sans-serif;
        color: #f5f5f5;
    }
    body {
        direction: rtl;
        text-align: right;
    }
    .title {
        text-align: center;
        background-color: #2c3e50;
        padding: 15px;
        border-radius: 10px;
        font-size: 2.2em;
        font-weight: bold;
        color: #ecf0f1;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }
    .header-text {
        text-align: right;
        color: #d3d3d3; /* لون رمادي فاتح */
        font-size: 0.7em; /* حجم خط صغير */
        margin-bottom: 10px;
        width: 100%; /* توسيع النص ليشغل كامل العرض */
        margin-right: 0; /* توسيط النص إلى اليمين */
    }
    .section-header {
        background-color: #34495e;
        padding: 10px;
        border-radius: 8px;
        font-size: 1.4em;
        font-weight: bold;
        color: #ecf0f1;
        margin-top: 20px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        font-size: 1.2em;
        color: #ecf0f1;
        margin-bottom: 15px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        color: #ecf0f1;
        font-size: 1em;
        padding: 10px;
        background-color: #2c3e50;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }
    .button {
        background-color: #2980b9;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        font-size: 1.1em;
        cursor: pointer;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #3498db;
    }
    .slider-label {
        color: #ecf0f1;
        font-size: 1.1em;
    }
    .input-label {
        color: #ffffff;
        font-size: 1.2em;
        margin-bottom: 5px;
    }
    .selectbox-label {
        color: #ffffff;
        font-size: 1.2em;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# إضافة الديباجة في أعلى الصفحة وتوسيطها إلى اليمين
st.markdown("""
    <div class="header-text">
        المديرية العامة للتربية والتعليم بمحافظة مسقط <br>
        دائرة الإشراف التربوي <br>
        قسم الإشراف الفني <br>
        الرياضة المدرسية
    </div>
    """, unsafe_allow_html=True)

# عنوان التطبيق بتصميم حديث
st.markdown('<div class="title">حاسبة قياسات الملاعب المصغرة</div>', unsafe_allow_html=True)

# إضافة العنوان لنوع الملعب مع لون أبيض
st.markdown('<div class="selectbox-label">اختر نوع الملعب:</div>', unsafe_allow_html=True)
# اختيار نوع الملعب باستخدام قائمة منسدلة
option = st.selectbox("", ["كرة اليد", "الكرة الطائرة", "كرة السلة"])

# استخدام اختيار المستخدم لعرض الملعب المناسب مع إدخال يدوي
if option == "كرة اليد":
    st.markdown('<div class="section-header">قياسات ملعب كرة اليد المصغر</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">أدخل العرض الجديد لملعب كرة اليد (بالمتر):</div>', unsafe_allow_html=True)
    handball_width = st.number_input("", min_value=0.0, step=0.5)
    handball_length = handball_width * 2  # الطول يساوي ضعف العرض

    if handball_width:
        st.markdown('<div class="result-box">نتائج قياسات ملعب كرة اليد المصغر:</div>', unsafe_allow_html=True)
        st.write(f"طول الملعب: {round(handball_length, 1)} متر")
        st.write(f"خط 9 أمتار: {round(0.45 * handball_width, 1)} متر")
        st.write(f"خط 6 أمتار: {round(0.3 * handball_width, 1)} متر")
        st.write(f"خط رمية الجزاء: {round(0.35 * handball_width, 1)} متر")
        st.write(f"منطقة التبديل: {round(0.23 * handball_width, 1)} متر")
        st.write(f"منطقة الحارس: {round(0.2 * handball_width, 1)} متر")

elif option == "الكرة الطائرة":
    st.markdown('<div class="section-header">قياسات ملعب الكرة الطائرة المصغر</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):</div>', unsafe_allow_html=True)
    volleyball_width = st.number_input("", min_value=0.0, step=0.5)
    volleyball_length = volleyball_width * 2  # الطول يساوي ضعف العرض

    if volleyball_width:
        st.markdown('<div class="result-box">نتائج قياسات ملعب الكرة الطائرة المصغر:</div>', unsafe_allow_html=True)
        front_area = 0.333333333333333 * volleyball_width
        back_area = 0.666666666666667 * volleyball_width
        substitution_area_length = 0.19 * volleyball_width

        st.write(f"طول الملعب: {round(volleyball_length, 1)} متر")
        st.write(f"مساحة المنطقة الأمامية: {round(front_area, 1)} متر")
        st.write(f"مساحة المنطقة الخلفية: {round(back_area, 1)} متر")
        st.write(f"طول امتداد خطوط منطقة تبديل اللاعبين: {round(substitution_area_length, 1)} متر")

elif option == "كرة السلة":
    st.markdown('<div class="section-header">قياسات ملعب كرة السلة المصغر</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">أدخل العرض الجديد لملعب كرة السلة (بالمتر):</div>', unsafe_allow_html=True)
    basketball_width = st.number_input("", min_value=0.0, step=0.5)
    basketball_length = basketball_width * 2 - 2  # الطول يساوي ضعف العرض

    if basketball_width:
        st.markdown('<div class="result-box">نتائج قياسات ملعب كرة السلة المصغر:</div>', unsafe_allow_html=True)
        free_throw_line = 0.386 * basketball_width
        free_throw_area_width = 0.326666666666667 * basketball_width
        three_point_line = 0.45 * basketball_width
        center_circle_diameter = 0.24 * basketball_width
        distance_to_end = 0.105 * basketball_width
        free_throw_half_circle = 0.12 * basketball_width

        st.write(f"طول الملعب: {round(basketball_length, 1)} متر")
        st.write(f"طول خط الرمية الحرة: {round(free_throw_line, 1)} متر")
        st.write(f"عرض منطقة الرمية الحرة: {round(free_throw_area_width, 1)} متر")
        st.write(f"خط الثلاث نقاط: {round(three_point_line, 1)} متر")
        st.write(f"قطر دائرة المنتصف: {round(center_circle_diameter, 1)} متر")
        st.write(f"المسافة بين السلة وخط النهاية: {round(distance_to_end, 1)} متر")
        st.write(f"نصف قطر دائرة الرمية الحرة: {round(free_throw_half_circle, 1)} متر")

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية
    </div>
    """, unsafe_allow_html=True)
