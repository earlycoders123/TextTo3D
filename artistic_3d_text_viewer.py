
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="🎨 Artistic 3D Text Viewer", layout="centered")
st.title("🌟 Artistic 3D Text Viewer for Kids")

user_text = st.text_input("✏️ Type your magical message", "Hello World!")
text_color = st.color_picker("🎨 Pick your text color", "#ff5733")

font_options = {
    "Comic": "Comic Sans MS",
    "Bubble": "Arial Black",
    "Cursive": "Brush Script MT",
    "Fantasy": "Impact",
    "Classic": "Times New Roman"
}
font_choice = st.selectbox("🔤 Choose a font style", list(font_options.keys()))
effect = st.selectbox("💫 Choose a 3D-like effect", ["None", "Shadow", "Glow", "Outline"])

font_selected = font_options[font_choice]
shadow_offset = dict(x=0.1, y=-0.1, z=0) if effect == "Shadow" else dict(x=0, y=0, z=0)

fig = go.Figure()

if effect in ["Shadow", "Glow", "Outline"]:
    fig.add_trace(go.Scatter3d(
        x=[shadow_offset["x"]],
        y=[shadow_offset["y"]],
        z=[shadow_offset["z"]],
        mode='text',
        text=[user_text],
        textfont=dict(size=32, color='black', family=font_selected),
        opacity=0.5,
    ))

fig.add_trace(go.Scatter3d(
    x=[0],
    y=[0],
    z=[0],
    mode='text',
    text=[user_text],
    textfont=dict(size=32, color=text_color, family=font_selected),
))

fig.update_layout(
    scene_camera=dict(eye=dict(x=1.5, y=1.5, z=1)),
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
