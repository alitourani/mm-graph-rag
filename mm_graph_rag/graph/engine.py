import networkx as nx
from llama_index.llms.litellm import LiteLLM
from mm_graph_rag.config.config import Config
from llama_index.core import Document, PropertyGraphIndex, Settings
from llama_index.core.graph_stores import SimplePropertyGraphStore
from llama_index.embeddings.gemini import GeminiEmbedding


class GraphRAGCore:

  def __init__(self, config: Config):
    self.config = config

    # 1. Configure free LLM via LiteLLM
    self.llm = LiteLLM(model_name=config.llm_model, api_key=config.api_key)

    # 2. Configure Gemini Embedding model
    self.embed_model = GeminiEmbedding(
        model_name="models/text-embedding-004", api_key=config.api_key
    )

    # 3. Register globally in LlamaIndex Settings to avoid OpenAI defaults
    Settings.llm = self.llm
    Settings.embed_model = self.embed_model

    # Initialize Property Graph Store
    self.graph_store = SimplePropertyGraphStore()
    self.nx_graph = nx.DiGraph()  # Mirror store for visualization

    # 4. Pass embed_model explicitly to PropertyGraphIndex
    self.index = PropertyGraphIndex.from_documents(
        [],
        property_graph_store=self.graph_store,
        llm=self.llm,
        embed_model=self.embed_model,
    )

  def add_extracted_text(self, text: str, source_id: str, media_type: str):
    doc = Document(
        text=text, doc_id=source_id, metadata={"media_type": media_type}
    )
    self.index.insert(doc)

    # Syncing nodes into NetworkX for visualization
    for node in self.index.property_graph_store.get_nodes():
      self.nx_graph.add_node(node.name, label=node.name)

  def query(self, query_str: str) -> str:
    # Pass embed_model and llm explicitly to the query engine
    query_engine = self.index.as_query_engine(
        llm=self.llm, embed_model=self.embed_model
    )
    response = query_engine.query(query_str)
    return str(response)