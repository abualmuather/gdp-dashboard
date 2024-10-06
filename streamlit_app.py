import streamlit as st
import matplotlib.pyplot as plt

# إعداد الرسومات للملاعب (بدون تعديل)
def draw_football_field(football_length, football_width, goal_area_depth, goal_area_width, penalty_area_depth, penalty_area_width, center_circle_radius):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([0, football_length], [0, 0], color="white")
    ax.plot([0, football_length], [football_width, football_width], color="white")
    ax.plot([0, 0], [0, football_width], color="white")
    ax.plot([football_length, football_length], [0, football_width], color="white")

    # منطقة الجزاء
    ax.plot([penalty_area_depth, penalty_area_depth], [(football_width - penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")
    ax.plot([football_length - penalty_area_depth, football_length - penalty_area_depth], [(football_width - penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")

    # منطقة المرمى
    ax.plot([goal_area_depth, goal_area_depth], [(football_width - goal_area_width) / 2, (football_width + goal_area_width) / 2], color="white")
    ax.plot([football_length - goal_area_depth, football_length - goal_area_depth], [(football_width - goal_area_width) / 2, (football_width + goal_area_width) / 2], color="white")

    # دائرة المنتصف
    center_circle = plt.Circle((football_length / 2, football_width / 2), center_circle_radius, color="white", fill=False)
    ax.add_artist(center_circle)

    # إعداد الرسم
    ax.set_facecolor("#2c3e50")
    ax.set_xlim(0, football_length)
    ax.set_ylim(0, football_width)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig

# واجهة Streamlit
st.markdown('<div class="title">حاسبة قياسات الملاعب المصغرة</div>', unsafe_allow_html=True)
option = st.selectbox("اختر نوع الملعب:", ["كرة القدم", "كرة اليد", "الكرة الطائرة", "كرة السلة"])

# إضافة النص باللون الأبيض
st.markdown('<p style="color:white;">عرض الملعب (متر):</p>', unsafe_allow_html=True)

if option == "كرة القدم":
    football_width = st.number_input("", min_value=0.0, step=0.5)
    if football_width > 0:
        football_length = football_width * 2
        goal_area_depth = (5.5 / 45) * football_width
        goal_area_width = (18.32 / 45) * football_width
        penalty_area_depth = (16.5 / 45) * football_width
        penalty_area_width = (40.3 / 45) * football_width
        center_circle_radius = (9.15 / 45) * football_width

        st.pyplot(draw_football_field(football_length, football_width, goal_area_depth, goal_area_width, penalty_area_depth, penalty_area_width, center_circle_radius))

elif option == "كرة اليد":
    handball_width = st.number_input("", min_value=0.0, step=0.5)
    if handball_width > 0:
        handball_length = handball_width * 2
        st.pyplot(draw_handball_field(handball_length, handball_width))

elif option == "الكرة الطائرة":
    volleyball_width = st.number_input("", min_value=0.0, step=0.5)
    if volleyball_width > 0:
        volleyball_length = volleyball_width * 2
        st.pyplot(draw_volleyball_field(volleyball_length, volleyball_width))

elif option == "كرة السلة":
    basketball_width = st.number_input("", min_value=0.0, step=0.5)
    if basketball_width > 0:
        basketball_length = basketball_width * 2 - 2
        st.pyplot(draw_basketball_field(basketball_length, basketball_width))

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية - محافظة مسقط
    </div>
    """, unsafe_allow_html=True)
