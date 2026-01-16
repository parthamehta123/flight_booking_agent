# Architecture

This project uses a Graph-based agent:
Planner → Executor → Verifier

- Planner: parses natural language robustly
- Executor: calls tools
- Verifier: validates output
- AgentGraph: orchestrates stateful conversation

Designed to demonstrate production-style agent architecture.

Tools are decoupled from orchestration.
Memory and DB layers are clean abstractions.