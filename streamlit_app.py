import streamlit as st
import matplotlib.pyplot as plt
import time

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
        text-align: center;
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
        text-align: center;
        color: #d3d3d3; 
        font-size: 0.7em; 
        margin-bottom: 10px;
        margin-left: auto;
        margin-right: auto;
        width: 100%;
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
    .stButton button {
        background-color: #2980b9;
        color: white;
        padding: 10px 20px;
        font-size: 1.2em;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }
    .stButton button:hover {
        background-color: #3498db;
    }
    </style>
    """, unsafe_allow_html=True)

# إضافة الديباجة في أعلى الصفحة وتوسيطها في الوسط
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

# اختيار نوع الملعب باستخدام قائمة منسدلة
option = st.selectbox("اختر نوع الملعب:", ["كرة القدم", "كرة اليد", "الكرة الطائرة", "كرة السلة"])

# حسابات الملاعب بناءً على اختيار المستخدم
if option == "كرة القدم":
    st.markdown('<div class="section-header">قياسات ملعب كرة القدم المصغر</div>', unsafe_allow_html=True)
    
    # إدخال العرض الجديد
    st.markdown('<div style="color: white; font-size: 1.2em;">عرض الملعب (متر):</div>', unsafe_allow_html=True)
    football_width = st.number_input("", min_value=0.0, step=0.5)
    
    if st.button("احسب القياسات"):
        with st.spinner("جاري حساب القياسات..."):
            time.sleep(2)  # تأخير بسيط لتوضيح أن الحساب يتم
            if football_width > 0:
                football_length = football_width * 2  # الطول يساوي ضعف العرض
                goal_area_depth = (5.5 / 45) * football_width  # عمق منطقة المرمى
                goal_area_width = (18.32 / 45) * football_width  # عرض منطقة المرمى
                penalty_area_depth = (16.5 / 45) * football_width  # عمق منطقة الجزاء
                penalty_area_width = (40.3 / 45) * football_width  # عرض منطقة الجزاء
                penalty_spot = (11 / 45) * football_width  # نقطة الجزاء
                center_circle = (9.15 / 45) * football_width  # دائرة المنتصف

                st.success("تم حساب القياسات بنجاح!")

                st.markdown('<div class="result-box">نتائج قياسات ملعب كرة القدم المصغر:</div>', unsafe_allow_html=True)
                st.write(f"طول الملعب: {round(football_length, 1)} متر")
                st.write(f"عمق منطقة المرمى: {round(goal_area_depth, 1)} متر")
                st.write(f"عرض منطقة المرمى: {round(goal_area_width, 1)} متر")
                st.write(f"عمق منطقة الجزاء: {round(penalty_area_depth, 1)} متر")
                st.write(f"عرض منطقة الجزاء: {round(penalty_area_width, 1)} متر")
                st.write(f"مسافة نقطة الجزاء: {round(penalty_spot, 1)} متر")
                st.write(f"نصف قطر دائرة المنتصف: {round(center_circle, 1)} متر")

elif option == "كرة اليد":
    st.markdown('<div class="section-header">قياسات ملعب كرة اليد المصغر</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">أدخل العرض الجديد لملعب كرة اليد (بالمتر):</div>', unsafe_allow_html=True)
    handball_width = st.number_input("", min_value=0.0, step=0.5)
    handball_length = handball_width * 2  # الطول يساوي ضعف العرض

    if st.button("احسب القياسات"):
        with st.spinner("جاري حساب القياسات..."):
            time.sleep(2)
            if handball_width > 0:
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

    if st.button("احسب القياسات"):
        with st.spinner("جاري حساب القياسات..."):
            time.sleep(2)
            if volleyball_width > 0:
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

    if st.button("احسب القياسات"):
        with st.spinner("جاري حساب القياسات..."):
            time.sleep(2)
            if basketball_width > 0:
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
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية - محافظة مسقط
    </div>
    <div class="footer">
        جميع الحقوق محفوظة لدائرة الإشراف التربوي
    </div>
    """, unsafe_allow_html=True)
