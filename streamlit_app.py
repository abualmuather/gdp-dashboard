import streamlit as st
import matplotlib.pyplot as plt

# إعداد الرسومات للملاعب
def draw_football_field(football_length, football_width, goal_area_depth, goal_area_width, penalty_area_depth, penalty_area_width, center_circle_radius):
    fig, ax = plt.subplots(figsize=(10, 6))

    # رسم الحدود الخارجية للملعب
    ax.plot([0, football_length], [0, 0], color="white")
    ax.plot([0, football_length], [football_width, football_width], color="white")
    ax.plot([0, 0], [0, football_width], color="white")
    ax.plot([football_length, football_length], [0, football_width], color="white")

    # منطقة الجزاء
    ax.plot([penalty_area_depth, penalty_area_depth], [(football_width - penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")
    ax.plot([football_length - penalty_area_depth, football_length - penalty_area_depth], [(football_width - penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")
    ax.plot([penalty_area_depth, football_length - penalty_area_depth], [(football_width - penalty_area_width) / 2, (football_width - penalty_area_width) / 2], color="white")
    ax.plot([penalty_area_depth, football_length - penalty_area_depth], [(football_width + penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")

    # منطقة المرمى
    ax.plot([goal_area_depth, goal_area_depth], [(football_width - goal_area_width) / 2, (football_width + goal_area_width) / 2], color="white")
    ax.plot([football_length - goal_area_depth, football_length - goal_area_depth], [(football_width - goal_area_width) / 2, (football_width + goal_area_width) / 2], color="white")
    ax.plot([goal_area_depth, football_length - goal_area_depth], [(football_width - goal_area_width) / 2, (football_width - goal_area_width) / 2], color="white")
    ax.plot([goal_area_depth, football_length - goal_area_depth], [(football_width + goal_area_width) / 2, (football_width + goal_area_width) / 2], color="white")

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

def draw_handball_field(handball_length, handball_width):
    fig, ax = plt.subplots(figsize=(8, 5))

    # رسم الحدود الخارجية
    ax.plot([0, handball_length], [0, 0], color="white")
    ax.plot([0, handball_length], [handball_width, handball_width], color="white")
    ax.plot([0, 0], [0, handball_width], color="white")
    ax.plot([handball_length, handball_length], [0, handball_width], color="white")

    # منطقة المرمى
    ax.plot([6, 6], [(handball_width - 7) / 2, (handball_width + 7) / 2], color="white")
    ax.plot([handball_length - 6, handball_length - 6], [(handball_width - 7) / 2, (handball_width + 7) / 2], color="white")

    # إعداد الرسم
    ax.set_facecolor("#2c3e50")
    ax.set_xlim(0, handball_length)
    ax.set_ylim(0, handball_width)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig

def draw_volleyball_field(volleyball_length, volleyball_width):
    fig, ax = plt.subplots(figsize=(9, 6))

    # رسم الحدود الخارجية
    ax.plot([0, volleyball_length], [0, 0], color="white")
    ax.plot([0, volleyball_length], [volleyball_width, volleyball_width], color="white")
    ax.plot([0, 0], [0, volleyball_width], color="white")
    ax.plot([volleyball_length, volleyball_length], [0, volleyball_width], color="white")

    # رسم خط المنتصف
    ax.plot([volleyball_length / 2, volleyball_length / 2], [0, volleyball_width], color="white")

    # إعداد الرسم
    ax.set_facecolor("#2c3e50")
    ax.set_xlim(0, volleyball_length)
    ax.set_ylim(0, volleyball_width)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig

def draw_basketball_field(basketball_length, basketball_width):
    fig, ax = plt.subplots(figsize=(8, 5))

    # رسم الحدود الخارجية
    ax.plot([0, basketball_length], [0, 0], color="white")
    ax.plot([0, basketball_length], [basketball_width, basketball_width], color="white")
    ax.plot([0, 0], [0, basketball_width], color="white")
    ax.plot([basketball_length, basketball_length], [0, basketball_width], color="white")

    # رسم دائرة المنتصف
    center_circle = plt.Circle((basketball_length / 2, basketball_width / 2), 1.8, color="white", fill=False)
    ax.add_artist(center_circle)

    # إعداد الرسم
    ax.set_facecolor("#2c3e50")
    ax.set_xlim(0, basketball_length)
    ax.set_ylim(0, basketball_width)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig

# واجهة Streamlit
st.markdown('<div class="title">حاسبة قياسات الملاعب المصغرة</div>', unsafe_allow_html=True)
option = st.selectbox("اختر نوع الملعب:", ["كرة القدم", "كرة اليد", "الكرة الطائرة", "كرة السلة"])

if option == "كرة القدم":
    football_width = st.number_input("أدخل العرض الجديد لملعب كرة القدم (بالمتر):", min_value=0.0, step=0.5)
    if football_width > 0:
        football_length = football_width * 2
        goal_area_depth = (5.5 / 45) * football_width
        goal_area_width = (18.32 / 45) * football_width
        penalty_area_depth = (16.5 / 45) * football_width
        penalty_area_width = (40.3 / 45) * football_width
        center_circle_radius = (9.15 / 45) * football_width

        st.pyplot(draw_football_field(football_length, football_width, goal_area_depth, goal_area_width, penalty_area_depth, penalty_area_width, center_circle_radius))

elif option == "كرة اليد":
    handball_width = st.number_input("أدخل العرض الجديد لملعب كرة اليد (بالمتر):", min_value=0.0, step=0.5)
    if handball_width > 0:
        handball_length = handball_width * 2
        st.pyplot(draw_handball_field(handball_length, handball_width))

elif option == "الكرة الطائرة":
    volleyball_width = st.number_input("أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):", min_value=0.0, step=0.5)
    if volleyball_width > 0:
        volleyball_length = volleyball_width * 2
        st.pyplot(draw_volleyball_field(volleyball_length, volleyball_width))

elif option == "كرة السلة":
    basketball_width = st.number_input("أدخل العرض الجديد لملعب كرة السلة (بالمتر):", min_value=0.0, step=0.5)
    if basketball_width > 0:
        basketball_length = basketball_width * 2 - 2
        st.pyplot(draw_basketball_field(basketball_length, basketball_width))

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية - محافظة مسقط
    </div>
    """, unsafe_allow_html=True)
