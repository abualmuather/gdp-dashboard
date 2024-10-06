import streamlit as st
import matplotlib.pyplot as plt

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

# إضافة العنوان لنوع الملعب مع لون أبيض
st.markdown('<div class="selectbox-label">اختر نوع الملعب:</div>', unsafe_allow_html=True)

# اختيار نوع الملعب باستخدام قائمة منسدلة
option = st.selectbox("", ["كرة اليد", "الكرة الطائرة", "كرة السلة", "كرة القدم"])

# حسابات الملاعب بناءً على اختيار المستخدم
if option == "كرة القدم":
    st.markdown('<div class="section-header">قياسات ملعب كرة القدم المصغر</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="color: white; font-size: 1.2em;">عرض الملعب (متر):</div>', unsafe_allow_html=True)
    football_width = st.number_input("", min_value=0.0, step=0.5)
    
    if st.button("احسب القياسات"):
        if football_width > 0:
            football_length = football_width * 2  # الطول يساوي ضعف العرض
            goal_area_depth = (5.5 / 45) * football_width  # عمق منطقة المرمى
            goal_area_width = (18.32 / 45) * football_width  # عرض منطقة المرمى
            penalty_area_depth = (16.5 / 45) * football_width  # عمق منطقة الجزاء
            penalty_area_width = (40.3 / 45) * football_width  # عرض منطقة الجزاء
            penalty_spot = (11 / 45) * football_width  # نقطة الجزاء
            center_circle = (9.15 / 45) * football_width  # دائرة المنتصف

            st.markdown('<div class="result-box">نتائج قياسات ملعب كرة القدم المصغر:</div>', unsafe_allow_html=True)
            st.write(f"**طول الملعب**: {round(football_length, 1)} متر")
            st.write(f"**عمق منطقة المرمى**: {round(goal_area_depth, 1)} متر")
            st.write(f"**عرض منطقة المرمى**: {round(goal_area_width, 1)} متر")
            st.write(f"**عمق منطقة الجزاء**: {round(penalty_area_depth, 1)} متر")
            st.write(f"**عرض منطقة الجزاء**: {round(penalty_area_width, 1)} متر")
            st.write(f"**مسافة نقطة الجزاء**: {round(penalty_spot, 1)} متر")
            st.write(f"**نصف قطر دائرة المنتصف**: {round(center_circle, 1)} متر")
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot([0, football_length], [0, 0], color="white")
            ax.plot([0, football_length], [football_width, football_width], color="white")
            ax.plot([0, 0], [0, football_width], color="white")
            ax.plot([football_length, football_length], [0, football_width], color="white")
            
            # منطقة الجزاء
            ax.plot([16.5, 16.5], [(football_width - penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")
            ax.plot([football_length - 16.5, football_length - 16.5], [(football_width - penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")
            ax.plot([16.5, football_length - 16.5], [(football_width - penalty_area_width) / 2, (football_width - penalty_area_width) / 2], color="white")
            ax.plot([16.5, football_length - 16.5], [(football_width + penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")
            
            ax.set_facecolor("#2c3e50")
            ax.set_xlim(0, football_length)
            ax.set_ylim(0, football_width)
            ax.set_aspect('equal', 'box')
            st.pyplot(fig)
        else:
            st.warning("الرجاء إدخال قيمة عرض صحيحة.")

elif option == "كرة اليد":
    st.markdown('<div class="section-header">قياسات ملعب كرة اليد المصغر</div>', unsafe_allow_html=True)
    handball_width = st.number_input("عرض الملعب (متر):", min_value=0.0, step=0.5)
    
    if st.button("احسب القياسات"):
        if handball_width > 0:
            handball_length = handball_width * 2  # الطول يساوي ضعف العرض
            goal_area_length = 6  # منطقة المرمى ثابتة
            goal_area_width = 7

            st.markdown('<div class="result-box">نتائج قياسات ملعب كرة اليد المصغر:</div>', unsafe_allow_html=True)
            st.write(f"**طول الملعب**: {round(handball_length, 1)} متر")
            st.write(f"**عمق منطقة المرمى**: {goal_area_length} متر")
            st.write(f"**عرض منطقة المرمى**: {goal_area_width} متر")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot([0, handball_length], [0, 0], color="white")
            ax.plot([0, handball_length], [handball_width, handball_width], color="white")
            ax.plot([0, 0], [0, handball_width], color="white")
            ax.plot([handball_length, handball_length], [0, handball_width], color="white")
            ax.plot([6, 6], [(handball_width - goal_area_width) / 2, (handball_width + goal_area_width) / 2], color="white")
            ax.plot([handball_length - 6, handball_length - 6], [(handball_width - goal_area_width) / 2, (handball_width + goal_area_width) / 2], color="white")
            ax.set_facecolor("#2c3e50")
            ax.set_xlim(0, handball_length)
            ax.set_ylim(0, handball_width)
            ax.set_aspect('equal', 'box')
            st.pyplot(fig)
        else:
            st.warning("الرجاء إدخال قيمة عرض صحيحة.")

elif option == "الكرة الطائرة":
    st.markdown('<div class="section-header">قياسات ملعب الكرة الطائرة المصغر</div>', unsafe_allow_html=True)
    volleyball_width = st.number_input("عرض الملعب (متر):", min_value=0.0, step=0.5)
    
    if st.button("احسب القياسات"):
        if volleyball_width > 0:
            volleyball_length = volleyball_width * 2  # الطول يساوي ضعف العرض

            st.markdown('<div class="result-box">نتائج قياسات ملعب الكرة الطائرة المصغر:</div>', unsafe_allow_html=True)
            st.write(f"**طول الملعب**: {round(volleyball_length, 1)} متر")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot([0, volleyball_length], [0, 0], color="white")
            ax.plot([0, volleyball_length], [volleyball_width, volleyball_width], color="white")
            ax.plot([0, 0], [0, volleyball_width], color="white")
            ax.plot([volleyball_length, volleyball_length], [0, volleyball_width], color="white")
            ax.plot([volleyball_length / 2, volleyball_length / 2], [0, volleyball_width], color="white")
            ax.set_facecolor("#2c3e50")
            ax.set_xlim(0, volleyball_length)
            ax.set_ylim(0, volleyball_width)
            ax.set_aspect('equal', 'box')
            st.pyplot(fig)
        else:
            st.warning("الرجاء إدخال قيمة عرض صحيحة.")

elif option == "كرة السلة":
    st.markdown('<div class="section-header">قياسات ملعب كرة السلة المصغر</div>', unsafe_allow_html=True)
    basketball_width = st.number_input("عرض الملعب (متر):", min_value=0.0, step=0.5)
    
    if st.button("احسب القياسات"):
        if basketball_width > 0:
            basketball_length = basketball_width * 2 - 2  # الطول يساوي ضعف العرض تقريباً

            st.markdown('<div class="result-box">نتائج قياسات ملعب كرة السلة المصغر:</div>', unsafe_allow_html=True)
            st.write(f"**طول الملعب**: {round(basketball_length, 1)} متر")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot([0, basketball_length], [0, 0], color="white")
            ax.plot([0, basketball_length], [basketball_width, basketball_width], color="white")
            ax.plot([0, 0], [0, basketball_width], color="white")
            ax.plot([basketball_length, basketball_length], [0, basketball_width], color="white")
            ax.plot([basketball_length / 2, basketball_length / 2], [0, basketball_width], color="white")
            center_circle = plt.Circle((basketball_length / 2, basketball_width / 2), 1.8, color="white", fill=False)
            ax.add_artist(center_circle)
            ax.set_facecolor("#2c3e50")
            ax.set_xlim(0, basketball_length)
            ax.set_ylim(0, basketball_width)
            ax.set_aspect('equal', 'box')
            st.pyplot(fig)
        else:
            st.warning("الرجاء إدخال قيمة عرض صحيحة.")

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية - محافظة مسقط
    </div>
    """, unsafe_allow_html=True)
