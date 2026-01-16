# ✈️ Flight Booking Agent — Flagship Agentic Systems Project

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-green)
![License](https://img.shields.io/badge/license-none-lightgrey)

A **production-style, fully working agent backend** demonstrating how to design, implement, and run a real agentic system using clean architecture principles.

This project is intentionally built to be:
- Cloneable  
- Runnable locally  
- Easy to understand  
- Architecturally honest  
- Portfolio-grade  

No fake folders. No placeholders. Everything runs.

---

## What this project demonstrates

- Agent orchestration using **Planner → Executor → Verifier**
- **Stateful multi-turn conversations**
- Robust natural language slot extraction (regex + dateparser)
- Validation logic (missing fields, invalid dates, bad inputs)
- Domain models (Flight, Booking)
- Repository abstraction for persistence
- Memory abstraction for user history
- Clean FastAPI backend with OpenAPI docs
- Tests, scripts, and documentation
- CI-ready project layout

This is not a toy demo — it is a working backend system.

---

## Example conversations (try these!)

These work both via the API and via `scripts/smoke_test.py`.

### Multi-turn conversation
```
User: Book me a flight
Agent: Sure — where are you flying from?

User: from sfo
Agent: Got it. Where would you like to go?

User: to jfk tomorrow for 2 people
Agent: Booked JetBlue FL5823 for $256. Confirmation: CONF635038
```

### Single-turn requests
```
"book flight from sfo to jfk tomorrow"
"2 people from austin to seattle next friday"
"fly from lax to chicago today"
```

These demonstrate:
- Slot-filling
- Validation
- Stateful behavior
- End-to-end tool execution

---

## Architecture Overview

```
Client
  ↓
FastAPI API Layer
  ↓
AgentGraph (Orchestrator)
  ├── Planner   → Extracts intent + slots
  ├── Executor  → Calls tools
  └── Verifier  → Ensures valid outcome
  ↓
Tools (Flight search / Booking)
  ↓
Repository (Persistence abstraction)
  ↓
Memory (User history abstraction)
```

The architecture is modular and extensible:
- Tools can be swapped with real APIs (Amadeus, Skyscanner, etc.)
- Repository can be replaced with Postgres
- Planner can be replaced with an LLM
- Memory can be replaced with a vector DB

---

## Project Structure

```
app/
  api/            # FastAPI endpoints
  agent/          # Agent orchestration + nodes
  tools/          # External capability layer
  models/         # Domain models
  db/             # Repository abstraction
  memory/         # Memory abstraction
  core/           # Shared types and errors
  config/         # Configuration
scripts/          # Local dev + demo scripts
tests/            # Automated tests
docs/             # Architecture notes
```

Every folder is intentional. Nothing is decorative.

---

## Running locally

### 1. Create environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run smoke test (fastest validation)
```bash
PYTHONPATH=. python scripts/smoke_test.py
```

Expected output:
```
Sure — where are you flying from?
Got it. Where would you like to go?
Booked JetBlue FL5823 for $256. Confirmation: CONF635038
```

### 4. Run API server
```bash
python -m uvicorn app.api.main:app --reload
```

Open:
http://127.0.0.1:8000/docs

Try `/chat`:
```json
{
  "user_id": "demo",
  "message": "book flight from sfo to jfk tomorrow for 2 people"
}
```

---

## Why this stands out from typical projects

Most agent demos:
- Hardcoded flows  
- No validation  
- No state  
- No tests  
- No architecture  

This project includes:
- Real conversational flow  
- Input validation  
- Stateful agent behavior  
- Modular design  
- Separation of concerns  
- Test coverage  
- Clear extensibility points  

---

## Extending the project (intentional design)

This architecture supports easy extension to:

- Replace planner with LLM-based planner
- Add structured tool calling
- Persist bookings in Postgres
- Store memory in Chroma / Pinecone
- Add authentication
- Add UI (Streamlit / React)
- Deploy to AWS / Fly.io / Railway
- Add OpenTelemetry tracing
- Add evaluation harness

The current design anticipates growth without major refactoring.

---

## Why this project exists

This project was built to demonstrate:
> "I understand how to design and build real agentic systems — not just run tutorials."

It reflects:
- Backend engineering skills  
- Architecture design  
- Product thinking  
- Clean code practices  
- Real-world system behavior  

---

## License

None — free to use, modify, and extend.

---

If you found this useful, feel free to ⭐ the repo.
