# Core Packages
import streamlit as st 
import os
import base64


#NLP Pkgs
import spacy
from spacy import displacy
nlp = spacy.load('en')

# Time Pkg
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

# Templates
file_name = 'yourdocument' + timestr + '.txt'
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


# Functions to Sanitize and Redact 
def sanitize_names(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'PERSON':
            redacted_sentences.append("[REDACTED NAME]")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)

def sanitize_places(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'GPE':
            redacted_sentences.append("[REDACTED PLACE]")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)

def sanitize_date(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'DATE':
            redacted_sentences.append("[REDACTED DATE]")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)

def sanitize_org(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'ORG':
            redacted_sentences.append("[REDACTED]")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)


def writetofile(text,file_name):
	with open(os.path.join('downloads',file_name),'w') as f:
		f.write(text)

def make_downloadable(filename):
	readfile = open(os.path.join("downloads",filename)).read()
	b64 = base64.b64encode(readfile.encode()).decode()
	href = '<a href="data:file/readfile;base64,{}">Download File File</a> (right-click and save as &lt;some_name&gt;.txt)'.format(b64)
	return href

@st.cache
def render_entities(rawtext):
	docx = nlp(rawtext)
	html = displacy.render(docx,style="ent")
	html = html.replace("\n\n","\n")
	result = HTML_WRAPPER.format(html)
	return result


def main():
	"""Document Redaction with Streamlit"""
	st.title("Document Redactor App")
	st.text("Built with Streamlit and SpaCy")

	activities = ["Redaction","Downloads","About"]
	choice = st.sidebar.selectbox("Select Choice",activities)

	if choice == 'Redaction':
		st.subheader("Redaction of Terms")

		rawtext = st.text_area("Enter Text","Type Here")
		redaction_item = ["names","places","org","date"]
		redaction_choice = st.selectbox("Select Item to Censor",redaction_item)
		save_option = st.radio("Save to File",("Yes","No"))
		if st.button("Submit"):
			if save_option == 'Yes':
				if redaction_choice == 'redact_names':
					result = sanitize_names(rawtext)
				elif redaction_choice == 'places':
					result = sanitize_places(rawtext)
				elif redaction_choice == 'date':
					result = sanitize_date(rawtext)
				elif redaction_choice == 'org':
					result = sanitize_org(rawtext)
				else:
					result = sanitize_names(rawtext)
				st.subheader("Original Text")
				new_docx = render_entities(rawtext)
				st.markdown(new_docx,unsafe_allow_html=True)

				st.subheader("Redacted Text")

				st.write(result)
				writetofile(result,file_name)
				st.info("Saved Result As :: {}".format(file_name))
			else:
				if redaction_choice == 'redact_names':
					result = sanitize_names(rawtext)
				elif redaction_choice == 'places':
					result = sanitize_places(rawtext)
				elif redaction_choice == 'date':
					result = sanitize_date(rawtext)
				elif redaction_choice == 'org':
					result = sanitize_org(rawtext)
				else:
					result = sanitize_names(rawtext)

				st.write(result)
			



	elif choice == 'Downloads':
		st.subheader("Downloads List")
		files = os.listdir(os.path.join('downloads'))
		file_to_download = st.selectbox("Select File To Download",files)
		st.info("File Name: {}".format(file_to_download))
		d_link = make_downloadable(file_to_download)
		st.markdown(d_link,unsafe_allow_html=True)

	elif choice == 'About':
		st.subheader("About The App & Credits ")

		st.text("MarcSkovMadsen @awesomestreamlit.org")
		st.text("Adrien Treuille @streamlit")
		st.text("Jesse E.Agbe @JCharisTech")

		st.success("Jesus Saves@JCharisTech")








if __name__ == '__main__':
	main()
