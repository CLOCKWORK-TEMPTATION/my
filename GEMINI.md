# GEMINI.md - Enhanced Architecture Analyzer

## Project Overview

This project is an "Enhanced Architecture Analyzer," a sophisticated Python application that leverages OpenAI's GPT models to perform in-depth analysis of system architecture descriptions. The primary input is a text file named `Session details.txt`, which contains a detailed description of a system's architecture, goals, and components. The application processes this input to generate a comprehensive analysis report in Markdown format, saved as `System_Architecture_Analysis.md`.

The application is built with a modern, asynchronous Python stack, utilizing:
- **`openai` & `instructor`**: To interface with OpenAI's language models and receive structured, validated responses.
- **`pydantic`**: For robust data modeling of the architectural components and analysis results.
- **`asyncio` & `aiofiles`**: For high-performance, non-blocking file I/O and concurrent API calls.
- **`python-dotenv`**: To manage environment variables, specifically the OpenAI API key.
- **`rich`**: For creating a visually appealing and highly readable command-line interface.

The analyzer can perform various types of analysis, including:
- **Basic Analysis**: Core components, data flows, and key innovations.
- **Failure Point Analysis**: Identifies critical vulnerabilities and single points of failure.
- **Integration Analysis**: Examines the tech stack, compatibility, and integration patterns.
- **Performance Analysis**: Assesses scalability, throughput, and latency.
- **Comprehensive Analysis**: A complete report combining all of the above.

A key convention of this project is that the codebase, including variable names, comments, and output, is written primarily in **Arabic**.

## Building and Running

To get the application running, follow these steps.

### 1. Setup Virtual Environment

It is recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 2. Install Dependencies

The project's dependencies are listed in the `requirements (2).txt` file. Install them using `pip`.

```bash
pip install -r "requirements (2).txt"
```

### 3. Configure Environment Variables

The application requires an OpenAI API key to function. Create a `.env` file in the project root and add your key.

```bash
# Create the .env file with your API key
echo "OPENAI_API_KEY=sk-proj-your-api-key-here" > .env
```
**Note:** Replace `sk-proj-your-api-key-here` with your actual OpenAI API key.

### 4. Run the Analyzer

The main entry point for the application is `enhanced_analyzer.py`. The script is configured to read `Session details.txt` and output `System_Architecture_Analysis.md` by default.

```bash
python enhanced_analyzer.py
```

Upon successful execution, a detailed markdown report will be generated in the root directory.

## Development Conventions

- **Language**: The primary language for code, comments, and user-facing output is **Arabic**. Any new contributions should adhere to this convention.
- **Data Modeling**: All data structures, especially for API responses, are strictly defined using `pydantic` models. This ensures type safety and data validation.
- **Asynchronous Code**: The application is built on `asyncio`. All I/O operations (file access, API calls) should be asynchronous to maintain performance.
- **CLI Output**: The `rich` library is used for all console output. This provides a consistent, high-quality user interface. New print statements or logging should use `rich` components like `Console`, `Panel`, and `Table`.
- **Configuration**: Application configuration is managed through the `AppConfig` dataclass and loaded via the `ConfigManager`. Avoid hardcoding values; add them to the configuration system instead.
