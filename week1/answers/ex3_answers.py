"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                                                        
I am afraid, I don't know the answer. At this point, I don't have access to a knowledge base.
Would you like to continue with confirm booking?
Your input ->  Yes, I have 160 guests                                                                              
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                                 
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                                                        
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking, I have 160 guests, 50 need vegan                                      
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500                                                                                                
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "Deposit exceeds authorised limit"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking, I have 160 guests, 50 need vegan                                      
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  Do you have parking on spot or nearby?                                                              
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM acknowledged it could not handle the parking question, stated its scope explicitly,
and then offered to resume the interrupted confirm_booking flow — keeping the dialogue
state intact rather than abandoning the in-progress booking.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
LangGraph returned a confused non-answer ("Your input is lacking necessary details") —
it did not call any tools but also did not explain why it couldn't help or offer to resume
the prior task. Rasa CALM, by contrast, gave a clear scope boundary ("I'm not trained
to help with that"), explained what it CAN do, and explicitly offered to return to the
booking flow. CALM's structured flows make out-of-scope handling a first-class design
concern; LangGraph leaves it entirely to the LLM's discretion, producing less predictable
behaviour.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
Ran rasa shell and asked the agent about an event date beyond its training cutoff.
Verified it responded with the cutoff guard message rather than fabricating event details.
Also tested a date within scope to confirm normal flow was unaffected.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
CALM gains: the LLM now handles intent classification, slot extraction from natural
language ("about 50 need vegan" → 50.0), and deciding which flow to trigger — tasks
that previously required NLU training data, regex validators, and explicit rules.yml paths.
Python (ActionValidateBooking) still enforces the deposit cap because business rules must
be deterministic and auditable; you cannot trust an LLM to reliably apply a £300 hard limit.
What the old approach offered that CALM doesn't: every dialogue path was explicit and
testable. With CALM, the LLM can take conversational detours that are hard to anticipate
in unit tests, and a model update could silently change extraction behaviour.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The setup cost (config.yml, domain.yml, flows.yml, endpoints.yml, rasa train, Rasa Pro licence)
bought strict containment: the CALM agent cannot improvise a response outside its defined flows,
and it cannot call a tool that isn't declared in flows.yml. LangGraph can freely call any tool
at any step and compose multi-tool chains on the fly. For a booking confirmation assistant that
must never hallucinate venue details or invent a price, the CALM constraint is a feature —
predictability and auditability matter more than flexibility. For a general-purpose assistant,
the same rigidity would be a serious limitation.
"""
