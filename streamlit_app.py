import streamlit as st

# إضافة CSS لتعيين صورة الخلفية، تقليل الشفافية، تحويل الكتابة من اليمين إلى اليسار، وجعل النصوص باللون الأسود
page_bg_img = '''
<style>
.stApp {
    background: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), url("https://i.imgur.com/imImwx1.jpeg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    direction: rtl; /* تحويل الكتابة من اليمين إلى اليسار */
    text-align: right;
    color: black; /* تغيير لون النصوص إلى الأسود */
}
h1, h2, h3, h4, h5, h6 {
    color: black; /* تغيير لون العناوين إلى الأسود */
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# عنوان التطبيق
st.title("حاسبة قياسات الملاعب المصغرة")

# --- قياسات ملعب كرة اليد ---
st.header("قياسات ملعب كرة اليد المصغر")
handball_width = st.number_input("أدخل العرض الجديد لملعب كرة اليد (بالمتر):", min_value=0.0, step=1.0, key="handball_width")

if handball_width:
    st.subheader("نتائج قياسات ملعب كرة اليد المصغر:")
    st.write(f"خط 9 أمتار: {round(0.45 * handball_width, 3)} متر")
    st.write(f"خط 6 أمتار: {round(0.3 * handball_width, 3)} متر")
    st.write(f"خط رمية الجزاء: {round(0.35 * handball_width, 3)} متر")
    st.write(f"منطقة التبديل: {round(0.23 * handball_width, 3)} متر")
    st.write(f"منطقة الحارس: {round(0.2 * handball_width, 3)} متر")

# --- قياسات ملعب الكرة الطائرة ---
st.header("قياسات ملعب الكرة الطائرة")
volleyball_width = st.number_input("أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):", min_value=0.0, step=1.0, key="volleyball_width")

if volleyball_width:
    st.subheader("نتائج قياسات ملعب الكرة الطائرة المصغر:")
    
    # المعادلات الجديدة بناءً على البيانات المقدمة
    front_area = 0.333333333333333 * volleyball_width
    back_area = 0.666666666666667 * volleyball_width
    substitution_area_length = 0.19 * volleyball_width

    # عرض النتائج
    st.write(f"مساحة المنطقة الأمامية: {round(front_area, 3)} متر")
    st.write(f"مساحة المنطقة الخلفية: {round(back_area, 3)} متر")
    st.write(f"طول امتداد خطوط منطقة تبديل اللاعبين: {round(substitution_area_length, 3)} متر")

# --- قياسات ملعب كرة السلة ---
st.header("قياسات ملعب كرة السلة")
basketball_width = st.number_input("أدخل العرض الجديد لملعب كرة السلة (بالمتر):", min_value=0.0, step=1.0, key="basketball_width")

if basketball_width:
    st.subheader("نتائج قياسات ملعب كرة السلة المصغر:")
    
    # المعادلات الجديدة بناءً على البيانات المقدمة
    free_throw_line = 0.386 * basketball_width
    free_throw_area_width = 0.276 * basketball_width
    three_point_line = 0.45 * basketball_width
    center_circle_diameter = 0.24 * basketball_width
    distance_to_end = 0.105 * basketball_width
    free_throw_half_circle = 0.12 * basketball_width

    # عرض النتائج
    st.write(f"طول خط الرمية الحرة: {round(free_throw_line, 3)} متر")
    st.write(f"عرض منطقة الرمية الحرة: {round(free_throw_area_width, 3)} متر")
    st.write(f"خط الثلاث نقاط: {round(three_point_line, 3)} متر")
    st.write(f"قطر دائرة المنتصف: {round(center_circle_diameter, 3)} متر")
    st.write(f"المسافة بين السلة وخط النهاية: {round(distance_to_end, 3)} متر")
    st.write(f"نصف قطر دائرة الرمية الحرة: {round(free_throw_half_circle, 3)} متر")

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <hr>
    <p style="text-align: center; color: black;">إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية</p>
    """, unsafe_allow_html=True)