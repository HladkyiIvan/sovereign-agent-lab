"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All three conditions were correct on the 70B model with clean baseline data. Interestingly,
PLAIN returned "The Haymarket Vaults" while XML and SANDWICH both returned "The Albanach" —
both are valid answers satisfying all constraints. The XML and SANDWICH formats appear to
trigger primacy bias, surfacing The Albanach (listed first) rather than scanning the full list.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is the more dangerous distractor. It satisfies both the capacity (160) and
vegan requirements, failing only on status=full — the least salient constraint. A model
skimming rather than evaluating all three criteria simultaneously would likely select it,
since two out of three attributes match perfectly.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C ran because both A and B were all-correct on the 70B model. The 8B model also answered
all three conditions correctly, returning "The Haymarket Vaults" consistently across PLAIN, XML,
and SANDWICH. This is a surprisingly robust result — the dataset's signal-to-noise ratio may
still be high enough that even the smaller model handles it without structural formatting help.
The experiment did not surface a formatting-dependent failure on either model with this dataset.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the signal-to-noise ratio is low — that is, when there
are many plausible-looking distractors, the correct answer is buried in the middle of a long
context, or the model is smaller and has less capacity for careful multi-constraint reasoning.
On clean, short datasets with strong frontier models, structural cues like XML tags and query
sandwiching provide marginal benefit; their value emerges under degraded conditions where
attention must be guided explicitly to the right information.
"""
