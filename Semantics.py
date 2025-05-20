import streamlit as st
import oci
import json
import os
import time
import io

st.set_page_config(page_title="The Semantics", layout="wide")
st.title(" The Semantics")
st.markdown("---")

# OCI Configuration Settings
config = oci.config.from_file(profile_name="DEFAULT")
namespace = "oraseemeaukpubsec"
bucket = "teentech"
compartmentid = "ocid1.compartment.oc1..aaaaaaaawalowtjkgiov65xz6vifzfifep3ac4mgo2nschtetybzgxewpxmq"

# Read JSON Output Function
def readoutput():
    with open('output.json', 'r') as file:
        data = json.load(file)

    transcriptions = data.get("transcriptions", [])

    if not transcriptions:
        return "No transcription data found."

    # Join all segments if multiple transcriptions are returned
    full_transcript = " ".join(t.get("transcription", "") for t in transcriptions)
    return full_transcript.strip()

# Translate Function
def translate(text):
    compartment_id = "ocid1.tenancy.oc1..aaaaaaaaqn7onpvawffborst65pw657jueegix2axkk3pjf4jlfn76hcqg4q"
    config = oci.config.from_file(profile_name="DEFAULT")
    endpoint = "https://inference.generativeai.uk-london-1.oci.oraclecloud.com"
    textinput = text

    generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))
    chat_detail = oci.generative_ai_inference.models.ChatDetails()

    chat_request = oci.generative_ai_inference.models.CohereChatRequest()
    chat_request.message = f"Translate this to English:\n\n{textinput}"
    chat_request.max_tokens = 1000
    chat_request.temperature = 0
    chat_request.frequency_penalty = 0
    chat_request.top_p = 0.75
    chat_request.top_k = 0

    chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id="ocid1.generativeaimodel.oc1.uk-london-1.amaaaaaask7dceyahpidcahiiyhcdmnvicfxo7suq3pxcimkyik75mbxziqq")
    chat_detail.chat_request = chat_request
    chat_detail.compartment_id = compartment_id
    chat_response = generative_ai_inference_client.chat(chat_detail)

    translation = chat_response.data.chat_response.text
    return translation

# Transcribe Function
def transcribe(inputfile):
    ai_speech_client = oci.ai_speech.AIServiceSpeechClient(config)
    create_transcription_job_response = ai_speech_client.create_transcription_job(
            create_transcription_job_details=oci.ai_speech.models.CreateTranscriptionJobDetails(
                compartment_id=compartmentid,
                input_location=oci.ai_speech.models.ObjectListInlineInputLocation(
                    location_type="OBJECT_LIST_INLINE_INPUT_LOCATION",
                    object_locations=[oci.ai_speech.models.ObjectLocation(
                        namespace_name=namespace,
                        bucket_name=bucket,
                        object_names=[inputfile])]),
                output_location=oci.ai_speech.models.OutputLocation(
                    namespace_name=namespace,
                    bucket_name=bucket)))
    
    outputlocation = create_transcription_job_response.data.output_location.prefix
    jobid = create_transcription_job_response.data.id

    while True:
        jobstatus = ai_speech_client.get_transcription_job(transcription_job_id=jobid)
        if jobstatus.data.lifecycle_state == "ACCEPTED" or jobstatus.data.lifecycle_state == "IN_PROGRESS":
            time.sleep(10)
        else:
            break

    object_storage = oci.object_storage.ObjectStorageClient(config)
    output_filename = f"oraseemeaukpubsec_teentech_{inputfile}.json"
    get_obj = object_storage.get_object(namespace, bucket_name=bucket, object_name=outputlocation + output_filename)
    with open("output.json",'wb') as f:
        for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
            f.write(chunk)
    transcription = readoutput()
    if "transcription" not in st.session_state:
        st.session_state["transcription"] = transcription
    return transcription

def upload_to_object_storage(file_path, namespace, bucket_name, object_name, config):
    object_storage_client = oci.object_storage.ObjectStorageClient(config)
    with open(file_path, "rb") as file_data:
        object_storage_client.put_object(
            namespace_name=namespace,
            bucket_name=bucket_name,
            object_name=object_name,
            put_object_body=file_data
        )

# === Mission Briefing ===
st.header("Mission")
st.write("""
Welcome Semantics, we need your skills to figure out what motive is causing catastrophe!

Our Agents have collected a series of conversations and encrypted them!

Navigate through the transcripts - find the motive behind the catastrophe!

Use the keywords on the right to help inform your decision - You have three chances to decrypt the relevant transcript!

Use the notes section to track your thoughts!

Good Luck Agents!
""")

# === Preloaded Transcripts Info ===
transcripts = {
    "Transcript 1 🇮🇹 (Italian)": {
        "language": "Italian",
        "audio_file": "Transcript 1.mp3",
    },
    "Transcript 2 🇬🇷 (Greek)": {
        "language": "Greek",
        "audio_file": "Transcript 2.mp3",
    },
    "Transcript 3 🇳🇱 (Dutch)": {
        "language": "Dutch",
        "audio_file": "Transcript 3.mp3",
    },
    "Transcript 4 🇪🇸 (Spanish)": {
        "language": "Spanish",
        "audio_file": "Transcript 4.mp3",
    },
    "Transcript 5 🇨🇳 (Chinese)": {
        "language": "Chinese",
        "audio_file": "Transcript 5.mp3",
    },
}

# === Horizontal Selection of Transcripts ===
st.markdown("### 🎧 Choose a Transcript")

cols = st.columns(len(transcripts))
for idx, (label, transcript_info) in enumerate(transcripts.items()):
    if label == st.session_state.get("selected_transcript"):
        cols[idx].markdown(f"✅ **{label}**")
    else:
        if cols[idx].button(label):
            st.session_state.selected_transcript = label

# Fallback default
if "selected_transcript" not in st.session_state:
    st.session_state.selected_transcript = list(transcripts.keys())[0]

selected_key = st.session_state.selected_transcript
selected_transcript = transcripts[selected_key]

st.markdown(f"**Selected Language:** {selected_transcript['language']}")
audio_path = f"audio/{selected_transcript['audio_file']}"
st.audio(audio_path, format="audio/mp3")

st.markdown("---")
st.markdown("### 📝 Transcribe")

# Transcription
if st.button("Run Transcription"):
    try:
        # The audio file path on local system (relative or absolute)
        audio_local_path = audio_path  
        object_name = selected_transcript["audio_file"]

        with st.spinner("Uploading audio file to OCI Object Storage..."):
            upload_to_object_storage(
                file_path=audio_local_path,
                namespace=namespace,
                bucket_name=bucket,
                object_name=object_name,
                config=config
            )

        with st.spinner("Transcribing via OCI Speech..."):
            transcript_text = transcribe(object_name)

        st.session_state.transcript_text = transcript_text
        st.success("✅ Transcription completed!")

    except Exception as e:
        st.error(f"❌ Transcription failed: {e}")

if "transcript_text" in st.session_state:
    st.text_area("Transcript Output", value=st.session_state.transcript_text, height=150)

    st.markdown("### 🌍 Translate")

    if "translated_text" not in st.session_state:
        if st.button("Run Translation"):
            try:
                with st.spinner("Translating..."):
                    translated_text = translate(st.session_state.transcript_text)
                    st.session_state.translated_text = translated_text
                    st.success("✅ Translation completed!")
            except Exception as e:
                st.error(f"❌ Translation failed: {e}")
    else:
        st.success("✅ Translation already completed. Scroll down to view.")

if "translated_text" in st.session_state:
    st.text_area("Translation Output", value=st.session_state.translated_text, height=150)

    st.markdown("### 🔎 Step 3: Extract Key Phrases")

    if st.button("Run Key Phrase Extraction"):
        # TODO: Add actual OCI key phrase logic
        st.success("Key phrases extracted (placeholder).")
        st.session_state.key_phrases = ["example phrase 1", "example phrase 2", "example phrase 3"]

if "key_phrases" in st.session_state:
    st.markdown("**Key Phrases:**")
    for phrase in st.session_state.key_phrases:
        st.write(f"- {phrase}")

# Notes Section
st.markdown("---")
st.header("🗒️ Notes")
notes = st.text_area("Write your observations here...")

if notes:
    st.write("✅ Notes saved.")
