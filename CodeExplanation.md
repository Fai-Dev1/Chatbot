# Chatbot Code Explanation

This document provides a detailed explanation of the `chatbot.py` script, following a structured format with explanations and code blocks.

---

## 1. Import Required Libraries

The script begins by importing the necessary libraries:

- **`openai`**: To interact with the OpenAI API.
- **`streamlit`**: To build the web UI.
- **`os`**: To load environment variables.
- **`dotenv`**: To load environment variables from a `.env` file.

```python
from openai import OpenAI
import streamlit as st
import os 
from dotenv import load_dotenv
```

---

## 2. Set Page Title

The `st.title()` function is used to set the page title, enhancing user experience by providing a clear heading.

```python
st.title("Chatbot basic")
```

---

## 3. Load Environment Variables

The `load_dotenv()` function loads environment variables from the `.env` file, which helps keep sensitive credentials secure.

```python
load_dotenv()
```

---

## 4. Initialize OpenAI Client

The script retrieves the API key from environment variables and initializes an OpenAI client using the retrieved key.

```python
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
```

---

## 5. Initialize Session State

Streamlit provides session state to maintain the chatbot's data across multiple interactions. It initializes two key values:

- **`openai_model`**: Stores the default model (gpt-5.6-luna).
- **`messages`**: Holds chat history to persist across interactions.

```python
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-5.6-luna"

if "messages" not in st.session_state:
    st.session_state.messages = []
```

---

## 6. Display Chat History

The script iterates over previous messages stored in the session state and displays them using `st.chat_message()`.

```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

---

## 7. Handle User Input

When the user enters text, it is added to the session state and displayed on the interface.

```python
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
```

---

## 8. Send Request to OpenAI API

The input message along with the previous chat history is sent to the OpenAI API, and responses are received in a streaming fashion.

```python
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
```

---

## 9. Store Assistant Response

The chatbot's response is stored in session state to maintain conversation continuity.

```python
    st.session_state.messages.append({"role": "assistant", "content": response})
```

---

## 10. Dependency Installation

To run the chatbot, install the required dependencies using the command below.

```bash
pip install openai streamlit python-dotenv
```

---

## 11. Running the Application

Run the chatbot using the following command, and it will open in the default web browser.

```bash
streamlit run chatbot.py
```
