
import streamlit as st
import pymupdf
import json

from src.predict import extract_entities
from agent.llm_agent import analyze_resume


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Resume Profile Extractor",
    page_icon="📄",
    layout="wide"
)


# ==========================================
# 2. HEADER
# ==========================================

st.title("Resume Profile Extractor")

st.write(
    "Upload your resume and supporting documents "
    "to extract and organize candidate information."
)

st.divider()


# ==========================================
# 3. ENTITY LABELS
# ==========================================

ENTITY_NAMES = [
    "NAME",
    "EMAIL",
    "PHONE",
    "SKILL",
    "DEGREE",
    "COLLEGE",
    "COMPANY",
    "DESIGNATION",
    "EXPERIENCE",
    "LOCATION",
    "GRADUATION_YEAR",
    "CERTIFICATION"
]

DISPLAY_NAMES = {
    "NAME": "Full Name",
    "EMAIL": "Email Address",
    "PHONE": "Phone Number",
    "SKILL": "Skills",
    "DEGREE": "Degree",
    "COLLEGE": "College / University",
    "COMPANY": "Company",
    "DESIGNATION": "Designation",
    "EXPERIENCE": "Work Experience",
    "LOCATION": "Location",
    "GRADUATION_YEAR": "Graduation Year",
    "CERTIFICATION": "Certifications"
}


# ==========================================
# 4. PDF TEXT EXTRACTION
# ==========================================

def extract_pdf_text(pdf_file):

    pdf = pymupdf.open(
        stream=pdf_file.getvalue(),
        filetype="pdf"
    )

    extracted_text = []

    try:
        for page_number, page in enumerate(pdf, start=1):

            page_text = page.get_text("text")

            extracted_text.append(
                f"\n--- Page {page_number} ---\n{page_text}"
            )

    finally:
        pdf.close()

    return "\n".join(extracted_text).strip()


# ==========================================
# 5. DOCUMENT UPLOAD
# ==========================================

st.subheader("Upload Documents")

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"],
    key="resume"
)

supporting_files = st.file_uploader(
    "Supporting Documents (Optional)",
    type=["pdf"],
    accept_multiple_files=True,
    key="supporting"
)

st.caption(
    "You can also upload certificates, marksheets "
    "and experience letters."
)


# ==========================================
# 6. ANALYZE BUTTON
# ==========================================

if st.button(
    "Analyze Resume",
    type="primary",
    use_container_width=True,
    disabled=resume_file is None
):

    try:

        # --------------------------------------
        # STEP 1: READ MAIN RESUME
        # --------------------------------------

        with st.spinner("Processing your documents..."):

            resume_text = extract_pdf_text(resume_file)

            if not resume_text:

                st.error(
                    "No readable text found in this PDF. "
                    "Please upload a text-based PDF."
                )

                st.stop()

        # --------------------------------------
        # STEP 2: READ SUPPORTING DOCUMENTS
        # --------------------------------------

        supporting_text = ""

        if supporting_files:

            with st.spinner("Processing supporting documents..."):

                for document in supporting_files:

                    document_text = extract_pdf_text(document)

                    supporting_text += (
                        f"\n\nDocument: {document.name}\n"
                        f"{document_text}"
                    )

        # --------------------------------------
        # STEP 3: EXTRACT INFORMATION
        # --------------------------------------

        with st.spinner("Extracting candidate information..."):

            bert_results = extract_entities(resume_text)

        # --------------------------------------
        # STEP 4: REVIEW INFORMATION
        # --------------------------------------

        with st.spinner("Preparing your candidate profile..."):

            reviewed_results = analyze_resume(
                resume_text=resume_text,
                bert_entities=bert_results,
                supporting_documents=supporting_text
            )

        # --------------------------------------
        # STEP 5: FINAL PROFILE
        # --------------------------------------

        final_profile = {}

        for entity in ENTITY_NAMES:

            final_profile[entity] = []

        for item in reviewed_results.get("field_reviews", []):

            entity = item.get("entity")

            if entity not in final_profile:
                continue

            values = item.get("recommended_values", [])

            if isinstance(values, str):
                values = [values] if values.strip() else []

            final_profile[entity] = [
                str(value).strip()
                for value in values
                if str(value).strip()
            ]

        # Save results in session
        st.session_state["final_profile"] = final_profile
        st.session_state["resume_filename"] = resume_file.name
        st.session_state["resume_text"] = resume_text
        st.session_state["analysis_complete"] = True

    except Exception as error:

        st.error(
            "Unable to process the documents. "
            "Please try again."
        )

        with st.expander("Technical error details"):

            st.code(str(error))


# ==========================================
# 7. DISPLAY FINAL PROFILE
# ==========================================

if st.session_state.get("analysis_complete", False):

    final_profile = st.session_state["final_profile"]

    st.divider()

    st.success("Profile successfully prepared!")

    st.header("Candidate Profile")

    st.caption(
        f"Resume: {st.session_state['resume_filename']}"
    )

    # --------------------------------------
    # PROFILE INFORMATION
    # --------------------------------------

    col1, col2 = st.columns(2)

    for index, entity in enumerate(ENTITY_NAMES):

        values = final_profile.get(entity, [])

        current_col = col1 if index % 2 == 0 else col2

        with current_col:

            with st.container(border=True):

                st.markdown(
                    f"**{DISPLAY_NAMES[entity]}**"
                )

                if values:

                    for value in values:
                        st.write(f"• {value}")

                else:

                    st.write("Not Found")

    # --------------------------------------
    # MISSING INFORMATION
    # --------------------------------------

    missing_fields = [
        DISPLAY_NAMES[entity]
        for entity in ENTITY_NAMES
        if not final_profile.get(entity)
    ]

    st.divider()

    st.header("Missing Information")

    if missing_fields:

        st.warning(
            f"{len(missing_fields)} information field(s) "
            "could not be found in the available documents."
        )

        for field in missing_fields:
            st.write(f"• {field}")

    else:

        st.success("All information fields have values.")

    # --------------------------------------
    # DOWNLOAD PROFILE
    # --------------------------------------

    st.divider()

    st.subheader("Download Candidate Profile")

    downloadable_profile = {
        "candidate": st.session_state["resume_filename"],
        "profile": {
            DISPLAY_NAMES[entity]: final_profile[entity]
            for entity in ENTITY_NAMES
        }
    }

    json_data = json.dumps(
        downloadable_profile,
        indent=4,
        ensure_ascii=False
    )

    st.download_button(
        label="Download Profile (JSON)",
        data=json_data,
        file_name="candidate_profile.json",
        mime="application/json",
        use_container_width=True
    )

    # --------------------------------------
    # ORIGINAL RESUME TEXT
    # --------------------------------------

    with st.expander("View Extracted Resume Content"):

        st.text_area(
            "Resume Content",
            st.session_state["resume_text"],
            height=300
        )

    # --------------------------------------
    # RESET
    # --------------------------------------

    if st.button("Analyze Another Resume"):

        st.session_state["analysis_complete"] = False
        st.session_state.pop("final_profile", None)
        st.session_state.pop("resume_filename", None)
        st.session_state.pop("resume_text", None)

        st.rerun()
