# 🍿 MM-Graph-RAG Configurations

The first step to get started with the framework is setting up your configuration.
All the key parameters can be easily adjusted in the [`config.yml`](/mm-graph-rag/config/config.yml) file. Tweak them to match your experiment needs!

| Item            | Type   | Description                            |
| --------------- | ------ | -------------------------------------- |
| `model_name`    | String | The employed MM-LLM                    |
| `device`        | String | The device used for running the system |
| `whisper_model` | String | The whisper model                      |
| `graph_depth`   | Int    | The depth of the graph for retrieval   |