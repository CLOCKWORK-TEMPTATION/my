# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Enhanced Architecture Analyzer - an async Python CLI application that uses LLMs (OpenAI, Anthropic, Google, DeepSeek) to analyze system architecture descriptions. Reads from `Session details.txt`, outputs to `System_Architecture_Analysis.md`.

**Primary language**: Arabic (code comments, prompts, and outputs)

## Build & Run Commands

```bash
# Run the analyzer (preferred method with uv)
uv run enhanced_analyzer.py

# Alternative: traditional Python
python enhanced_analyzer.py

# Install dependencies with uv
uv add <package_name>

# Run tests
python -m pytest tests/ -v
```

## Environment Setup

Requires `OPENAI_API_KEY` in `.env` file (or `.env.local`):
```bash
echo "OPENAI_API_KEY=sk-proj-..." > .env
```

## Architecture

The codebase is a monolith in `enhanced_analyzer.py` (~815 lines):

- **Data Models**: Pydantic models for structured LLM outputs (`SystemComponent`, `FailureAnalysisResult`, `ComprehensiveArchitectureReport`, etc.)
- **Agent**: `EnhancedArchitecturalAnalystAgent` - manages LLM interactions via `instructor` for structured responses
- **Config**: `ConfigManager` loads settings from environment variables
- **File I/O**: `AsyncFileHandler` uses `aiofiles` for non-blocking operations
- **UI**: `rich` library for console output

**Data Flow**:
1. Read raw text from `Session details.txt`
2. Send to LLM via `EnhancedArchitecturalAnalystAgent`
3. Format structured results to Markdown
4. Write to `System_Architecture_Analysis.md`

## Analysis Types

Six analysis modes available via `AnalysisType` enum:
- `BASIC` - core components, data flows, innovations
- `FAILURE` - vulnerabilities, single points of failure, recovery plans
- `PERFORMANCE` - scalability, throughput, latency
- `INTEGRATION` - tech stack compatibility, API compatibility, migration paths
- `COMPARATIVE` - compare two systems
- `COMPREHENSIVE` - full report combining all above

## Conventions

- **Structured LLM Output**: Always use `instructor` with Pydantic models for LLM calls
- **Async/Await**: All I/O is async (`asyncio`, `aiofiles`, `AsyncOpenAI`)
- **Rich UI**: Use `rich.console` for output, not `print()`
- **Arabic**: Maintain Arabic localization in prompts and outputs
