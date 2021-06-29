import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('University_Rank.csv')

def line_plot(column):
    x = df[column]
    y = df['Overall_Score']

    plt.scatter(x, y)
    plt.xlabel(str(column))
    plt.ylabel('Overall Score')
    title = 'Overall Score vs. ' + str(column)
    plt.title(title)

    return plt

def main():
    df = pd.read_csv('University_Rank.csv')
    factor = ['International_Student_Ratio', 'International_Faculty_Ratio', 'Faculty_Student_Ratio', 'Citations_per_Faculty', 'Academic_Reputation', 'Employer_Reputation']
    st.title("QS Top 30 University Analysis")
    data_load_state = st.text('Loading data...')
    data_load_state.text("Finished loading data!")
    column = st.sidebar.multiselect('Select a factor', factor)
    st.pyplot(line_plot(column))

main()
