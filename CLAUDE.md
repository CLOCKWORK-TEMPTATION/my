# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Enhanced Architecture Analyzer - a full-stack application using LLMs (primarily OpenAI) to analyze system architecture descriptions. Available as CLI tool, REST API, or web interface.

**Primary language for outputs**: Arabic (prompts, UI labels, and analysis outputs)

## Build & Run Commands

```bash
# CLI - Run analyzer directly (reads Session details.txt, outputs System_Architecture_Analysis.md)
uv run main.py --analysis-type comprehensive
uv run main.py --analysis-type basic|failure|performance|integration|comparative

# Backend - Start FastAPI server (port 8000)
cd backend && uvicorn main:app --reload

# Frontend - Start Vite dev server (port 5173)
cd frontend && npm run dev
cd frontend && npm run build   # Production build
cd frontend && npm run lint    # ESLint

# Python dependencies
uv add <package>
```

## Environment Setup

Requires `OPENAI_API_KEY` in `.env`:
```bash
echo "OPENAI_API_KEY=sk-proj-..." > .env
```

## Architecture

**Full-Stack Components:**
- `enhanced_analyzer.py` (~815 lines) - Core analysis engine (Pydantic models, LLM agent, formatters)
- `main.py` - CLI entry point with argparse
- `backend/main.py` - FastAPI REST API wrapping the analyzer
- `frontend/` - React 19 + TypeScript + Vite + Tailwind CSS + shadcn/ui

**Core Classes in enhanced_analyzer.py:**
- `EnhancedArchitecturalAnalystAgent` - LLM interactions via `instructor` for structured outputs
- `ConfigManager` - Environment-based config loading
- `AsyncFileHandler` - Non-blocking file I/O with `aiofiles`
- 13 Pydantic models for typed LLM responses (`SystemComponent`, `FailureAnalysisResult`, `ComprehensiveArchitectureReport`, etc.)

**API Endpoints:**
- `POST /api/analyze` - Analyze text input
- `POST /api/analyze-file` - Analyze uploaded file
- `GET /api/analysis-types` - List available analyses

## Analysis Types

Six modes via `AnalysisType` enum: `BASIC`, `FAILURE`, `PERFORMANCE`, `INTEGRATION`, `COMPARATIVE`, `COMPREHENSIVE`

## Conventions

- **Structured LLM Output**: Always use `instructor` with Pydantic models
- **Async/Await**: All I/O is async (`asyncio`, `aiofiles`, `AsyncOpenAI`)
- **Rich UI**: Use `rich.console` for CLI output
- **Arabic**: Maintain Arabic localization in all user-facing text
- **Frontend**: shadcn/ui components, RTL layout (`dir="rtl"`)
