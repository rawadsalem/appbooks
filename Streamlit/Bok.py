import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r"C:\Users\hp\Desktop\Data Sets\Books.csv"
data = pd.read_csv(file_path)

# Create a Streamlit app
st.title("Interactive Book Visualization")

# Add a sidebar for interactive features
st.sidebar.header("Interactive Features")

# Interactive feature 1: Time Frame Selector
selected_year = st.sidebar.slider("Select a Year", min_value=data['Year'].min(), max_value=data['Year'].max())

# Interactive feature 2: Genre Selector
selected_genre = st.sidebar.selectbox("Select a Genre", data['Genre'].unique())

# Filter the data based on selected features
filtered_data = data[(data['Year'] == selected_year) & (data['Genre'] == selected_genre)]

# Create Matplotlib figures
fig1, ax1 = plt.subplots()
sns.scatterplot(
    data=filtered_data,
    x='User Rating',
    y='Price',
    hue='Genre',
    size='Reviews',
    palette={'Fiction': 'blue', 'Non Fiction': 'green'},
    ax=ax1
)
ax1.set_title(f'Book Ratings, Prices, and Reviews in {selected_year} ({selected_genre})')
ax1.set_xlabel('User Rating')
ax1.set_ylabel('Price')
ax1.set_xlim(3, 5)
ax1.set_ylim(0, 25)

fig2, ax2 = plt.subplots()
sns.histplot(
    data=filtered_data,
    x='Price',
    y='User Rating',
    hue='Genre',
    palette={'Fiction': 'blue', 'Non Fiction': 'green'},
    ax=ax2
)
ax2.set_title(f'Price vs. User Rating in {selected_year} ({selected_genre})')
ax2.set_xlabel('Price In USD')
ax2.set_ylabel('User Rating On 5')

# Create a third visualization with an interactive feature
st.header("Additional Visualization")

# Interactive feature 3: Book Rating Distribution
selected_distribution = st.selectbox("Select a Rating Distribution", ["User Rating", "Reviews"])

fig3, ax3 = plt.subplots()
if selected_distribution == "User Rating":
    sns.histplot(
        data=filtered_data,
        x='User Rating',
        hue='Genre',
        palette={'Fiction': 'blue', 'Non Fiction': 'green'},
        ax=ax3
    )
    ax3.set_title(f'User Rating Distribution in {selected_year} ({selected_genre})')
    ax3.set_xlabel('User Rating')
else:
    sns.histplot(
        data=filtered_data,
        x='Reviews',
        hue='Genre',
        palette={'Fiction': 'blue', 'Non Fiction': 'green'},
        ax=ax3
    )
    ax3.set_title(f'Review Count Distribution in {selected_year} ({selected_genre})')
    ax3.set_xlabel('Review Count')

# Display the selected visualizations
st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)

# Optionally, you can add more text or explanations here
st.write("Explore book ratings, prices, and reviews over time with the interactive features on the sidebar.")

# Close the Streamlit app
st.write("Thank you for using the Book Visualization App!")
