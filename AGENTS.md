# AGENTS Rules for Go Projects with Generative AI

## 1. Project Context & "Big Picture"
This project implements an **Enhanced Architecture Analyzer** in Go, porting functionality from an existing Python prototype. It leverages the **Google Generative AI SDK (`google.golang.org/genai`)** and supports a multi-provider strategy to perform multi-layer architectural analysis.

**Major Components:**
* **Client Initialization:** `genai.NewClient` with API key handling (via `godotenv`).
* **Generative Models Strategy (Jan 2026 Standards):**
    * **Primary Core (Google):** Uses **`gemini-3-pro`** (Nov 2025) for high-fidelity architectural parsing and standard reporting.
    * **Deep Reasoning:** Uses **`gemini-3-deep-think`** (Dec 2025) specifically for the `FailureAnalysisResult` pipeline to detect complex edge cases.
    * **High-Speed/Chat:** Uses **`gemini-3-flash`** for interactive CLI chat and quick summaries.
    * **External/Comparative Options:**
        * *OpenAI:* **`gpt-5.2`** (and `gpt-5.2-codex` for code-specific tasks).
        * *Anthropic:* **`claude-4-5-sonnet`** (Enterprise standard).
    * **Local/Offline Support:** Provisions for **`llama-4-scout`** or **`deepseek-v3.2`** via local inference servers if privacy is strictly required.
* **Data Models (Target):** Structured structs for `ArchitectureResult`, `FailureAnalysisResult`, `IntegrationReport`, etc., mirroring the Python `pydantic` models.
* **Analysis Workflow:** A pipeline approach where raw text is fed into specific prompt templates to generate structured insights.
* **CLI Output:** Uses `github.com/pterm/pterm` for rich terminal output.

**Data Flow:**
Input File (`Session_details.txt`) -> Go Structs -> Selected Model API (e.g., Gemini 3 Pro) -> JSON/Structured Response -> Formatted Markdown Report (`System_Architecture_Analysis.md`).

## 2. Essential Developer Workflows
* **Dependency Management:**
    * Add new deps: `go get <package-path>` (e.g., `go get google.golang.org/genai`).
    * Sync deps: `go mod tidy`.
* **Running the App:**
    * `go run main.go`
* **Environment Setup:**
    * Create a `.env` file in the root.
    * **CRITICAL (Google):** `GEMINI_API_KEY=your_key_here` (Access to Gemini 3 family).
    * **OPTIONAL (Competitors):**
        * `OPENAI_API_KEY` (for GPT-5.2 access).
        * `ANTHROPIC_API_KEY` (for Claude 4.5 access).
        * `DEEPSEEK_API_KEY` (for DeepSeek V3.2/R1 access).
* **Testing:**
    * Run tests: `go test ./...`
    * Use table-driven tests to benchmark `gemini-3-pro` vs `gemini-3-deep-think` for result accuracy.

## 3. Project-Specific Patterns & Conventions
* **Prompt Engineering:**
    * **Structure:** Prompts should be defined as constants, separating "System" instructions from "User" content.
    * **Model Routing:** explicitly define which prompt requires the **Reasoning** capabilities of models like `o3` or `gemini-3-deep-think`.
    * **Multimodal:** When using images, use `genai.ImageData` combined with `genai.Text`.
    * **Chat vs. Generate:** Use `GenerateContent` for single-pass analysis. Use `StartChat` only for interactive refinements using the faster `gemini-3-flash`.
* **Structured Output (Go equivalent of Pydantic):**
    * **Go Strategy:** Since the Go SDK doesn't natively support "response_model" like Instructor-Python yet, prompts must explicitly request **JSON output** matching the Go structs.
    * *Example pattern:* Append "Respond with valid JSON matching this schema: ..." to the prompt.
* **Error Handling:**
    * Wrap API calls in standard `if err != nil` blocks.
    * Use `log.Fatal` for startup failures.
    * Use `pterm.Error` for runtime processing errors.

## 4. Integration Points & Key Files
* **`main.go`**: Entry point. Needs to implement the `ModelSelector` logic to choose between `gemini-3-pro` and other variants based on flags.
* **`enhanced_analyzer.py`**: **Reference Implementation.**
* **`go.mod`**: Lists current dependencies (`google.golang.org/genai`, `github.com/joho/godotenv`, `github.com/pterm/pterm`).

## 5. Migration Strategy (Python -> Go)
* **Models:** Convert Python `pydantic.BaseModel` to Go `struct`s with JSON tags.
* **Analysis Logic:** Port `EnhancedArchitecturalAnalystAgent` methods to Go functions.
* **CLI:** Replace `rich` calls with `pterm` equivalents.