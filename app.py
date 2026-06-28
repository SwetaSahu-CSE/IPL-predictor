import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl','rb'))
teams = pickle.load(open('teams.pkl','rb'))
cities= pickle.load(open('cities.pkl','rb'))
st.title("IPL Win Predictor")
col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox('select the batting team',sorted(teams))
with col2:
    bowling_team=st.selectbox('select the bowling team',sorted(teams))
col3,col4=st.columns(2)
with col3:
    selected_city=st.selectbox('select host city',sorted(cities))
with col4:
    target = st.selectbox("Target", range(1, 301))
score = st.selectbox("Score", range(0, 301))
overs_list = []

for over in range(20):
    for ball in range(6):
        overs_list.append(float(f"{over}.{ball}"))

overs_list.append(20.0)

overs = st.selectbox("Overs completed", overs_list)
wickets = st.selectbox("Wickets Out", range(0, 11))
if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    st.header(batting_team + " - " + str(round(win * 100)) + "%")
    st.header(bowling_team + " - " + str(round(loss * 100)) + "%")