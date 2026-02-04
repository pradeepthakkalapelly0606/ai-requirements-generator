import streamlit as st
from openai import OpenAI

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Requirements → User Stories Generator")

req = st.text_area("Paste your requirement here:")

if st.button("Generate Stories"):
    prompt = f"""
    Convert this requirement into:

    1. User Stories
    2. Acceptance Criteria
    3. Edge Cases
    4. Test Cases

    Requirement:
    {req}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    output = response.choices[0].message.content

    st.write(output)

    st.download_button(
        label="Download as TXT",
    	data=output,
    	file_name="requirements_output.txt",
    	mime="text/plain"
	)

