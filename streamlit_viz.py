from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

    # Import and show world happiness dataset for 2015.
world_happiness_2015 = pd.read_csv('https://www.dropbox.com/s/jzeoltl0nakjqyg/2015.csv?dl=1')
world_happiness_2016 = pd.read_csv('https://www.dropbox.com/s/kg35k13y3vmadn0/2016.csv?dl=1')
world_happiness_2017 = pd.read_csv('https://www.dropbox.com/s/ku2dg5cq2gqqzjs/2017.csv?dl=1')
world_happiness_2018 = pd.read_csv('https://www.dropbox.com/s/1yr0htr2daq42sq/2018.csv?dl=1')
world_happiness_2019 = pd.read_csv('https://www.dropbox.com/s/hnu8ic6jpnxkmnk/2019.csv?dl=1')
world_happiness_2015
