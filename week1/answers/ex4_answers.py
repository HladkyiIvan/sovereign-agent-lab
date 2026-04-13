"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

"""
NOTE from DK: Task was completed with changed code for the research agent (see exercise4_mcp_client_DKmodified)
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues","get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "It seems there are no Edinburgh venues currently available that can accommodate 300 people with vegan options. Would you like to adjust your search criteria (e.g., lower the capacity requirement or check for other dietary options)?"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
The only file that required modification was mcp_venue_server.py. After the change, Albanach was no longer returned as a candidate, leaving Haymarket as the sole result. The agent's output reflected this accordingly, which aligns with what we anticipated.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 28   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP establishes a standardised communication layer between agents and tools. Any agent can discover and invoke available tools without prior knowledge of their implementation, and tool updates on the server side take effect without touching client code.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
* The overall system belongs to the OpenClaw Automator category. Per the specification, it autonomously forms a plan, invokes tools, persists results to memory, and delivers a structured summary upon completion.
* At its base sits a set of Python-implemented data-interaction tools, which serve as the primary means through which the agent acts on its environment.
* A second tier of tools extends this foundation with live web search and file read/write capabilities, enabling the agent to gather and record real-world information.
* A critical design element is the separation between a deliberate "planner" sub-agent and a fast "executor" sub-agent; the two operate in tandem so reasoning stays decoupled from action.
* Finally, heartbeat-based scheduling keeps the agent running continuously while guarding against excessive token consumption and runaway error loops.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
Research should be handled by the OpenClaw Automator, and the live call by the Rasa Digital Employee. This split is supported directly by what we observed: the Automator ventured beyond the provided data to surface creative options (e.g. the transportation suggestions in Ex2), whereas the Digital Employee stayed tightly within its defined flows and resisted attempts to go off-script (as seen in Ex3). Reversing the assignment would yield a researcher too constrained to explore edge cases and a caller too unchecked to guarantee safe, human-verified decisions.
"""