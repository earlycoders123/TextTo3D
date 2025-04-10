
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="🌀 Text to 3D Viewer", layout="centered")
st.title("🌟 Text to 3D Viewer")

user_text = st.text_input("🎈 Type something fun!", "Hello 3D World")
text_color = st.color_picker("🎨 Pick a color for your text", "#ff6347")

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=[0],
    y=[0],
    z=[0],
    mode='text',
    text=[user_text],
    textfont=dict(size=30, color=text_color),
))

fig.update_layout(
    scene_camera=dict(eye=dict(x=1.5, y=1.5, z=0.5)),
    scene=dict(
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=False, visible=False),
        zaxis=dict(showgrid=False, visible=False),
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)
