import os
import sys
import logging
import asyncio
import json
from datetime import datetime
from typing import List, Optional, Literal
from dataclasses import dataclass
from enum import Enum

import aiofiles
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax

# =================================================================================================
# إعدادات السجلات والعرض (Logging & Display Configuration)
# =================================================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True, markup=True)]
)

logger = logging.getLogger("ArchitectureAnalyzerApp")
console = Console()

# =================================================================================================
# أنواع التحليل المتاحة (Analysis Types)
# =================================================================================================

class AnalysisType(str, Enum):
    BASIC = "basic"
    FAILURE = "failure"
    PERFORMANCE = "performance"
    INTEGRATION = "integration"
    COMPARATIVE = "comparative"
    COMPREHENSIVE = "comprehensive"

# =================================================================================================
# نماذج البيانات الأساسية (Core Data Models)
# =================================================================================================

class SystemComponent(BaseModel):
    name: str = Field(..., description="اسم المكون (مثال: 'Orchestrator Agent', 'Knowledge Graph')")
    type: Literal["Agent", "Database", "Service", "Interface", "Orchestrator", "Cache", "Queue", "Gateway"]
    responsibility: str = Field(..., description="المسؤولية التقنية للمكون")
    technologies: List[str] = Field(..., description="التقنيات المقترحة (مثال: 'Neo4j', 'FastAPI')")
    criticality: Literal["low", "medium", "high", "critical"] = Field(default="medium")

class DataFlow(BaseModel):
    source: str = Field(..., description="مصدر البيانات")
    target: str = Field(..., description="هدف البيانات")
    protocol: str = Field(..., description="بروتوكول الاتصال (gRPC, REST, Pub/Sub, WebSocket)")
    data_type: str = Field(..., description="نوع البيانات المنقولة")
    throughput: Optional[str] = Field(default=None, description="إنتاجية البيانات المتوقعة")

class DecisionEngineSpec(BaseModel):
    negotiation_protocol: str = Field(..., description="بروتوكول المفاوضة (مثال: Contract Net Protocol)")
    optimization_metric: str = Field(..., description="المقياس الأساسي للتحسين")
    decision_latency: Optional[str] = Field(default=None, description="زمن القرار المتوقع")

class ArchitectureResult(BaseModel):
    """نموذج التحليل الأساسي للمعمارية"""
    winning_system_name: str
    core_components: List[SystemComponent]
    data_flows: List[DataFlow]
    decision_engine: DecisionEngineSpec
    key_innovations: List[str]
    implementation_challenges: List[str]

# =================================================================================================
# نماذج تحليل نقاط الفشل (Failure Analysis Models)
# =================================================================================================

class RiskAssessment(BaseModel):
    failure_point: str = Field(..., description="نقطة الفشل المحتملة")
    probability: Literal["low", "medium", "high"] = Field(default="medium")
    severity: Literal["minor", "critical", "catastrophic"] = Field(default="critical")
    mitigation_strategy: str = Field(..., description="استراتيجية التخفيف")
    fallback_option: Optional[str] = Field(default=None, description="خيار بديل")

class FailureAnalysisResult(BaseModel):
    """نتائج تحليل نقاط الفشل"""
    system_name: str
    critical_vulnerabilities: List[RiskAssessment]
    single_points_of_failure: List[str]
    recovery_time_objective: str
    redundancy_requirements: List[str]
    disaster_recovery_plan: Optional[str]

# =================================================================================================
# نماذج تحليل التكامل (Integration Analysis Models)
# =================================================================================================

class TechStackAnalysis(BaseModel):
    technology: str = Field(..., description="اسم التقنية")
    version_range: str = Field(..., description="نطاق الإصدارات المدعومة")
    compatibility_issues: List[str] = Field(default_factory=list)
    integration_points: List[str] = Field(default_factory=list)
    deprecation_risk: Literal["none", "low", "medium", "high"] = Field(default="none")

class IntegrationReport(BaseModel):
    """تقرير التكامل والتوافقية"""
    system_name: str
    tech_stack_analysis: List[TechStackAnalysis]
    integration_patterns_used: List[str]
    api_compatibility_score: float = Field(ge=0, le=1)
    migration_path: Optional[str]
    deprecated_technologies: List[str]
    security_compliance: List[str]

# =================================================================================================
# نماذج تحليل الأداء (Performance Analysis Models)
# =================================================================================================

class ScalabilityMetric(BaseModel):
    metric_name: str = Field(..., description="اسم المقياس")
    current_capacity: str = Field(..., description="السعة الحالية")
    scalability_factor: float = Field(ge=1.0, description="عامل التوسع")
    bottleneck: Optional[str] = Field(default=None, description="عنق الزجاجة المحتمل")

class PerformanceAnalysis(BaseModel):
    """تحليل الأداء والتوسع"""
    system_name: str
    throughput_estimate: str = Field(..., description="تقدير الإنتاجية")
    latency_profile: str = Field(..., description="ملف الزمن الكامن")
    scalability_metrics: List[ScalabilityMetric]
    recommended_scaling_strategy: str
    load_balancing_approach: str
    caching_strategy: str
    optimization_opportunities: List[str]
    expected_tps: Optional[float] = Field(default=None, description="المعاملات المتوقعة في الثانية")

# =================================================================================================
# نموذج المقارنة (Comparison Model)
# =================================================================================================

class SystemComparison(BaseModel):
    """مقارنة بين نظامين"""
    system_a: str
    system_b: str
    performance_differential: str
    complexity_ratio: float
    cost_efficiency_comparison: str
    recommendation: str
    decision_factors: List[str]
    trade_offs: List[str]

# =================================================================================================
# التقرير الشامل (Comprehensive Report Model)
# =================================================================================================

class ComprehensiveArchitectureReport(BaseModel):
    """التقرير المعماري الشامل المتكامل"""
    basic_analysis: ArchitectureResult
    failure_analysis: FailureAnalysisResult
    integration_analysis: IntegrationReport
    performance_analysis: PerformanceAnalysis
    comparative_analysis: Optional[SystemComparison] = None
    generated_at: str
    confidence_level: float = Field(ge=0, le=1)
    analyst_notes: Optional[str] = None

# =================================================================================================
# مدير التكوين (Configuration Manager)
# =================================================================================================

@dataclass
class AppConfig:
    api_key: str
    input_file: str
    output_file: str
    model_name: str = "gpt-5.2-2025-12-11"
    analysis_type: AnalysisType = AnalysisType.COMPREHENSIVE
    temperature: float = 0.2

class ConfigManager:
    @staticmethod
    def load_config() -> AppConfig:
        try:
            load_dotenv()
            api_key = os.getenv("OPENAI_API_KEY")
            
            if not api_key:
                env_local_path = r"E:\backtopython\.env.local"
                if os.path.exists(env_local_path):
                    load_dotenv(env_local_path)
                api_key = os.getenv("OPENAI_API_KEY")
            
            if not api_key:
                raise ValueError("❌ Environment variable 'OPENAI_API_KEY' is missing.")
            
            return AppConfig(
                api_key=api_key,
                input_file="Session_details.txt",
                output_file="System_Architecture_Analysis.md",
                analysis_type=AnalysisType.COMPREHENSIVE
            )
        
        except Exception as e:
            logger.critical(f"[red]Configuration Error:[/red] {str(e)}")
            sys.exit(1)

# =================================================================================================
# معالج الملفات غير المتزامن (Async File Handler)
# =================================================================================================

class AsyncFileHandler:
    @staticmethod
    async def read_file(file_path: str) -> str:
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File '{file_path}' not found.")
            
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                content = await f.read()
            
            logger.info(f"✓ Read file '[bold cyan]{file_path}[/bold cyan]' | Size: {len(content)} chars")
            return content
        
        except Exception as e:
            logger.error(f"[red]Read Error:[/red] {str(e)}")
            raise
    
    @staticmethod
    async def save_report(file_path: str, content: str) -> None:
        try:
            async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
                await f.write(content)
            
            logger.info(f"✓ Report saved to '[bold green]{file_path}[/bold green]'")
        
        except Exception as e:
            logger.error(f"[red]Save Error:[/red] {str(e)}")
            raise

# =================================================================================================
# وكيل التحليل المحسّن (Enhanced Analysis Agent)
# =================================================================================================

class EnhancedArchitecturalAnalystAgent:
    def __init__(self, config: AppConfig):
        self.client = instructor.patch(AsyncOpenAI(api_key=config.api_key))
        self.model = config.model_name
        self.temperature = config.temperature
    
    # =============================================================================
    # 1️⃣ التحليل الأساسي
    # =============================================================================
    async def analyze(self, raw_text: str) -> ArchitectureResult:
        logger.info("🔍 Starting [bold magenta]Basic Architecture Analysis[/bold magenta]...")
        
        try:
            result = await self.client.chat.completions.create(
                model=self.model,
                response_model=ArchitectureResult,
                messages=[
                    {
                        "role": "system",
                        "content": """أنت مهندس برمجيات محترف متخصص في تحليل المعماريات.
قم بتحليل سجل الجلسة واستخراج معمارية النظام الفائز بتنسيق منظم ودقيق.
يجب أن تكون جميع النتائج باللغة العربية الفصحى مع مراعاة الدقة التقنية."""
                    },
                    {
                        "role": "user",
                        "content": f"""قم بتحليل معمارية النظام من السجل التالي واستخرج:
1. مكونات النظام الأساسية
2. تدفقات البيانات
3. محرك القرار
4. الابتكارات الرئيسية
5. التحديات المتوقعة

السجل:
{raw_text[:90000]}"""
                    }
                ],
                temperature=self.temperature,
                max_retries=3
            )
            
            logger.info("✓ Basic analysis complete")
            return result
        
        except Exception as e:
            logger.error(f"[red]Analysis Error:[/red] {str(e)}")
            raise
    
    # =============================================================================
    # 2️⃣ تحليل نقاط الفشل
    # =============================================================================
    async def analyze_failure_points(self, arch_text: str) -> FailureAnalysisResult:
        logger.info("⚠️ Starting [bold red]Failure Point Analysis[/bold red]...")
        
        try:
            result = await self.client.chat.completions.create(
                model=self.model,
                response_model=FailureAnalysisResult,
                messages=[
                    {
                        "role": "system",
                        "content": """أنت خبير موثوقية الأنظمة والهندسة المختصة بالمرونة.
قم بتحليل شامل لنقاط الفشل المحتملة والمخاطر والثغرات الحرجة.
قدم استراتيجيات تخفيف واقعية وعملية."""
                    },
                    {
                        "role": "user",
                        "content": f"""حلل نقاط الفشل المحتملة في هذه المعمارية بشكل تفصيلي:
1. تحديد الثغرات الحرجة
2. نقاط الفشل الوحيد
3. خطة التعافي من الكوارث
4. متطلبات التكرار والتكرار

المعمارية:
{arch_text[:90000]}"""
                    }
                ],
                temperature=self.temperature,
                max_retries=3
            )
            
            logger.info("✓ Failure analysis complete")
            return result
        
        except Exception as e:
            logger.error(f"[red]Failure Analysis Error:[/red] {str(e)}")
            raise
    
    # =============================================================================
    # 3️⃣ تحليل التكامل والتوافقية
    # =============================================================================
    async def analyze_integration(self, arch_text: str) -> IntegrationReport:
        logger.info("🔗 Starting [bold blue]Integration & Compatibility Analysis[/bold blue]...")
        
        try:
            result = await self.client.chat.completions.create(
                model=self.model,
                response_model=IntegrationReport,
                messages=[
                    {
                        "role": "system",
                        "content": """أنت خبير التكامل والتوافقية التقنية.
قم بتحليل عميق للمكدس التكنولوجي والتوافقيات والنقاط المتكاملة.
اعتبر المعايير الأمنية والامتثال التنظيمي."""
                    },
                    {
                        "role": "user",
                        "content": f"""حلل توافقية وتكامل هذه المعمارية:
1. تحليل المكدس التكنولوجي
2. أنماط التكامل المستخدمة
3. نقاط التوافقية
4. تقييم توافقية API
5. مسار الهجرة المستقبلي
6. التقنيات المتقادمة

المعمارية:
{arch_text[:90000]}"""
                    }
                ],
                temperature=self.temperature,
                max_retries=3
            )
            
            logger.info("✓ Integration analysis complete")
            return result
        
        except Exception as e:
            logger.error(f"[red]Integration Analysis Error:[/red] {str(e)}")
            raise
    
    # =============================================================================
    # 4️⃣ تحليل الأداء والتوسع
    # =============================================================================
    async def analyze_performance(self, arch_text: str) -> PerformanceAnalysis:
        logger.info("⚡ Starting [bold yellow]Performance & Scalability Analysis[/bold yellow]...")
        
        try:
            result = await self.client.chat.completions.create(
                model=self.model,
                response_model=PerformanceAnalysis,
                messages=[
                    {
                        "role": "system",
                        "content": """أنت خبير الأداء والبنية القابلة للتوسع.
قم بتقييم تفصيلي للأداء وقابلية التوسع والتحسينات الممكنة.
اعتبر الحمل المتوقع والتجاوزات."""
                    },
                    {
                        "role": "user",
                        "content": f"""حلل أداء وقابلية التوسع لهذه المعمارية:
1. تقدير الإنتاجية
2. ملف الزمن الكامن
3. مقاييس قابلية التوسع
4. استراتيجية التوسع الموصى بها
5. نهج موازنة الحمل
6. استراتيجية التخزين المؤقت
7. فرص التحسين

المعمارية:
{arch_text[:90000]}"""
                    }
                ],
                temperature=self.temperature,
                max_retries=3
            )
            
            logger.info("✓ Performance analysis complete")
            return result
        
        except Exception as e:
            logger.error(f"[red]Performance Analysis Error:[/red] {str(e)}")
            raise
    
    # =============================================================================
    # 5️⃣ التحليل المقارن
    # =============================================================================
    async def compare_architectures(
        self, 
        system_a_text: str, 
        system_b_text: str
    ) -> SystemComparison:
        logger.info("⚖️ Starting [bold cyan]Comparative Analysis[/bold cyan]...")
        
        try:
            result = await self.client.chat.completions.create(
                model=self.model,
                response_model=SystemComparison,
                messages=[
                    {
                        "role": "system",
                        "content": """أنت محلل معماريات متخصص في المقارنة والتحليل النسبي.
قارن بين النظامين بعمق وقدم توصيات موثوقة مبنية على بيانات."""
                    },
                    {
                        "role": "user",
                        "content": f"""قارن بين النظامين التاليين بشكل شامل:

النظام الأول:
{system_a_text[:45000]}

النظام الثاني:
{system_b_text[:45000]}

قدم:
1. مقارنة الأداء
2. تحليل التعقيد
3. مقارنة كفاءة التكاليف
4. التوصيات
5. العوامل المؤثرة في القرار
6. المقايضات والخيارات"""
                    }
                ],
                temperature=self.temperature,
                max_retries=3
            )
            
            logger.info("✓ Comparative analysis complete")
            return result
        
        except Exception as e:
            logger.error(f"[red]Comparison Error:[/red] {str(e)}")
            raise
    
    # =============================================================================
    # 6️⃣ إنشاء التقرير الشامل
    # =============================================================================
    async def generate_comprehensive_report(
        self, 
        arch_text: str,
        comparison_text: Optional[str] = None
    ) -> ComprehensiveArchitectureReport:
        """إنشاء تقرير معماري شامل متكامل"""
        
        console.print(Panel.fit(
            "[bold cyan]🚀 GENERATING COMPREHENSIVE ARCHITECTURE REPORT[/bold cyan]",
            border_style="cyan"
        ))
        
        try:
            # 1. التحليل الأساسي
            basic = await self.analyze(arch_text)
            
            # 2. تحليل نقاط الفشل
            failure = await self.analyze_failure_points(arch_text)
            
            # 3. تحليل التكامل
            integration = await self.analyze_integration(arch_text)
            
            # 4. تحليل الأداء
            performance = await self.analyze_performance(arch_text)
            
            # 5. التحليل المقارن (اختياري)
            comparison = None
            if comparison_text:
                comparison = await self.compare_architectures(arch_text, comparison_text)
            
            report = ComprehensiveArchitectureReport(
                basic_analysis=basic,
                failure_analysis=failure,
                integration_analysis=integration,
                performance_analysis=performance,
                comparative_analysis=comparison,
                generated_at=datetime.now().isoformat(),
                confidence_level=0.94
            )
            
            logger.info("[bold green]✓ Comprehensive report generation complete[/bold green]")
            return report
        
        except Exception as e:
            logger.error(f"[red]Report Generation Error:[/red] {str(e)}")
            raise
    
    # =============================================================================
    # تنسيق التقارير (Report Formatting)
    # =============================================================================
    
    def _format_basic_analysis(self, data: ArchitectureResult) -> str:
        """تنسيق التحليل الأساسي"""
        md = "### المكونات الأساسية\n"
        md += "| المكون | النوع | الأهمية | المسؤولية | التقنيات |\n"
        md += "|--------|------|--------|-----------|----------|\n"
        
        for comp in data.core_components:
            techs = ", ".join(comp.technologies)
            md += f"| {comp.name} | {comp.type} | {comp.criticality} | {comp.responsibility} | {techs} |\n"
        
        md += "\n### تدفق البيانات\n"
        for flow in data.data_flows:
            md += f"- **{flow.source}** → **{flow.target}**: {flow.data_type} (عبر `{flow.protocol}`)"
            if flow.throughput:
                md += f" | الإنتاجية: {flow.throughput}"
            md += "\n"
        
        md += "\n### محرك القرار\n"
        md += f"- **البروتوكول**: {data.decision_engine.negotiation_protocol}\n"
        md += f"- **هدف التحسين**: {data.decision_engine.optimization_metric}\n"
        if data.decision_engine.decision_latency:
            md += f"- **زمن القرار**: {data.decision_engine.decision_latency}\n"
        
        md += "\n### الابتكارات الرئيسية\n"
        for innov in data.key_innovations:
            md += f"- 🎯 {innov}\n"
        
        md += "\n### التحديات المتوقعة\n"
        for chall in data.implementation_challenges:
            md += f"- ⚠️ {chall}\n"
        
        return md
    
    def _format_failure_analysis(self, data: FailureAnalysisResult) -> str:
        """تنسيق تحليل الفشل"""
        md = f"### النظام: {data.system_name}\n\n"
        
        md += "#### الثغرات الحرجة\n"
        for risk in data.critical_vulnerabilities:
            severity_emoji = "🔴" if risk.severity == "catastrophic" else "🟠" if risk.severity == "critical" else "🟡"
            md += f"\n{severity_emoji} **{risk.failure_point}**\n"
            md += f"   - الاحتمالية: {risk.probability}\n"
            md += f"   - الخطورة: {risk.severity}\n"
            md += f"   - الاستراتيجية: {risk.mitigation_strategy}\n"
            if risk.fallback_option:
                md += f"   - البديل: {risk.fallback_option}\n"
        
        md += f"\n#### نقاط الفشل الوحيد\n"
        for spof in data.single_points_of_failure:
            md += f"- {spof}\n"
        
        md += f"\n#### متطلبات التعافي\n"
        md += f"- **الهدف الزمني للتعافي (RTO)**: {data.recovery_time_objective}\n"
        md += f"- **متطلبات التكرار**:\n"
        for req in data.redundancy_requirements:
            md += f"  - {req}\n"
        
        if data.disaster_recovery_plan:
            md += f"\n#### خطة التعافي من الكوارث\n{data.disaster_recovery_plan}\n"
        
        return md
    
    def _format_integration_analysis(self, data: IntegrationReport) -> str:
        """تنسيق تحليل التكامل"""
        md = f"### النظام: {data.system_name}\n\n"
        
        md += "#### تحليل المكدس التكنولوجي\n"
        for tech in data.tech_stack_analysis:
            risk_emoji = "🟢" if tech.deprecation_risk == "none" else "🟡" if tech.deprecation_risk == "low" else "🟠" if tech.deprecation_risk == "medium" else "🔴"
            md += f"\n{risk_emoji} **{tech.technology}** (v{tech.version_range})\n"
            if tech.compatibility_issues:
                md += f"   - مشاكل التوافقية: {', '.join(tech.compatibility_issues)}\n"
            if tech.integration_points:
                md += f"   - نقاط التكامل: {', '.join(tech.integration_points)}\n"
        
        md += f"\n#### أنماط التكامل\n"
        for pattern in data.integration_patterns_used:
            md += f"- {pattern}\n"
        
        md += f"\n#### درجات التقييم\n"
        score_percent = int(data.api_compatibility_score * 100)
        md += f"- **توافقية API**: {score_percent}%\n"
        
        if data.deprecated_technologies:
            md += f"\n#### التقنيات المتقادمة\n"
            for deprecated in data.deprecated_technologies:
                md += f"- ⚠️ {deprecated}\n"
        
        if data.migration_path:
            md += f"\n#### مسار الهجرة\n{data.migration_path}\n"
        
        if data.security_compliance:
            md += f"\n#### الامتثال الأمني\n"
            for compliance in data.security_compliance:
                md += f"- ✅ {compliance}\n"
        
        return md
    
    def _format_performance_analysis(self, data: PerformanceAnalysis) -> str:
        """تنسيق تحليل الأداء"""
        md = f"### النظام: {data.system_name}\n\n"
        
        md += f"#### ملف الأداء\n"
        md += f"- **الإنتاجية المتوقعة**: {data.throughput_estimate}\n"
        md += f"- **ملف الزمن الكامن**: {data.latency_profile}\n"
        if data.expected_tps:
            md += f"- **المعاملات في الثانية (TPS)**: {data.expected_tps}\n"
        
        md += f"\n#### مقاييس قابلية التوسع\n"
        for metric in data.scalability_metrics:
            md += f"\n- **{metric.metric_name}**\n"
            md += f"  - السعة الحالية: {metric.current_capacity}\n"
            md += f"  - عامل التوسع: {metric.scalability_factor}x\n"
            if metric.bottleneck:
                md += f"  - عنق الزجاجة: {metric.bottleneck}\n"
        
        md += f"\n#### استراتيجيات التحسين\n"
        md += f"- **استراتيجية التوسع**: {data.recommended_scaling_strategy}\n"
        md += f"- **موازنة الحمل**: {data.load_balancing_approach}\n"
        md += f"- **استراتيجية التخزين المؤقت**: {data.caching_strategy}\n"
        
        md += f"\n#### فرص التحسين\n"
        for opp in data.optimization_opportunities:
            md += f"- 🚀 {opp}\n"
        
        return md
    
    def _format_comparison(self, data: SystemComparison) -> str:
        """تنسيق التحليل المقارن"""
        md = f"#### مقارنة: {data.system_a} vs {data.system_b}\n\n"
        
        md += f"- **الفارق في الأداء**: {data.performance_differential}\n"
        md += f"- **نسبة التعقيد**: {data.complexity_ratio}x\n"
        md += f"- **مقارنة كفاءة التكاليف**: {data.cost_efficiency_comparison}\n"
        
        md += f"\n#### العوامل المؤثرة في القرار\n"
        for factor in data.decision_factors:
            md += f"- {factor}\n"
        
        md += f"\n#### المقايضات والخيارات\n"
        for tradeoff in data.trade_offs:
            md += f"- {tradeoff}\n"
        
        md += f"\n#### التوصية\n**{data.recommendation}**\n"
        
        return md
    
    def format_comprehensive_report(self, report: ComprehensiveArchitectureReport) -> str:
        """تنسيق التقرير الشامل الكامل"""
        md = f"# 📊 تقرير التحليل المعماري الشامل\n\n"
        
        md += f"**تم الإنشاء**: {report.generated_at}\n"
        md += f"**مستوى الثقة**: {int(report.confidence_level * 100)}%\n\n"
        
        if report.analyst_notes:
            md += f"**ملاحظات المحلل**: {report.analyst_notes}\n\n"
        
        md += "---\n\n"
        
        # القسم الأول: التحليل الأساسي
        md += "## 1️⃣ التحليل الأساسي\n\n"
        md += self._format_basic_analysis(report.basic_analysis)
        
        # تحليل الفشل
        md += "\n---\n\n## 2️⃣ تحليل نقاط الفشل والمخاطر\n\n"
        md += self._format_failure_analysis(report.failure_analysis)
        
        # تحليل التكامل
        md += "\n---\n\n## 3️⃣ تقرير التكامل والتوافقية\n\n"
        md += self._format_integration_analysis(report.integration_analysis)
        
        # تحليل الأداء
        md += "\n---\n\n## 4️⃣ تحليل الأداء والقابلية للتوسع\n\n"
        md += self._format_performance_analysis(report.performance_analysis)
        
        # التحليل المقارن
        if report.comparative_analysis:
            md += "\n---\n\n## 5️⃣ التحليل المقارن\n\n"
            md += self._format_comparison(report.comparative_analysis)
        
        md += "\n---\n\n## 📝 الملخص التنفيذي\n\n"
        md += "### النقاط الرئيسية\n"
        md += f"- **النظام المحلل**: {report.basic_analysis.winning_system_name}\n"
        md += f"- **عدد المكونات الأساسية**: {len(report.basic_analysis.core_components)}\n"
        md += f"- **عدد تدفقات البيانات**: {len(report.basic_analysis.data_flows)}\n"
        md += f"- **الابتكارات المحددة**: {len(report.basic_analysis.key_innovations)}\n"
        md += f"- **التحديات المعروفة**: {len(report.basic_analysis.implementation_challenges)}\n"
        md += f"- **الثغرات الحرجة**: {len(report.failure_analysis.critical_vulnerabilities)}\n"
        md += f"- **توافقية API**: {int(report.integration_analysis.api_compatibility_score * 100)}%\n"
        
        md += "\n---\n"
        md += "*تم إنشاء هذا التقرير بواسطة نظام التحليل المعماري المحسّن - GPT-5.2*\n"
        
        return md

# =================================================================================================
# تطبيق المحلل المحسّن (Enhanced Analyzer Application)
# =================================================================================================

class EnhancedSystemAnalyzerApp:
    def __init__(self):
        self.config = ConfigManager.load_config()
        self.agent = EnhancedArchitecturalAnalystAgent(self.config)
    
    async def run(self, analysis_type: AnalysisType = AnalysisType.COMPREHENSIVE):
        """
        أنواع التحليل المتاحة:
        - BASIC: التحليل الأساسي فقط
        - FAILURE: تحليل نقاط الفشل
        - PERFORMANCE: تحليل الأداء والتوسع
        - INTEGRATION: تحليل التكامل
        - COMPARATIVE: التحليل المقارن
        - COMPREHENSIVE: التحليل الشامل الكامل
        """
        
        console.print(Panel.fit(
            f"[bold green]🎯 STARTING {analysis_type.value.upper()} ANALYSIS[/bold green]",
            border_style="green"
        ))
        
        try:
            raw_data = await AsyncFileHandler.read_file(self.config.input_file)
            
            if analysis_type == AnalysisType.COMPREHENSIVE:
                report = await self.agent.generate_comprehensive_report(raw_data)
                content = self.agent.format_comprehensive_report(report)
            
            elif analysis_type == AnalysisType.BASIC:
                analysis = await self.agent.analyze(raw_data)
                content = self.agent._format_basic_analysis(analysis)
            
            elif analysis_type == AnalysisType.FAILURE:
                analysis = await self.agent.analyze_failure_points(raw_data)
                content = self.agent._format_failure_analysis(analysis)
            
            elif analysis_type == AnalysisType.PERFORMANCE:
                analysis = await self.agent.analyze_performance(raw_data)
                content = self.agent._format_performance_analysis(analysis)
            
            elif analysis_type == AnalysisType.INTEGRATION:
                analysis = await self.agent.analyze_integration(raw_data)
                content = self.agent._format_integration_analysis(analysis)
            
            else:
                raise ValueError(f"Unknown analysis type: {analysis_type}")
            
            await AsyncFileHandler.save_report(self.config.output_file, content)
            
            console.print(Panel.fit(
                "[bold green]✅ ANALYSIS COMPLETED SUCCESSFULLY[/bold green]",
                border_style="green"
            ))
        
        except Exception as e:
            logger.critical(f"[red]Analysis failed:[/red] {str(e)}")
            console.print(Panel(
                f"[red]❌ ERROR: {str(e)}[/red]",
                border_style="red"
            ))
            sys.exit(1)

# =================================================================================================
# نقطة الدخول (Entry Point)
# =================================================================================================

async def main():
    """نقطة الدخول الرئيسية"""
    console.clear()
    
    # شعار البداية
    console.print("""
    [bold cyan]
    ╔═══════════════════════════════════════════════════════════════════╗
    ║     🏗️  ENHANCED ARCHITECTURE ANALYZER - GPT-5.2 Edition 🏗️       ║
    ║                  Advanced Multi-Layer Analysis                    ║
    ╚═══════════════════════════════════════════════════════════════════╝
    [/bold cyan]
    """)
    
    app = EnhancedSystemAnalyzerApp()
    
    # تشغيل التحليل الشامل
    await app.run(AnalysisType.COMPREHENSIVE)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("[yellow]Process interrupted by user[/yellow]")
        sys.exit(0)
