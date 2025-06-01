# AI-CALC

**Overview:**
This project reimagines the traditional calculator by combining symbolic computation with generative reasoning. It blends deterministic math APIs (WolframAlpha) with LLM-based interpretation (Gemini), creating a smart calculator that not only solves but also explains and contextualizes mathematical expressions.

**Key Features:**

- Hybrid Intelligence: Uses WolframAlpha for accurate symbolic computation; routes the result to a generative model (Gemini) to generate step-by-step reasoning or context-aware suggestions.
- LLM-Augmented Clarity: When enabled, the app rewrites results in human-like explanations—useful for learners or when interpreting ambiguous queries.
- Streamlit UI: Clean and intuitive interface for inputting math expressions, toggling LLM explanations, and viewing visual outputs or symbolic interpretations.


**Technical Stack:**

- Frontend/UI and Deployment: Streamlit
- APIs Used: WolframAlpha SDK, Gemini API
- Architecture: Asynchronous dual-agent pipeline — one deterministic, one generative


Why It Matters:
Unlike calculators limited to raw computation, this AI-powered version understands why a solution matters—bridging the gap between solving and reasoning. It's ideal for educational use, technical assistants, or even chatbot integration.

