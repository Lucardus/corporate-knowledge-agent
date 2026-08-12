# Corporate Knowledge Agent

A corporate AI agent capable of answering questions from employees and clients by combining:
- **Unstructured data** (policies, manuals, FAQs) via RAG
- **Structured data** (metrics, status, reports) via database queries
- **Security** against prompt injection and PII leakage
- **Full observability** in production

Project developed during the Triggo.ai **Production-Ready AI with Google Cloud** bootcamp.

## Stack
- **Model**: Gemini via Vertex AI SDK
- **Agent orchestration**: Agent Development Kit (ADK)
- **RAG**: AlloyDB / Cloud SQL (pgvector)
- **Data integration**: MCP + MCP Toolbox
- **Agent-to-agent communication**: A2A
- **Security**: Model Armor + Sensitive Data Protection
- **Deployment**: Cloud Run / GKE / Agent Engine
- **Evaluation**: Vertex AI Evaluation

## Progress
- [x] Day 1 — Base app with Vertex AI SDK (`src/agents/base_chatbot.py`)
- [x] Day 2 — Agents with ADK
- [ ] Day 3 — Advanced RAG
- [ ] Day 4 — MCP + A2A
- [ ] Day 5 — Security
- [ ] Day 6 — Deployment + observability
- [ ] Day 7 — Evaluation

#ProductionReadyAI
