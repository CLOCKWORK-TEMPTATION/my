# AGENTS # AI Coding Agent Guidelines for Architecture Analyzer

This document provides essential context and instructions for AI agents working on the Architecture Analyzer project.

## 🏗️ Architecture & Core Components

This is a Python-based asynchronous CLI application designed to analyze system architectures using state-of-the-art LLMs (Multi-Provider Support).

* **Entry Point:** `main.py` (simple wrapper) and `enhanced_analyzer.py` (core logic).
* **Core Logic (`enhanced_analyzer.py`):**
    * **Data Models:** Heavy use of `pydantic.BaseModel` for structured LLM outputs (e.g., `SystemComponent`, `FailureAnalysisResult`, `ComprehensiveArchitectureReport`).
    * **Agent:** `EnhancedArchitecturalAnalystAgent` manages interactions with multiple AI providers (OpenAI, Anthropic, Google, DeepSeek) using `instructor` for structured responses.
    * **Configuration:** `ConfigManager` loads settings from environment variables (`.env`, `.env.local`) and handles API keys for various providers.
    * **File I/O:** `AsyncFileHandler` uses `aiofiles` for non-blocking read/write operations.
    * **UI/Logging:** `rich` library is used for console output and logging.

**Data Flow:**
1.  Read raw text input (default: `Session details.txt`).
2.  Send to LLM via `EnhancedArchitecturalAnalystAgent`.
    * *Dynamic Model Routing:* Selects the appropriate model (e.g., `gpt-5.2` vs `claude-4.5-sonnet`) based on the complexity of the requested analysis.
3.  Format structured results into Markdown.
4.  Write output to file (default: `System_Architecture_Analysis.md`).

## 🤖 Recommended Model Configurations (Jan 2026 Standards)

To ensure optimal analysis quality, the system supports the following model tiers. Agents should default to the **Stable High-Performance** tier unless specified otherwise.

| Task Type | Recommended Model | Provider | Use Case |
| :--- | :--- | :--- | :--- |
| **Complex Logic / Architecture** | **GPT-5.2** | OpenAI | Primary model for deep architectural synthesis and pattern recognition. |
| **Reasoning / Root Cause** | **o3 / o3-mini** | OpenAI | Best for complex failure analysis and chain-of-thought deduction. |
| **Reasoning (Alternative)** | **Gemini 3 Deep Think** | Google | Excellent alternative for deep reasoning tasks. |
| **Context / Creative Analysis** | **Claude 4.5 Opus** | Anthropic | Superior for nuanced qualitative analysis and long-context sessions. |
| **High Speed / Efficiency** | **Claude 4.5 Sonnet** | Anthropic | Best balance of speed and intelligence for routine checks. |
| **Low Latency** | **Gemini 3 Flash** | Google | For rapid, iterative feedback loops. |
| **Open Weight / Cost-Effective** | **Llama 4 Scout** | Meta | For local testing or budget-constrained environments. |

## 🛠️ Developer Workflow

* **Environment:** Python >= 3.11 using `uv` for dependency management.
* **Running the Analysis:**
    ```bash
    uv run enhanced_analyzer.py
    ```
    *Note: Ensure relevant API keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`) are set in the environment.*
* **Dependencies:** Managed via `pyproject.toml`.
    * Add new deps: `uv add <package_name>`
* **Input Data:** The analyzer expects input text in `Session details.txt`. Ensure this file exists and contains the architectural session logs to be analyzed.

## 🧩 Patterns & Conventions

* **Structured LLM Output:** ALWAYS use `instructor` with `pydantic` models for LLM interactions, regardless of the provider.
    ```python
    # Example Pattern with Dynamic Model Selection
    result = await self.client.chat.completions.create(
        model=self.config.get_model_for_task("reasoning"), # e.g., returns "o3-mini"
        response_model=YourPydanticModel, 
        messages=[...]
    )
    ```
* **Async/Await:** The entire I/O and network layer is asynchronous (`asyncio`, `aiofiles`, `AsyncOpenAI/AsyncAnthropic`). Maintain this pattern for all I/O-bound tasks.
* **Rich UI:** Use `rich.console` and `rich.logging` for user feedback. Do not use standard `print()`.
* **Arabic Language:** The system prompts and outputs are primarily in **Arabic**. Ensure new prompts or output formats maintain this localization.
* **Error Handling:** Use `try/except` blocks with specific error logging. Handle provider-specific errors (e.g., rate limits on `o3-mini` or context window errors).

## 🔑 Key Files

* `enhanced_analyzer.py`: **Monolith file** containing models, logic, and UI.
* `Session details.txt`: Default input source.
* `System_Architecture_Analysis.md`: Default output destination.

## 🚀 Immediate Next Actions for Agents

* Update `ConfigManager` to support `GPT-5.2`, `Gemini 3`, and `Claude 4.5` configurations.
* Implement a **Model Selector** logic in `EnhancedArchitecturalAnalystAgent` to switch between `o3-mini` (for failure analysis) and `gpt-5.2` (for general reporting).
* Ensure `pydantic` models are robust enough to handle the increased nuance and detail provided by these 2026-era models.