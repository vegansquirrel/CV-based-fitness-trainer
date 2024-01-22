import streamlit as st


st.title('AI Fitness Trainer: Squats Analysis')


recorded_file = 'squat_video.webm'
sample_vid = st.empty()
sample_vid.video(recorded_file)