# Corporate Knowledge Agent

Agente de IA corporativo capaz de responder perguntas de colaboradores/clientes combinando:
- **Dados não estruturados** (políticas, manuais, FAQs) via RAG
- **Dados estruturados** (métricas, status, relatórios) via consulta a banco de dados
- **Segurança** contra prompt injection e vazamento de PII
- **Observabilidade** completa em produção

Projeto desenvolvido durante o bootcamp **Production-Ready AI with Google Cloud**.

## Stack
- **Modelo**: Gemini via Vertex AI SDK
- **Orquestração de agentes**: Agent Development Kit (ADK)
- **RAG**: AlloyDB / Cloud SQL (pgvector)
- **Integração de dados**: MCP + MCP Toolbox
- **Comunicação entre agentes**: A2A
- **Segurança**: Model Armor + Sensitive Data Protection
- **Deploy**: Cloud Run / GKE / Agent Engine
- **Avaliação**: Vertex AI Evaluation

## Progresso
- [x] Dia 1 — App base com Vertex AI SDK (`src/agents/base_chatbot.py`)
- [ ] Dia 2 — Agentes com ADK
- [ ] Dia 3 — RAG avançado
- [ ] Dia 4 — MCP + A2A
- [ ] Dia 5 — Segurança
- [ ] Dia 6 — Deploy + observabilidade
- [ ] Dia 7 — Avaliação

#ProductionReadyAI
