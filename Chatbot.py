import streamlit as st

st.title('Indian Constitution Chatbot')

user_input = st.text_input('Ask a question about the Indian Constitution')

if st.button('Submit'):
    if user_input:
        # Generate the chatbot response
        response = generate_chatbot_response(user_input)
        st.write('Chatbot Response:')
        st.write(response)
    else:
        st.write('Please enter a question.')