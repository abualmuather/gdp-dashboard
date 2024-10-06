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
        color: #d3d3d3; /* لون رمادي فاتح */
        font-size: 0.7em; /* حجم خط صغير */
        margin-bottom: 10px;
        margin-left: auto;
        margin-right: auto;
        width: 100%; /* توسيع النص ليشغل كامل العرض */
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

# إضافة العنوان لنوع الملعب مع لون أبيض
st.markdown('<div class="selectbox-label">اختر نوع الملعب:</div>', unsafe_allow_html=True)

# اختيار نوع الملعب باستخدام قائمة منسدلة
option = st.selectbox("", ["كرة اليد", "الكرة الطائرة", "كرة السلة", "كرة القدم"])

# استخدام اختيار المستخدم لعرض الملعب المناسب مع إدخال يدوي
if option == "كرة القدم":
    st.markdown('<div class="section-header">قياسات ملعب كرة القدم المصغر</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="input-label">أدخل العرض الجديد لملعب كرة القدم (بالمتر):</div>', unsafe_allow_html=True)
    football_width = st.number_input("", min_value=0.0, step=0.5)
    football_length = football_width * 2  # الطول يساوي ضعف العرض

    if football_width:
        # الحسابات باستخدام النسب على أساس العرض الرسمي 45 متر
        goal_area_depth = (5.5 / 45) * football_width  # عمق منطقة المرمى
        goal_area_width = (18.32 / 45) * football_width  # عرض منطقة المرمى
        penalty_spot = (11 / 45) * football_width  # نقطة الجزاء
        center_circle = (9.15 / 45) * football_width  # دائرة المنتصف

        st.markdown('<div class="result-box">نتائج قياسات ملعب كرة القدم المصغر:</div>', unsafe_allow_html=True)
        st.write(f"طول الملعب: {round(football_length, 1)} متر")
        st.write(f"عمق منطقة المرمى: {round(goal_area_depth, 1)} متر")
        st.write(f"عرض منطقة المرمى: {round(goal_area_width, 1)} متر")
        st.write(f"مسافة نقطة الجزاء: {round(penalty_spot, 1)} متر")
        st.write(f"نصف قطر دائرة المنتصف: {round(center_circle, 1)} متر")

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية - محافظة مسقط
    </div>
    """, unsafe_allow_html=True)
