import asyncio
import argparse
import sys
from enhanced_analyzer import main as enhanced_main, AnalysisType, EnhancedSystemAnalyzerApp


def parse_arguments():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Enhanced Architecture Analyzer - Analyze system architectures using LLMs"
    )
    parser.add_argument(
        '--analysis-type',
        type=str,
        choices=['basic', 'failure', 'performance', 'integration', 'comparative', 'comprehensive'],
        default='comprehensive',
        help='Type of analysis to perform (default: comprehensive)'
    )
    return parser.parse_args()


async def run_custom_analysis(analysis_type: AnalysisType):
    """Run analysis with specified type"""
    from enhanced_analyzer import EnhancedSystemAnalyzerApp
    
    app = EnhancedSystemAnalyzerApp()
    await app.run(analysis_type)


def main():
    """Entry point for the application"""
    args = parse_arguments()
    
    # Map string to AnalysisType enum
    analysis_type_map = {
        'basic': AnalysisType.BASIC,
        'failure': AnalysisType.FAILURE,
        'performance': AnalysisType.PERFORMANCE,
        'integration': AnalysisType.INTEGRATION,
        'comparative': AnalysisType.COMPARATIVE,
        'comprehensive': AnalysisType.COMPREHENSIVE
    }
    
    analysis_type = analysis_type_map[args.analysis_type]
    
    # Run the appropriate analysis
    try:
        if analysis_type == AnalysisType.COMPREHENSIVE:
            # Use the default main function from enhanced_analyzer
            asyncio.run(enhanced_main())
        else:
            # Run custom analysis type
            asyncio.run(run_custom_analysis(analysis_type))
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
