# KnowBear: Advanced Knowledge Orchestration Engine

KnowBear is a high-performance, modular knowledge engine designed for multi-layered information synthesis and delivery. It leverages a hybrid RAG (Retrieval-Augmented Generation) pipeline integrated with a multi-agent ensemble inference system to provide depth-adjustable explanations.

## Architecture Architecture

The system is built on a decoupled micro-architecture:

### 1. Unified Inference Orchestration (Backend)
- **FastAPI Core**: High-concurrency asynchronous API layer ensuring sub-millisecond overhead.
- **Multi-Agent Ensemble**: A proprietary (abstracted) voting and judging logic that orchestrates multiple LLM providers (Groq, Gemini, etc.) to ensure high-fidelity output.
- **Context-Aware RAG**: Integrates specialized search providers (Tavily, Serper, Exa) to inject real-time grounded context into the inference loop.
- **Layered Explanation Logic**: Implements a progressive depth system (ELI5 to Technical Depth) via specialized prompt engineering and Chain-of-Thought (CoT) distillation.

### 2. Distributed Caching & State
- **Redis L2 Cache**: High-performance persistent storage for expensive inference results, implementing smart TTL and invalidation strategies.
- **L1 In-Memory Caching**: Local caching for frequent lookups to minimize network latency.
- **Supabase Integration**: Relational persistence for user state, query history, and metadata with robust RLS (Row Level Security) policies.

### 3. Progressive Neural UI (Frontend)
- **React + TypeScript**: Type-safe, component-driven architecture for rapid iteration and stability.
- **Tailwind CSS**: Utility-first design system with a premium, low-latency visual aesthetic.
- **Streaming Response Architecture**: Server-Sent Events (SSE) integration for real-time, token-by-token UI updates, enhancing perceived performance.
- **Modular Visualizations**: Integrated Mermaid.js for dynamic architectural and flow diagrams.

## Tech Stack

- **Inference**: Groq (Llama 3.x), Google GenAI (Gemini 2.0 Flash)
- **Backend**: Python 3.11, FastAPI, Pydantic, Structlog, Redis
- **Frontend**: Vite, React 18, Framer Motion, Lucide React, Tailwind CSS
- **Database**: Supabase (PostgreSQL), Drizzle ORM
- **Infrastructure**: Vercel Serverless Functions

## Key Features

- **Dynamic Depth Switching**: Instantaneous toggling between various cognitive complexity levels.
- **Ensemble Inference**: Cross-model validation to minimize hallucinations and maximize technical accuracy.
- **Architecture Visualization**: Automatic generation of technical diagrams for complex topics.
- **Advanced Export System**: Multi-format synthesis (Markdown, TXT) for offline knowledge ingestion.
- **Rate-Limited Resilience**: Integrated leaky-bucket rate limiting via Redis to maintain system stability under load.

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- Redis Server

### Installation
1. Clone the repository.
2. Initialize the backend:
   ```bash
   cd api
   pip install -r requirements.txt
   ```
3. Initialize the frontend:
   ```bash
   npm install
   ```
4. Configure environment variables in `.env` based on `.env.example`.
