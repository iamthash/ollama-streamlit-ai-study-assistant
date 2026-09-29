import streamlit as st
import ollama
st.title("AI Study Assistant")
question = st.text_input("Ask your question:")
if st.button("Ask AI"):
    if question:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        answer = response["message"]["content"]
        st.write(answer)
    else:
        st.warning("Please enter a question.")