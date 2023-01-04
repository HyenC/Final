import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="줌인줌아웃",
    page_icon="📸",
    layout="wide"
)

# sidebar
with st.sidebar:
    st.markdown("## 📸줌인줌아웃📸")
    st.markdown("#### 실시간 웹캠 자리비움 탐지 보고서")

# 녹화본 파일 띄우기
def main():
    video_file = open("data/final.mp4", "rb")
    st.video(video_file)

width = max(width, 0.01)
side = max((100 - width) / 2, 0.01)

_, container, _ = st.columns([side, width, side])
container.video(data=video_file)    

if __name__ == "__main__":
    main()
