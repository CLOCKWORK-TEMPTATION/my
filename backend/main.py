"""
FastAPI Backend for Architecture Analyzer
Provides REST API endpoints for architectural analysis using LLMs
"""

import os
import sys
import logging
from typing import Optional
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Add parent directory to path to import enhanced_analyzer
sys.path.append(str(Path(__file__).parent.parent))

from enhanced_analyzer import (
    EnhancedArchitecturalAnalystAgent,
    AppConfig,
    AnalysisType,
    ComprehensiveArchitectureReport
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Architecture Analyzer API",
    description="REST API for analyzing system architectures using advanced LLMs",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class AnalysisRequest(BaseModel):
    text: str = Field(..., description="Architecture session text to analyze")
    analysis_type: str = Field(
        default="comprehensive",
        description="Type of analysis: basic, failure, performance, integration, comparative, comprehensive"
    )
    model_name: Optional[str] = Field(
        default="gpt-4",
        description="LLM model to use for analysis"
    )

class AnalysisResponse(BaseModel):
    success: bool
    analysis_type: str
    report: str
    generated_at: str
    message: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: str

# Initialize analyzer agent
def get_config() -> AppConfig:
    """Get configuration for the analyzer"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    
    return AppConfig(
        api_key=api_key,
        input_file="",  # Not used in API mode
        output_file="",  # Not used in API mode
        model_name="gpt-4",
        temperature=0.2
    )

# API Endpoints
@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        timestamp=datetime.now().isoformat()
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        timestamp=datetime.now().isoformat()
    )

@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_architecture(request: AnalysisRequest):
    """
    Analyze architecture from text input
    
    Args:
        request: Analysis request containing text and configuration
        
    Returns:
        AnalysisResponse with the generated report
    """
    try:
        logger.info(f"Received analysis request - Type: {request.analysis_type}")
        
        # Validate analysis type
        try:
            analysis_type = AnalysisType(request.analysis_type.lower())
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid analysis type. Must be one of: {[t.value for t in AnalysisType]}"
            )
        
        # Create config
        config = get_config()
        config.model_name = request.model_name or "gpt-4"
        
        # Create agent
        agent = EnhancedArchitecturalAnalystAgent(config)
        
        # Perform analysis based on type
        if analysis_type == AnalysisType.COMPREHENSIVE:
            report = await agent.generate_comprehensive_report(request.text)
            content = agent.format_comprehensive_report(report)
        elif analysis_type == AnalysisType.BASIC:
            analysis = await agent.analyze(request.text)
            content = agent._format_basic_analysis(analysis)
        elif analysis_type == AnalysisType.FAILURE:
            analysis = await agent.analyze_failure_points(request.text)
            content = agent._format_failure_analysis(analysis)
        elif analysis_type == AnalysisType.PERFORMANCE:
            analysis = await agent.analyze_performance(request.text)
            content = agent._format_performance_analysis(analysis)
        elif analysis_type == AnalysisType.INTEGRATION:
            analysis = await agent.analyze_integration(request.text)
            content = agent._format_integration_analysis(analysis)
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported analysis type: {analysis_type.value}")
        
        logger.info(f"Analysis completed successfully - Type: {request.analysis_type}")
        
        return AnalysisResponse(
            success=True,
            analysis_type=request.analysis_type,
            report=content,
            generated_at=datetime.now().isoformat(),
            message="Analysis completed successfully"
        )
        
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Configuration error: {str(e)}")
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/api/analyze-file", response_model=AnalysisResponse)
async def analyze_from_file(
    file: UploadFile = File(...),
    analysis_type: str = "comprehensive",
    model_name: Optional[str] = "gpt-4"
):
    """
    Analyze architecture from uploaded file
    
    Args:
        file: Uploaded text file containing architecture session
        analysis_type: Type of analysis to perform
        model_name: LLM model to use
        
    Returns:
        AnalysisResponse with the generated report
    """
    try:
        logger.info(f"Received file upload - Filename: {file.filename}")
        
        # Read file content
        content = await file.read()
        text = content.decode('utf-8')
        
        # Create analysis request
        request = AnalysisRequest(
            text=text,
            analysis_type=analysis_type,
            model_name=model_name
        )
        
        # Delegate to analyze endpoint
        return await analyze_architecture(request)
        
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File must be UTF-8 encoded text")
    except Exception as e:
        logger.error(f"File upload error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")

@app.get("/api/analysis-types")
async def get_analysis_types():
    """Get available analysis types"""
    return {
        "types": [
            {
                "value": "comprehensive",
                "label": "تحليل شامل (Comprehensive)",
                "description": "تحليل معماري كامل متعدد الطبقات"
            },
            {
                "value": "basic",
                "label": "تحليل أساسي (Basic)",
                "description": "تحليل المكونات وتدفقات البيانات الأساسية"
            },
            {
                "value": "failure",
                "label": "تحليل نقاط الفشل (Failure Analysis)",
                "description": "تحديد المخاطر ونقاط الفشل المحتملة"
            },
            {
                "value": "performance",
                "label": "تحليل الأداء (Performance)",
                "description": "تقييم الأداء والتوسعية"
            },
            {
                "value": "integration",
                "label": "تحليل التكامل (Integration)",
                "description": "تحليل التوافقية والتكامل التقني"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)