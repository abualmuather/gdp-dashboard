import streamlit as st

# إضافة CSS لتعيين صورة الخلفية وتعديل الكتابة من اليمين إلى اليسار مع تصميم عصري
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://i.imgur.com/plTogEg.png'); /* استبدل بـ رابط الصورة المباشر */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Arial', sans-serif;
    }
    body {
        direction: rtl;
        text-align: right;
    }
    .title {
        text-align: center;
        background-color: rgba(0, 123, 255, 0.9); /* خلفية حديثة زرقاء */
        padding: 15px;
        border-radius: 15px;
        font-size: 2.5em;
        font-weight: bold;
        color: #fff;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .section-header {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 10px;
        border-radius: 8px;
        font-size: 1.5em;
        font-weight: bold;
        color: #f0f0f0; /* لون فاتح */
        margin-top: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 10px;
        font-size: 1.2em;
        color: #000;
        margin-bottom: 15px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        color: #f0f0f0; /* لون فاتح */
        font-size: 1em;
        padding: 10px;
        background-color: rgba(0, 123, 255, 0.9);
        border-radius: 15px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .button {
        background-color: #007BFF;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        font-size: 1.1em;
        cursor: pointer;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

# عنوان التطبيق بتصميم حديث
st.markdown('<div class="title">حاسبة قياسات الملاعب المصغرة</div>', unsafe_allow_html=True)

# إضافة زرين تفاعليين لاختيار نوع الملعب
option = st.selectbox("اختر نوع الملعب:", ["كرة اليد", "الكرة الطائرة", "كرة السلة"])

# استخدام اختيار المستخدم لعرض الملعب المناسب
if option == "كرة اليد":
    st.markdown('<div class="section-header">قياسات ملعب كرة اليد المصغر</div>', unsafe_allow_html=True)
    handball_width = st.slider("أدخل العرض الجديد لملعب كرة اليد (بالمتر):", min_value=0.0, max_value=50.0, step=0.5, key="handball_width")

    if handball_width:
        st.markdown('<div class="result-box">نتائج قياسات ملعب كرة اليد المصغر:</div>', unsafe_allow_html=True)
        st.write(f"خط 9 أمتار: {round(0.45 * handball_width, 3)} متر")
        st.write(f"خط 6 أمتار: {round(0.3 * handball_width, 3)} متر")
        st.write(f"خط رمية الجزاء: {round(0.35 * handball_width, 3)} متر")
        st.write(f"منطقة التبديل: {round(0.23 * handball_width, 3)} متر")
        st.write(f"منطقة الحارس: {round(0.2 * handball_width, 3)} متر")

elif option == "الكرة الطائرة":
    st.markdown('<div class="section-header">قياسات ملعب الكرة الطائرة المصغر</div>', unsafe_allow_html=True)
    volleyball_width = st.slider("أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):", min_value=0.0, max_value=50.0, step=0.5, key="volleyball_width")

    if volleyball_width:
        st.markdown('<div class="result-box">نتائج قياسات ملعب الكرة الطائرة المصغر:</div>', unsafe_allow_html=True)
        front_area = 0.333333333333333 * volleyball_width
        back_area = 0.666666666666667 * volleyball_width
        substitution_area_length = 0.19 * volleyball_width

        st.write(f"مساحة المنطقة الأمامية: {round(front_area, 3)} متر")
        st.write(f"مساحة المنطقة الخلفية: {round(back_area, 3)} متر")
        st.write(f"طول امتداد خطوط منطقة تبديل اللاعبين: {round(substitution_area_length, 3)} متر")

elif option == "كرة السلة":
    st.markdown('<div class="section-header">قياسات ملعب كرة السلة المصغر</div>', unsafe_allow_html=True)
    basketball_width = st.slider("أدخل العرض الجديد لملعب كرة السلة (بالمتر):", min_value=0.0, max_value=50.0, step=0.5, key="basketball_width")

    if basketball_width:
        st.markdown('<div class="result-box">نتائج قياسات ملعب كرة السلة المصغر:</div>', unsafe_allow_html=True)
        free_throw_line = 0.386 * basketball_width
        free_throw_area_width = 0.326666666666667 * basketball_width
        three_point_line = 0.45 * basketball_width
        center_circle_diameter = 0.24 * basketball_width
        distance_to_end = 0.105 * basketball_width
        free_throw_half_circle = 0.12 * basketball_width

        st.write(f"طول خط الرمية الحرة: {round(free_throw_line, 3)} متر")
        st.write(f"عرض منطقة الرمية الحرة: {round(free_throw_area_width, 3)} متر")
        st.write(f"خط الثلاث نقاط: {round(three_point_line, 3)} متر")
        st.write(f"قطر دائرة المنتصف: {round(center_circle_diameter, 3)} متر")
        st.write(f"المسافة بين السلة وخط النهاية: {round(distance_to_end, 3)} متر")
        st.write(f"نصف قطر دائرة الرمية الحرة: {round(free_throw_half_circle, 3)} متر")

# إضافة زر إعادة تعيين
if st.button('إعادة تعيين'):
    st.experimental_rerun()

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية
    </div>
    """, unsafe_allow_html=True)
