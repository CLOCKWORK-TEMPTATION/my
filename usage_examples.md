# أمثلة الاستخدام - Enhanced Architecture Analyzer

يقدم هذا المستند أمثلة تفصيلية ومتقدمة لاستخدام نظام محلل المعماريات المحسّن.

---

## 📑 جدول المحتويات

1. [الاستخدام الأساسي](#الاستخدام-الأساسي)
2. [أنواع التحليل](#أنواع-التحليل)
3. [التكوين المخصص](#التكوين-المخصص)
4. [الاستخدام البرمجي](#الاستخدام-البرمجي)
5. [حالات الاستخدام المتقدمة](#حالات-الاستخدام-المتقدمة)
6. [استكشاف الأخطاء](#استكشاف-الأخطاء)

---

## 🚀 الاستخدام الأساسي

### مثال 1: التشغيل الافتراضي

```bash
# التشغيل باستخدام uv
uv run enhanced_analyzer.py

# أو باستخدام main.py
uv run main.py

# أو مباشرة بـ Python
python enhanced_analyzer.py
```

**النتيجة المتوقعة:**
```
╔═══════════════════════════════════════════════════════════════════╗
║     🏗️  ENHANCED ARCHITECTURE ANALYZER - GPT-5.2 Edition 🏗️       ║
║                  Advanced Multi-Layer Analysis                    ║
╚═══════════════════════════════════════════════════════════════════╝

✓ Read file 'Session_details.txt' | Size: 45000 chars
🔍 Starting Basic Architecture Analysis...
✓ Basic analysis complete
⚠️ Starting Failure Point Analysis...
✓ Failure analysis complete
🔗 Starting Integration & Compatibility Analysis...
✓ Integration analysis complete
⚡ Starting Performance & Scalability Analysis...
✓ Performance analysis complete
✓ Report saved to 'System_Architecture_Analysis.md'

╔═══════════════════════════════════════════════════════════════════╗
║              ✅ ANALYSIS COMPLETED SUCCESSFULLY                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### مثال 2: اختيار نوع التحليل

```bash
# التحليل الأساسي
uv run main.py --analysis-type basic

# تحليل نقاط الفشل
uv run main.py --analysis-type failure

# تحليل الأداء
uv run main.py --analysis-type performance

# تحليل التكامل
uv run main.py --analysis-type integration

# التحليل المقارن
uv run main.py --analysis-type comparative

# التحليل الشامل (الافتراضي)
uv run main.py --analysis-type comprehensive
```

---

## 🔍 أنواع التحليل

### مثال 1: التحليل الأساسي (Basic)

**السيناريو:** تحليل معمارية نظام بسيط واستخراج المكونات الأساسية

```bash
uv run main.py --analysis-type basic
```

**المدخلات المطلوبة:**
```
Session_details.txt:
```
```
الجلسة: تصميم نظام إدارة المهام
النظام الفائز: TaskFlow Pro

المكونات الأساسية:
- Orchestrator Agent: يدير توزيع المهام بين الوكلاء
- Task Database: يخزن حالة المهام والتقدم
- User Interface: واجهة المستخدم للتفاعل
- Notification Service: يرسل إشعارات للمستخدمين

تدفقات البيانات:
- UI → Orchestrator: طلبات المهام (REST API)
- Orchestrator → Database: حفظ الحالة (PostgreSQL)
- Orchestrator → Notification: إشعارات (WebSocket)
```

**المخرجات المتوقعة:**
```markdown
### المكونات الأساسية
| المكون | النوع | الأهمية | المسؤولية | التقنيات |
|--------|------|--------|-----------|----------|
| Orchestrator Agent | Agent | critical | إدارة توزيع المهام | FastAPI, Python |
| Task Database | Database | high | تخزين حالة المهام | PostgreSQL |
| User Interface | Interface | medium | واجهة المستخدم | React, TypeScript |
| Notification Service | Service | medium | إرسال الإشعارات | WebSocket, Node.js |

### تدفق البيانات
- **User Interface** → **Orchestrator Agent**: طلبات المهام (عبر `REST API`)
- **Orchestrator Agent** → **Task Database**: حفظ الحالة (عبر `PostgreSQL`)
- **Orchestrator Agent** → **Notification Service**: إشعارات (عبر `WebSocket`)

### محرك القرار
- **البروتوكول**: Contract Net Protocol
- **هدف التحسين**: الكفاءة الكلية

### الابتكارات الرئيسية
- 🎯 نظام توزيع المهام الديناميكي
- 🎯 إشعارات فورية عبر WebSocket
- 🎯 واجهة مستخدم تفاعلية

### التحديات المتوقعة
- ⚠️ إدارة التزامن العالي
- ⚠️ ضمان اتساق البيانات
- ⚠️ قابلية التوسع
```

### مثال 2: تحليل نقاط الفشل (Failure)

**السيناريو:** تحليل مخاطر نظام معقد وتحديد نقاط الفشل الحرجة

```bash
uv run main.py --analysis-type failure
```

**المدخلات المطلوبة:**
```
Session_details.txt:
```
```
الجلسة: نظام إدارة المخزون الموزع
النظام الفائز: InventoryHub

المعمارية:
- Central Orchestrator: ينسق العمليات عبر الفروع
- Local Inventory Agents: يدير المخزون في كل فرع
- Distributed Cache: يخزن البيانات المؤقتة
- Message Queue: ينسق الرسائل بين الخدمات

المخاطر المحتملة:
- فشل Central Orchestrator يؤدي لتوقف النظام
- فقدان البيانات في Distributed Cache
- تأخير الرسائل في Message Queue
```

**المخرجات المتوقعة:**
```markdown
### النظام: InventoryHub

#### الثغرات الحرجة

🔴 **فشل Central Orchestrator**
   - الاحتمالية: high
   - الخطورة: catastrophic
   - الاستراتيجية: تنفيذ نظام HA مع Active-Passive
   - البديل: تشغيل Orchestrator محلي في كل فرع

🟠 **فقدان البيانات في Distributed Cache**
   - الاحتمالية: medium
   - الخطورة: critical
   - الاستراتيجية: استخدام Redis Cluster مع استمرارية البيانات
   - البديل: تخزين البيانات الحرجة في PostgreSQL

🟡 **تأخير الرسائل في Message Queue**
   - الاحتمالية: medium
   - الخطورة: minor
   - الاستراتيجية: استخدام RabbitMQ مع Cluster
   - البديل: تنفيذ مهلة زمنية وإعادة المحاولة

#### نقاط الفشل الوحيد
- Central Orchestrator (بدون HA)
- قاعدة البيانات الرئيسية (بدون Replication)
- Message Broker (بدون Cluster)

#### متطلبات التعافي
- **الهدف الزمني للتعافي (RTO)**: 5 دقائق
- **متطلبات التكرار**:
  - Orchestrator: Active-Passive
  - Database: Multi-Master Replication
  - Cache: Redis Cluster
  - Queue: RabbitMQ Cluster

#### خطة التعافي من الكوارث
1. فشل Orchestrator: التبديل التلقائي للـ Passive node
2. فشل Database: التوجيه للـ Replicas
3. فشل Cache: إعادة تحميل البيانات من Database
4. فشل Queue: استخدام Queue الثانوية
```

### مثال 3: تحليل الأداء (Performance)

**السيناريو:** تقييم أداء نظام تجارة إلكترونية وتحديد فرص التحسين

```bash
uv run main.py --analysis-type performance
```

**المدخلات المطلوبة:**
```
Session_details.txt:
```
```
الجلسة: نظام تجارة إلكترونية عالي الأداء
النظام الفائز: ShopFast

المعمارية:
- API Gateway: يدير جميع الطلبات
- Product Service: يدير المنتجات
- Order Service: يدير الطلبات
- Payment Service: يدير المدفوعات
- Redis Cache: يخزن البيانات المؤقتة
- PostgreSQL: قاعدة البيانات الرئيسية

المتطلبات:
- دعم 10,000 طلب في الثانية
- زمن استجابة أقل من 100ms
- قابلية التوسع الأفقي
```

**المخرجات المتوقعة:**
```markdown
### النظام: ShopFast

#### ملف الأداء
- **الإنتاجية المتوقعة**: 10,000 TPS
- **ملف الزمن الكامن**: < 100ms (P95)
- **المعاملات في الثانية (TPS)**: 10,000

#### مقاييس قابلية التوسع

- **API Gateway**
  - السعة الحالية: 5,000 TPS
  - عامل التوسع: 2x
  - عنق الزجاجة: معالجة التوجيه

- **Product Service**
  - السعة الحالية: 3,000 TPS
  - عامل التوسع: 3.3x
  - عنق الزجاجة: استعلامات قاعدة البيانات

- **Order Service**
  - السعة الحالية: 2,000 TPS
  - عامل التوسع: 5x
  - عنق الزجاجة: معالجة الأعمال

- **Payment Service**
  - السعة الحالية: 1,000 TPS
  - عامل التوسع: 10x
  - عنق الزجاجة: تكامل البنوك

#### استراتيجيات التحسين
- **استراتيجية التوسع**: التوسع الأفقي مع Kubernetes
- **موازنة الحمل**: Round-Robin مع Health Checks
- **استراتيجية التخزين المؤقت**: Redis Cluster مع Cache-Aside

#### فرص التحسين
- 🚀 تنفيذ CDN للملفات الثابتة
- 🚀 استخدام Read Replicas لقاعدة البيانات
- 🚀 تنفيذ Event Sourcing للطلبات
- 🚀 تحسين استعلامات قاعدة البيانات
- 🚀 استخدام GraphQL للطلبات المعقدة
```

### مثال 4: تحليل التكامل (Integration)

**السيناريو:** تحليل توافقية نظام قديم مع خدمات حديثة

```bash
uv run main.py --analysis-type integration
```

**المدخلات المطلوبة:**
```
Session_details.txt:
```
```
الجلسة: ترقية نظام إدارة الموارد البشرية
النظام الفائز: HRHub Modern

المكدس التكنولوجي:
- Frontend: React 18, TypeScript
- Backend: Node.js 20, Express
- Database: PostgreSQL 15
- Cache: Redis 7
- Message Queue: RabbitMQ 3.12
- Legacy Integration: SOAP API (Java 8)

نقاط التكامل:
- تكامل مع نظام الرواتب القديم (SOAP)
- تكامل مع نظام Active Directory
- تكامل مع خدمة البريد الإلكتروني
```

**المخرجات المتوقعة:**
```markdown
### النظام: HRHub Modern

#### تحليل المكدس التكنولوجي

🟢 **React 18** (v18.2.0)
   - نقاط التكامل: REST API, WebSocket

🟢 **Node.js 20** (v20.10.0)
   - نقاط التكامل: Express, PostgreSQL, Redis

🟢 **PostgreSQL 15** (v15.2)
   - نقاط التكامل: Node.js, Redis

🟢 **Redis 7** (v7.2.0)
   - نقاط التكامل: Node.js, PostgreSQL

🟠 **RabbitMQ 3.12** (v3.12.10)
   - نقاط التكامل: Node.js, Legacy System

🔴 **Java 8** (v8.0)
   - مشاكل التوافقية: EOL في 2019
   - نقاط التكامل: SOAP API
   - خطر التقادم: high

#### أنماط التكامل
- REST API للخدمات الحديثة
- SOAP API للنظام القديم
- Message Queue للمعالجة غير المتزامنة
- Webhooks للإشعارات

#### درجات التقييم
- **توافقية API**: 85%

#### التقنيات المتقادمة
- ⚠️ Java 8 (EOL في 2019)
- ⚠️ SOAP API (يفضل REST)
- ⚠️ Active Directory (يفضل OAuth2)

#### مسار الهجرة
1. إنشاء API Gateway لتحويل SOAP إلى REST
2. ترقية Java 8 إلى Java 21
3. استبدال SOAP بـ REST API
4. تنفيذ OAuth2 بدلاً من Active Directory

#### الامتثال الأمني
- ✅ تشفير البيانات في النقل (TLS 1.3)
- ✅ تشفير البيانات في التخزين (AES-256)
- ✅ مصادقة JWT
- ✅ RBAC للصلاحيات
```

### مثال 5: التحليل المقارن (Comparative)

**السيناريو:** مقارنة بين نظامين معماريين مختلفين

```bash
uv run main.py --analysis-type comparative
```

**المدخلات المطلوبة:**
```
Session_details.txt:
```
```
الجلسة: اختيار معمارية نظام الدردشة

النظام الأول: ChatFlow (Microservices)
المعمارية:
- Microservices Architecture
- Kubernetes Deployment
- MongoDB Database
- WebSocket Communication
- Redis Cache

النظام الثاني: ChatHub (Monolithic)
المعمارية:
- Monolithic Architecture
- Docker Deployment
- PostgreSQL Database
- WebSocket Communication
- In-Memory Cache
```

**المخرجات المتوقعة:**
```markdown
#### مقارنة: ChatFlow vs ChatHub

- **الفارق في الأداء**: ChatFlow أسرع بـ 20% في الاستجابة
- **نسبة التعقيد**: ChatFlow 2.5x أكثر تعقيداً
- **مقارنة كفاءة التكاليف**: ChatHub أرخص بـ 40% في التشغيل

#### العوامل المؤثرة في القرار
- قابلية التوسع: ChatFlow أفضل
- سهولة التطوير: ChatHub أفضل
- الصيانة: ChatFlow أفضل
- التكلفة: ChatHub أفضل
- الموثوقية: ChatFlow أفضل

#### المقايضات والخيارات
- ChatFlow: أداء أعلى وتوسع أفضل لكن تكلفة أعلى وتعقيد أكثر
- ChatHub: تكلفة أقل وسهولة تطوير لكن قابلية توسع محدودة

#### التوصية
**استخدم ChatFlow إذا:**
- تحتاج إلى قابلية توسع عالية
- لديك فريق كبير للتطوير
- الميزانية ليست مشكلة

**استخدم ChatHub إذا:**
- النظام صغير أو متوسط
- الفريق صغير
- تحتاج إلى تقليل التكاليف
```

### مثال 6: التحليل الشامل (Comprehensive)

**السيناريو:** تحليل شامل لنظام معقد

```bash
uv run main.py --analysis-type comprehensive
```

**المدخلات المطلوبة:**
```
Session_details.txt:
```
```
الجلسة: تصميم نظام إدارة سلسلة التوريد
النظام الفائز: SupplyChain Pro

المعمارية الكاملة:
[وصف مفصل للمعمارية مع جميع التفاصيل]
```

**المخرجات المتوقعة:**
```markdown
# 📊 تقرير التحليل المعماري الشامل

**تم الإنشاء**: 2026-01-04T05:00:00.000Z
**مستوى الثقة**: 94%

---

## 1️⃣ التحليل الأساسي

### المكونات الأساسية
| المكون | النوع | الأهمية | المسؤولية | التقنيات |
|--------|------|--------|-----------|----------|
| Orchestrator Agent | Agent | critical | تنسيق العمليات | FastAPI, Python |
| Inventory Service | Service | high | إدارة المخزون | Node.js, PostgreSQL |
| Order Service | Service | high | إدارة الطلبات | Go, MongoDB |
| Shipping Service | Service | medium | إدارة الشحن | Java, PostgreSQL |
| Analytics Service | Service | low | التحليلات | Python, BigQuery |

### تدفق البيانات
- **Orchestrator Agent** → **Inventory Service**: طلبات المخزون (عبر `gRPC`)
- **Orchestrator Agent** → **Order Service**: طلبات الطلبات (عبر `REST API`)
- **Order Service** → **Shipping Service**: طلبات الشحن (عبر `Message Queue`)

### محرك القرار
- **البروتوكول**: Contract Net Protocol
- **هدف التحسين**: تقليل التكاليف

### الابتكارات الرئيسية
- 🎯 نظام توزيع ديناميكي للمخزون
- 🎯 تحليلات فورية للطلب
- 🎯 تتبع شحن ذكي

### التحديات المتوقعة
- ⚠️ إدارة التزامن العالي
- ⚠️ ضمان اتساق البيانات
- ⚠️ قابلية التوسع

---

## 2️⃣ تحليل نقاط الفشل والمخاطر

### الثغرات الحرجة
🔴 **فشل Orchestrator Agent**
   - الاحتمالية: high
   - الخطورة: catastrophic
   - الاستراتيجية: تنفيذ HA

---

## 3️⃣ تقرير التكامل والتوافقية

### تحليل المكدس التكنولوجي
🟢 **FastAPI** (v0.104.1)
   - نقاط التكامل: PostgreSQL, MongoDB, Redis

---

## 4️⃣ تحليل الأداء والقابلية للتوسع

### ملف الأداء
- **الإنتاجية المتوقعة**: 5,000 TPS
- **ملف الزمن الكامن**: < 200ms

---

## 📝 الملخص التنفيذي

### النقاط الرئيسية
- **النظام المحلل**: SupplyChain Pro
- **عدد المكونات الأساسية**: 5
- **عدد تدفقات البيانات**: 3
- **الابتكارات المحددة**: 3
- **التحديات المعروفة**: 3
- **الثغرات الحرجة**: 1
- **توافقية API**: 90%

---

*تم إنشاء هذا التقرير بواسطة نظام التحليل المعماري المحسّن - GPT-5.2*
```

---

## ⚙️ التكوين المخصص

### مثال 1: تخصيص ملفات الإدخال والإخراج

**تعديل [`enhanced_analyzer.py`](enhanced_analyzer.py:201):**

```python
return AppConfig(
    api_key=api_key,
    input_file="my_custom_input.txt",      # ملف إدخال مخصص
    output_file="my_custom_output.md",    # ملف إخراج مخصص
    analysis_type=AnalysisType.COMPREHENSIVE
)
```

**الاستخدام:**
```bash
# إنشاء ملف الإدخال المخصص
echo "محتوى سجل الجلسة المخصص..." > my_custom_input.txt

# تشغيل التحليل
uv run enhanced_analyzer.py

# التقرير سيُحفظ في my_custom_output.md
```

### مثال 2: تخصيص النموذج

**تعديل [`enhanced_analyzer.py`](enhanced_analyzer.py:181):**

```python
@dataclass
class AppConfig:
    api_key: str
    input_file: str
    output_file: str
    model_name: str = "gpt-4o-mini"  # استخدام نموذج أسرع وأرخص
    analysis_type: AnalysisType = AnalysisType.COMPREHENSIVE
    temperature: float = 0.2
```

**الخيارات المتاحة:**
- `gpt-5.2-2025-12-11` - الأكثر دقة (الافتراضي)
- `gpt-4o` - متوازن
- `gpt-4o-mini` - سريع واقتصادي
- `gpt-4-turbo` - جيد للأعمال الروتينية

### مثال 3: تخصيص درجة الحرارة

**تعديل [`enhanced_analyzer.py`](enhanced_analyzer.py:183):**

```python
@dataclass
class AppConfig:
    api_key: str
    input_file: str
    output_file: str
    model_name: str = "gpt-5.2-2025-12-11"
    analysis_type: AnalysisType = AnalysisType.COMPREHENSIVE
    temperature: float = 0.1  # أكثر تحفظاً (0.0-1.0)
```

**التوصيات:**
- `0.0-0.2` - للتحليلات التقنية الدقيقة
- `0.3-0.5` - للتحليلات الإبداعية
- `0.6-1.0` - للمحتوى الإبداعي (غير موصى به للتحليل المعماري)

### مثال 4: استخدام ملفات .env متعددة

**إنشاء ملفات بيئة متعددة:**

```bash
# .env (البيئة الافتراضية)
OPENAI_API_KEY=sk-proj-default-key

# .env.local (البيئة المحلية)
OPENAI_API_KEY=sk-proj-local-key

# .env.production (البيئة الإنتاجية)
OPENAI_API_KEY=sk-proj-prod-key
```

**الاستخدام:**
```bash
# استخدام البيئة الافتراضية
uv run enhanced_analyzer.py

# استخدام البيئة المحلية
OPENAI_API_KEY=sk-proj-local-key uv run enhanced_analyzer.py

# استخدام البيئة الإنتاجية
export OPENAI_API_KEY=sk-proj-prod-key
uv run enhanced_analyzer.py
```

---

## 💻 الاستخدام البرمجي

### مثال 1: استخدام التطبيق مباشرة

```python
import asyncio
from enhanced_analyzer import EnhancedSystemAnalyzerApp, AnalysisType

async def run_basic_analysis():
    """تشغيل التحليل الأساسي"""
    app = EnhancedSystemAnalyzerApp()
    await app.run(AnalysisType.BASIC)

asyncio.run(run_basic_analysis())
```

### مثال 2: استخدام الوكيل مباشرة

```python
import asyncio
from enhanced_analyzer import EnhancedArchitecturalAnalystAgent, ConfigManager

async def run_custom_analysis():
    """تشغيل تحليل مخصص"""
    config = ConfigManager.load_config()
    agent = EnhancedArchitecturalAnalystAgent(config)
    
    # قراءة الملف
    from enhanced_analyzer import AsyncFileHandler
    raw_data = await AsyncFileHandler.read_file("Session_details.txt")
    
    # تشغيل التحليل الأساسي
    basic_result = await agent.analyze(raw_data)
    
    # تشغيل تحليل الفشل
    failure_result = await agent.analyze_failure_points(raw_data)
    
    # تنسيق النتائج
    basic_content = agent._format_basic_analysis(basic_result)
    failure_content = agent._format_failure_analysis(failure_result)
    
    # حفظ النتائج
    await AsyncFileHandler.save_report("basic_report.md", basic_content)
    await AsyncFileHandler.save_report("failure_report.md", failure_content)

asyncio.run(run_custom_analysis())
```

### مثال 3: إنشاء تقرير شامل مخصص

```python
import asyncio
from enhanced_analyzer import EnhancedArchitecturalAnalystAgent, ConfigManager, AsyncFileHandler

async def generate_custom_report():
    """إنشاء تقرير شامل مخصص"""
    config = ConfigManager.load_config()
    agent = EnhancedArchitecturalAnalystAgent(config)
    
    # قراءة الملفات
    system_a = await AsyncFileHandler.read_file("system_a.txt")
    system_b = await AsyncFileHandler.read_file("system_b.txt")
    
    # إنشاء التقرير الشامل
    report = await agent.generate_comprehensive_report(system_a, system_b)
    
    # تنسيق التقرير
    content = agent.format_comprehensive_report(report)
    
    # حفظ التقرير
    await AsyncFileHandler.save_report("custom_report.md", content)

asyncio.run(generate_custom_report())
```

### مثال 4: معالجة الأخطاء

```python
import asyncio
import logging
from enhanced_analyzer import EnhancedSystemAnalyzerApp, AnalysisType

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_with_error_handling():
    """تشغيل التحليل مع معالجة الأخطاء"""
    try:
        app = EnhancedSystemAnalyzerApp()
        await app.run(AnalysisType.COMPREHENSIVE)
        logger.info("✅ التحليل اكتمل بنجاح")
    except FileNotFoundError as e:
        logger.error(f"❌ ملف الإدخال غير موجود: {e}")
    except ValueError as e:
        logger.error(f"❌ خطأ في القيم: {e}")
    except Exception as e:
        logger.error(f"❌ خطأ غير متوقع: {e}")
        raise

asyncio.run(run_with_error_handling())
```

### مثال 5: تشغيل تحليلات متعددة بالتوازي

```python
import asyncio
from enhanced_analyzer import EnhancedArchitecturalAnalystAgent, ConfigManager, AsyncFileHandler, AnalysisType

async def run_parallel_analyses():
    """تشغيل تحليلات متعددة بالتوازي"""
    config = ConfigManager.load_config()
    agent = EnhancedArchitecturalAnalystAgent(config)
    
    # قراءة الملف
    raw_data = await AsyncFileHandler.read_file("Session_details.txt")
    
    # تشغيل التحليلات بالتوازي
    tasks = [
        agent.analyze(raw_data),
        agent.analyze_failure_points(raw_data),
        agent.analyze_integration(raw_data),
        agent.analyze_performance(raw_data)
    ]
    
    results = await asyncio.gather(*tasks)
    
    # حفظ النتائج
    await AsyncFileHandler.save_report("basic.md", agent._format_basic_analysis(results[0]))
    await AsyncFileHandler.save_report("failure.md", agent._format_failure_analysis(results[1]))
    await AsyncFileHandler.save_report("integration.md", agent._format_integration_analysis(results[2]))
    await AsyncFileHandler.save_report("performance.md", agent._format_performance_analysis(results[3]))

asyncio.run(run_parallel_analyses())
```

---

## 🎯 حالات الاستخدام المتقدمة

### مثال 1: تحليل معمارية موجودة

**السيناريو:** تحليل معمارية نظام موجود لتحديد فرص التحسين

```bash
# 1. إنشاء ملف وصف المعمارية
cat > existing_architecture.txt << 'EOF'
الجلسة: تحليل نظام CRM الموجود
النظام الحالي: Legacy CRM

المعمارية الحالية:
- Monolithic Application
- PHP 7.4 Backend
- MySQL 5.7 Database
- jQuery Frontend
- No Caching Layer
- No Message Queue

المشاكل الحالية:
- أداء بطيء
- صعوبة الصيانة
- عدم قابلية التوسع
- تقنيات قديمة
EOF

# 2. تشغيل التحليل الشامل
uv run main.py --analysis-type comprehensive

# 3. مراجعة التقرير
cat System_Architecture_Analysis.md
```

### مثال 2: تقييم مقترحات معمارية متعددة

**السيناريو:** مقارنة بين مقترحات معمارية مختلفة

```python
import asyncio
from enhanced_analyzer import EnhancedArchitecturalAnalystAgent, ConfigManager, AsyncFileHandler

async def compare_proposals():
    """مقارنة بين مقترحات معمارية متعددة"""
    config = ConfigManager.load_config()
    agent = EnhancedArchitecturalAnalystAgent(config)
    
    # قراءة المقترحات
    proposal_a = await AsyncFileHandler.read_file("proposal_a.txt")
    proposal_b = await AsyncFileHandler.read_file("proposal_b.txt")
    proposal_c = await AsyncFileHandler.read_file("proposal_c.txt")
    
    # مقارنة A vs B
    comparison_ab = await agent.compare_architectures(proposal_a, proposal_b)
    await AsyncFileHandler.save_report(
        "comparison_ab.md",
        agent._format_comparison(comparison_ab)
    )
    
    # مقارنة B vs C
    comparison_bc = await agent.compare_architectures(proposal_b, proposal_c)
    await AsyncFileHandler.save_report(
        "comparison_bc.md",
        agent._format_comparison(comparison_bc)
    )
    
    # مقارنة A vs C
    comparison_ac = await agent.compare_architectures(proposal_a, proposal_c)
    await AsyncFileHandler.save_report(
        "comparison_ac.md",
        agent._format_comparison(comparison_ac)
    )

asyncio.run(compare_proposals())
```

### مثال 3: إنشاء تقارير دورية

**السيناريو:** إنشاء تقارير دورية لمراقبة المعمارية

```python
import asyncio
import schedule
import time
from datetime import datetime
from enhanced_analyzer import EnhancedSystemAnalyzerApp, AnalysisType

async def generate_weekly_report():
    """إنشاء تقرير أسبوعي"""
    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = f"weekly_report_{timestamp}.md"
    
    # تعديل ملف الإخراج
    from enhanced_analyzer import ConfigManager
    config = ConfigManager.load_config()
    config.output_file = output_file
    
    # تشغيل التحليل
    app = EnhancedSystemAnalyzerApp()
    await app.run(AnalysisType.COMPREHENSIVE)

def run_scheduler():
    """تشغيل المجدول"""
    schedule.every().friday.at("09:00").do(
        lambda: asyncio.run(generate_weekly_report())
    )
    
    while True:
        schedule.run_pending()
        time.sleep(60)

# تشغيل المجدول
# run_scheduler()
```

### مثال 4: تحليل معمارية مع تكامل CI/CD

**السيناريو:** دمج التحليل المعماري في عملية CI/CD

```yaml
# .github/workflows/architecture-analysis.yml
name: Architecture Analysis

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  analyze:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install uv
          uv sync
      
      - name: Run architecture analysis
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          uv run main.py --analysis-type comprehensive
      
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: architecture-report
          path: System_Architecture_Analysis.md
```

### مثال 5: تحليل معمارية مع تصدير JSON

**السيناريو:** تصدير النتائج بصيغة JSON للمعالجة الإضافية

```python
import asyncio
import json
from enhanced_analyzer import EnhancedArchitecturalAnalystAgent, ConfigManager, AsyncFileHandler

async def export_to_json():
    """تصدير النتائج بصيغة JSON"""
    config = ConfigManager.load_config()
    agent = EnhancedArchitecturalAnalystAgent(config)
    
    # قراءة الملف
    raw_data = await AsyncFileHandler.read_file("Session_details.txt")
    
    # تشغيل التحليل
    report = await agent.generate_comprehensive_report(raw_data)
    
    # تحويل إلى JSON
    report_dict = report.model_dump()
    
    # حفظ JSON
    with open("architecture_report.json", "w", encoding="utf-8") as f:
        json.dump(report_dict, f, ensure_ascii=False, indent=2)
    
    print("✅ تم تصدير التقرير بصيغة JSON")

asyncio.run(export_to_json())
```

---

## 🔧 استكشاف الأخطاء

### مثال 1: خطأ في ملف الإدخال

**المشكلة:**
```
❌ Error: File 'Session_details.txt' not found.
```

**الحل:**
```bash
# التحقق من وجود الملف
ls -la Session_details.txt

# إنشاء الملف إذا لم يكن موجوداً
echo "محتوى سجل الجلسة..." > Session_details.txt

# أو تحديد ملف آخر
# عدّل enhanced_analyzer.py:203
input_file="my_file.txt"
```

### مثال 2: خطأ في مفتاح API

**المشكلة:**
```
❌ Configuration Error: Environment variable 'OPENAI_API_KEY' is missing.
```

**الحل:**
```bash
# إنشاء ملف .env
echo "OPENAI_API_KEY=sk-proj-..." > .env

# التحقق من المفتاح
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENAI_API_KEY'))"

# أو تعيين المفتاح مباشرة
export OPENAI_API_KEY=sk-proj-...
uv run enhanced_analyzer.py
```

### مثال 3: خطأ في الاتصال

**المشكلة:**
```
❌ Analysis Error: Connection error
```

**الحل:**
```bash
# التحقق من الاتصال بالإنترنت
ping api.openai.com

# التحقق من صحة المفتاح
curl -H "Authorization: Bearer $OPENAI_API_KEY" https://api.openai.com/v1/models

# التحقق من حالة الخدمة
# https://status.openai.com
```

### مثال 4: خطأ في الذاكرة

**المشكلة:**
```
❌ Analysis Error: Out of memory
```

**الحل:**
```bash
# تقليل حجم ملف الإدخال
head -n 1000 Session_details.txt > small_session.txt

# استخدام نموذج أخف
# عدّل enhanced_analyzer.py:181
model_name: str = "gpt-4o-mini"

# زيادة الذاكرة المتاحة
# Linux/macOS
export PYTHONMALLOC=malloc
# Windows
set PYTHONMALLOC=malloc
```

### مثال 5: خطأ في المهلة الزمنية

**المشكلة:**
```
❌ Analysis Error: Timeout
```

**الحل:**
```python
# تعديل enhanced_analyzer.py
# إضافة timeout parameter
result = await self.client.chat.completions.create(
    model=self.model,
    response_model=ArchitectureResult,
    messages=[...],
    temperature=self.temperature,
    max_retries=3,
    timeout=300.0  # 5 دقائق
)
```

---

## 📚 ملخص

### أمثلة التشغيل السريع

```bash
# 1. التحليل الأساسي
uv run main.py --analysis-type basic

# 2. تحليل الفشل
uv run main.py --analysis-type failure

# 3. تحليل الأداء
uv run main.py --analysis-type performance

# 4. تحليل التكامل
uv run main.py --analysis-type integration

# 5. التحليل المقارن
uv run main.py --analysis-type comparative

# 6. التحليل الشامل
uv run main.py --analysis-type comprehensive
```

### أمثلة الاستخدام البرمجي

```python
# 1. استخدام التطبيق مباشرة
from enhanced_analyzer import EnhancedSystemAnalyzerApp, AnalysisType
app = EnhancedSystemAnalyzerApp()
await app.run(AnalysisType.COMPREHENSIVE)

# 2. استخدام الوكيل مباشرة
from enhanced_analyzer import EnhancedArchitecturalAnalystAgent, ConfigManager
config = ConfigManager.load_config()
agent = EnhancedArchitecturalAnalystAgent(config)
result = await agent.analyze(raw_data)

# 3. معالجة الملفات
from enhanced_analyzer import AsyncFileHandler
raw_data = await AsyncFileHandler.read_file("input.txt")
await AsyncFileHandler.save_report("output.md", content)
```

### نصائح للاستخدام الأمثل

1. **استخدم التحليل الشامل** للتقييم الكامل
2. **استخدم التحليل المحدد** للتركيز على جانب معين
3. **استخدم النماذج الأخف** للأعمال الروتينية
4. **استخدم المعالجة غير المتزامنة** للأداء الأمثل
5. **استخدم معالجة الأخطاء** للإنتاج

---

*تم إنشاؤه بعناية فائقة - يناير 2026*
