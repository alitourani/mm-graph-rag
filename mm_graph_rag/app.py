import streamlit as st
import streamlit.components.v1 as components
from mm_graph_rag.config.config import Config
from mm_graph_rag.graph.engine import GraphRAGCore
from mm_graph_rag.graph.visualizer import GraphVisualizer
from mm_graph_rag.processors.vision_processor import VisionProcessor
from mm_graph_rag.processors.audio_processor import AudioProcessor

st.set_page_config(layout="wide", page_title="Multimodal Graph-RAG")


@st.cache_resource
def init_system():
    config = Config()
    engine = GraphRAGCore(config)
    vision_proc = VisionProcessor(config.llm_model, config.api_key)
    audio_proc = AudioProcessor(config.whisper_model)
    return engine, vision_proc, audio_proc


engine, vision_proc, audio_proc = init_system()

st.title("Multimodal Graph-RAG & Network Visualizer")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Data Ingestion")
    file_type = st.selectbox("Select Media Type", ["Text", "Image", "Audio"])
    uploaded_file = st.file_uploader("Upload File")

    if st.button("Process & Ingest") and uploaded_file:
        file_path = f"/tmp/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if file_type == "Text":
            text = uploaded_file.read().decode("utf-8")
        elif file_type == "Image":
            text = vision_proc.process_image(file_path)
        elif file_type == "Audio":
            text = audio_proc.process_audio(file_path)

        engine.add_extracted_text(
            text, source_id=uploaded_file.name, media_type=file_type.lower()
        )
        st.success(f"Successfully added {uploaded_file.name} to the Graph Store.")

    st.subheader("Query Engine")
    user_query = st.text_input("Ask a question across all modalities:")
    if st.button("Submit Query") and user_query:
        answer = engine.query(user_query)
        st.write("**Answer:**", answer)

with col2:
    st.subheader("Interactive Knowledge Graph")
    if st.button("Refresh Visualization"):
        html_file = GraphVisualizer.render_to_html(engine.nx_graph)
        with open(html_file, "r", encoding="utf-8") as f:
            components.html(f.read(), height=650, scrolling=True)
