# src/mm_graph_rag/graph/schema.py
from pydantic import BaseModel, Field


class Entity(BaseModel):
    id: str = Field(description="Unique lowercased entity identifier e.g. 'alice'")
    type: str = Field(description="Entity category e.g. 'PERSON', 'CONCEPT', 'OBJECT'")
    description: str = Field(description="Brief description of the entity")

class Relationship(BaseModel):
    source: str = Field(description="Source entity ID")
    target: str = Field(description="Target entity ID")
    relation: str = Field(description="Relationship type e.g. 'USES', 'LOCATED_IN'")

class GraphExtraction(BaseModel):
    entities: list[Entity]
    relationships: list[Relationship]