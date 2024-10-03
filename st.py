import streamlit as st

# Set the title of the app
st.title("Handsome Husband For Tasnim")

# Display the first image
image_path_1 = "image2.png"  # Replace with your first image path
st.image(image_path_1, caption="A handsome husband for Tasnim!", use_column_width=True)

# Display the second image
image_path_2 = "image3.jpg"  # Replace with your second image path
st.image(image_path_2, caption="Another handsome look!", use_column_width=True)
