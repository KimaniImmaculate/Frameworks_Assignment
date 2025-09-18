import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset with caching
@st.cache_data
def load_data(nrows=100000):
    # Only load useful columns to save memory
    usecols = ['title', 'publish_time', 'journal', 'authors', 'source_x']
    df = pd.read_csv('metadata.csv', usecols=usecols, nrows=nrows, low_memory=False)
    
    # Clean: drop rows missing title or publish_time
    df = df.dropna(subset=['title', 'publish_time'])
    
    # Convert publish_time to datetime and extract year
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    
    # Fill missing journals with "Unknown"
    df['journal'] = df['journal'].fillna("Unknown")
    
    return df

df = load_data()

# Title of the app
st.title("CORD-19 Research Paper Analysis")

# Show sample of the data
st.subheader("Sample Data")
st.dataframe(df.head())

# Publication Year Distribution
st.subheader("Publication Year Distribution")
year_counts = df['year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(30,10))
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, palette="viridis")
ax.set_title("Number of Papers Published by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Top Sources
st.subheader("Top 10 Sources by Paper Count")
source_counts = df['source_x'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=source_counts.values, y=source_counts.index, ax=ax, palette="viridis")
ax.set_title("Top 10 Sources by Paper Count")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Source")
st.pyplot(fig)

# Search for Papers by Keyword
st.subheader("Search for Papers by Keyword")
keyword = st.text_input("Enter a keyword:")
if keyword:
    results = df[df['title'].str.contains(keyword, case=False, na=False)]
    st.write(results[['title', 'publish_time', 'journal', 'authors']].head(10))
