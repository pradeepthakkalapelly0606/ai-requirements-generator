import streamlit as st
from openai import OpenAI

import os
st.set_page_config(
    page_title="AI Requirements Generator",
    page_icon="🤖",
    layout="wide"
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🤖 AI Requirements → User Stories Generator")
st.caption("Convert raw requirements into structured Agile stories instantly")

req = st.text_area(
    "📌 Paste your requirement below:",
    height=200
)

if st.button("✨ Generate Stories"):
    with st.spinner("Generating stories using AI..."):
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

    	st.text_area("Result", value=output, height=400)

    	st.download_button(
        	label="Download as TXT",
    		data=output,
    		file_name="requirements_output.txt",
    		mime="text/plain"
	)
st.markdown("---")
st.caption("Built using Python + Streamlit + OpenAI API")

