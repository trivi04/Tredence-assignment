from app.core.registry import NODE_REGISTRY

SUMMARY_LIMIT = 120

def split_text(state, tools):
    text = state.get("text", "")
    chunks = [text[i:i+100] for i in range(0, len(text), 100)]
    state["chunks"] = chunks
    return state

def generate_summaries(state, tools):
    summaries = [chunk[:50] for chunk in state["chunks"]]
    state["summaries"] = summaries
    return state

def merge_summaries(state, tools):
    merged = " ".join(state["summaries"])
    state["merged_summary"] = merged
    return state

def refine_summary(state, tools):
    summary = state["merged_summary"]
    refined = summary[: int(len(summary) * 0.7)]
    state["final_summary"] = refined

    if len(refined) > SUMMARY_LIMIT:
        state["_next"] = "generate_summaries"
    else:
        state["_terminate"] = True

    return state

NODE_REGISTRY["split"] = split_text
NODE_REGISTRY["generate_summaries"] = generate_summaries
NODE_REGISTRY["merge"] = merge_summaries
NODE_REGISTRY["refine"] = refine_summary