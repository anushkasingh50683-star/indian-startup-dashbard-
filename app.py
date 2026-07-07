import streamlit as st
import pandas as pd

df = pd.read_csv('startup_funding.csv')

df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')

df['Startup Name'] = df['Startup Name'].fillna('Unknown')

