import streamlit as st

# إضافة CSS لتعيين صورة الخلفية وتعديل الكتابة من اليمين إلى اليسار باستثناء العنوان الرئيسي
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://i.imgur.com/imImwx1.jpeg'); /* استبدل بـ رابط الصورة المباشر */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    body {
        direction: rtl; /* تحويل الكتابة من اليمين إلى اليسار */
        text-align: right; /* محاذاة النصوص إلى اليمين */
    }
    .title {
        direction: ltr; /* عدم تحويل عنوان التطبيق */
        text-align: center; /* محاذاة العنوان في المنتصف */
        background-color: rgba(255, 255, 255, 0.8); /* خلفية شفافة للنص */
        padding: 10px;
        border-radius: 10px;
        font-size: 2em;
        font-weight: bold;
        color: #000;
    }
    .section-header {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 5px;
        border-radius: 5px;
        font-size: 1.5em;
        font-weight: bold;
        color: #000;
        margin-top: 20px;
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 5px;
        font-size: 1.2em;
        color: #000;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        color: #000;
        font-size: 1em;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# عنوان التطبيق (يظل من اليسار إلى اليمين وفي الوسط)
st.markdown('<div class="title">حاسبة قياسات الملاعب المصغرة</div>', unsafe_allow_html=True)

# --- قياسات ملعب كرة اليد ---
st.markdown('<div class="section-header">قياسات ملعب كرة اليد المصغر</div>', unsafe_allow_html=True)
handball_width = st.number_input("أدخل العرض الجديد لملعب كرة اليد (بالمتر):", min_value=0.0, step=1.0, key="handball_width")

if handball_width:
    st.markdown('<div class="result-box">نتائج قياسات ملعب كرة اليد المصغر:</div>', unsafe_allow_html=True)
    st.write(f"خط 9 أمتار: {round(0.45 * handball_width, 3)} متر")
    st.write(f"خط 6 أمتار: {round(0.3 * handball_width, 3)} متر")
    st.write(f"خط رمية الجزاء: {round(0.35 * handball_width, 3)} متر")
    st.write(f"منطقة التبديل: {round(0.23 * handball_width, 3)} متر")
    st.write(f"منطقة الحارس: {round(0.2 * handball_width, 3)} متر")

# --- قياسات ملعب الكرة الطائرة ---
st.markdown('<div class="section-header">قياسات ملعب الكرة الطائرة</div>', unsafe_allow_html=True)
volleyball_width = st.number_input("أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):", min_value=0.0, step=1.0, key="volleyball_width")

if volleyball_width:
    st.markdown('<div class="result-box">نتائج قياسات ملعب الكرة الطائرة المصغر:</div>', unsafe_allow_html=True)
    front_area = 0.333333333333333 * volleyball_width
    back_area = 0.666666666666667 * volleyball_width
    substitution_area_length = 0.19 * volleyball_width

    st.write(f"مساحة المنطقة الأمامية: {round(front_area, 3)} متر")
    st.write(f"مساحة المنطقة الخلفية: {round(back_area, 3)} متر")
    st.write(f"طول امتداد خطوط منطقة تبديل اللاعبين: {round(substitution_area_length, 3)} متر")

# --- قياسات ملعب كرة السلة ---
st.markdown('<div class="section-header">قياسات ملعب كرة السلة</div>', unsafe_allow_html=True)
basketball_width = st.number_input("أدخل العرض الجديد لملعب كرة السلة (بالمتر):", min_value=0.0, step=1.0, key="basketball_width")

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

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية
    </div>
    """, unsafe_allow_html=True)