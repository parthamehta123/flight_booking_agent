from app.agent.nodes.llm_planner import llm_extract_slots
from app.agent.nodes.regex_planner import extract_slots


def planner(state: dict, text: str):
    # Try LLM first
    llm_result = llm_extract_slots(text)
    if llm_result:
        state.update(llm_result)
    else:
        # Fallback to deterministic regex planner
        state = extract_slots(text, state)

    for slot in ["origin", "destination", "date"]:
        if slot not in state:
            return {"action": "ask", "slot": slot}

    return {"action": "execute"}
