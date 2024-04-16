import openai
import streamlit as st

# Read the API key from the file
with open("keys/openai_api_key.txt") as f:
    key = f.read().strip()

# Set your OpenAI API key
openai.api_key = key

st.title("An AI Code Reviewer App")

# Input for the user's Python code
code = st.text_area("Enter your Python or java or c code here:", height=200)

if st.button("Review"):
    try:
        # Use the OpenAI API to analyze the code
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "system", "content": "You are a helpful AI Assistant"},
                {"role": "user", "content": code}
            ]
        )

        # Process the API response to extract suggestions
        suggestions = response["choices"][0]["message"]["content"]
        
        # Display the suggestions to the user
        st.markdown("**Code Review:**")
        st.code(suggestions, language="java" if "public static void main" in code else "c" if "int main()" in code else "python")
    except Exception as e:
        st.error(f"An error occurred: {e}")
