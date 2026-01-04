import { useState, useRef } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";
import { Loader2, Upload, FileText, CheckCircle2, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { Badge } from "@/components/ui/badge";

// Types
interface AnalysisResponse {
  success: boolean;
  analysis_type: string;
  report: string;
  generated_at: string;
  message?: string;
}

interface AnalysisType {
  value: string;
  label: string;
  description: string;
}

const ANALYSIS_TYPES: AnalysisType[] = [
  {
    value: "comprehensive",
    label: "تحليل شامل (Comprehensive)",
    description: "تحليل معماري كامل متعدد الطبقات"
  },
  {
    value: "basic",
    label: "تحليل أساسي (Basic)",
    description: "تحليل المكونات وتدفقات البيانات الأساسية"
  },
  {
    value: "failure",
    label: "تحليل نقاط الفشل (Failure Analysis)",
    description: "تحديد المخاطر ونقاط الفشل المحتملة"
  },
  {
    value: "performance",
    label: "تحليل الأداء (Performance)",
    description: "تقييم الأداء والتوسعية"
  },
  {
    value: "integration",
    label: "تحليل التكامل (Integration)",
    description: "تحليل التوافقية والتكامل التقني"
  }
];

function App() {
  const [activeTab, setActiveTab] = useState("text");
  const [textInput, setTextInput] = useState("");
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [analysisType, setAnalysisType] = useState("comprehensive");
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState<AnalysisResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
    }
  };

  const handleAnalyze = async () => {
    setIsLoading(true);
    setError(null);
    setResult(null);

    try {
      let response;
      
      if (activeTab === "text") {
        if (!textInput.trim()) {
          throw new Error("الرجاء إدخال نص للتحليل");
        }
        
        response = await axios.post<AnalysisResponse>("http://localhost:8000/api/analyze", {
          text: textInput,
          analysis_type: analysisType,
          model_name: "gpt-4"
        });
      } else {
        if (!selectedFile) {
          throw new Error("الرجاء اختيار ملف للتحليل");
        }
        
        const formData = new FormData();
        formData.append("file", selectedFile);
        
        response = await axios.post<AnalysisResponse>(
          `http://localhost:8000/api/analyze-file?analysis_type=${analysisType}&model_name=gpt-4`,
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
      }

      setResult(response.data);
    } catch (err) {
      console.error(err);
      if (axios.isAxiosError(err) && err.response) {
        setError(err.response.data.detail || "حدث خطأ أثناء التحليل");
      } else if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("حدث خطأ غير متوقع");
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 p-4 md:p-8 font-sans" dir="rtl">
      <div className="max-w-5xl mx-auto space-y-8">
        
        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-4xl font-bold tracking-tight text-slate-900 dark:text-white">
            محلل البنية التحتية المعزز
          </h1>
          <p className="text-lg text-slate-600 dark:text-slate-400">
            تحليل معماري ذكي باستخدام الذكاء الاصطناعي
          </p>
        </div>

        {/* Main Input Section */}
        <Card className="border-slate-200 dark:border-slate-800 shadow-sm">
          <CardHeader>
            <CardTitle>إدخال البيانات</CardTitle>
            <CardDescription>
              قم بإدخال وصف النظام أو رفع ملف يحتوي على التفاصيل
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            
            {/* Analysis Type Selector */}
            <div className="space-y-2">
              <label className="text-sm font-medium text-slate-700 dark:text-slate-300">
                نوع التحليل
              </label>
              <Select value={analysisType} onValueChange={setAnalysisType}>
                <SelectTrigger className="w-full md:w-[300px] text-right" dir="rtl">
                  <SelectValue placeholder="اختر نوع التحليل" />
                </SelectTrigger>
                <SelectContent dir="rtl">
                  {ANALYSIS_TYPES.map((type) => (
                    <SelectItem key={type.value} value={type.value}>
                      {type.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            {/* Input Tabs */}
            <Tabs defaultValue="text" value={activeTab} onValueChange={setActiveTab} className="w-full">
              <TabsList className="grid w-full grid-cols-2 mb-4">
                <TabsTrigger value="text">نص مباشر</TabsTrigger>
                <TabsTrigger value="file">رفع ملف</TabsTrigger>
              </TabsList>
              
              <TabsContent value="text" className="space-y-4">
                <Textarea
                  placeholder="أدخل وصف النظام هنا..."
                  className="min-h-[200px] font-mono text-sm"
                  value={textInput}
                  onChange={(e) => setTextInput(e.target.value)}
                />
              </TabsContent>
              
              <TabsContent value="file" className="space-y-4">
                <div 
                  className="border-2 border-dashed border-slate-300 dark:border-slate-700 rounded-lg p-12 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors"
                  onClick={() => fileInputRef.current?.click()}
                >
                  <input
                    type="file"
                    className="hidden"
                    ref={fileInputRef}
                    onChange={handleFileChange}
                    accept=".txt,.md"
                  />
                  <Upload className="h-10 w-10 text-slate-400 mb-4" />
                  <p className="text-sm text-slate-600 dark:text-slate-400 font-medium">
                    {selectedFile ? selectedFile.name : "اضغط لرفع ملف نصي (.txt, .md)"}
                  </p>
                  {selectedFile && (
                    <Badge variant="secondary" className="mt-2">
                      {(selectedFile.size / 1024).toFixed(2)} KB
                    </Badge>
                  )}
                </div>
              </TabsContent>
            </Tabs>

            {/* Error Message */}
            {error && (
              <Alert variant="destructive">
                <AlertCircle className="h-4 w-4" />
                <AlertTitle>خطأ</AlertTitle>
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            )}

          </CardContent>
          <CardFooter>
            <Button 
              className="w-full text-lg h-12" 
              onClick={handleAnalyze} 
              disabled={isLoading}
            >
              {isLoading ? (
                <>
                  <Loader2 className="ml-2 h-5 w-5 animate-spin" />
                  جاري التحليل...
                </>
              ) : (
                <>
                  <FileText className="ml-2 h-5 w-5" />
                  بدء التحليل
                </>
              )}
            </Button>
          </CardFooter>
        </Card>

        {/* Results Section */}
        {result && (
          <div className="space-y-4 animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="flex items-center justify-between">
              <h2 className="text-2xl font-bold text-slate-900 dark:text-white">نتائج التحليل</h2>
              <Badge variant="outline" className="text-sm px-3 py-1">
                {new Date(result.generated_at).toLocaleString('ar-SA')}
              </Badge>
            </div>
            
            <Card className="border-slate-200 dark:border-slate-800 overflow-hidden">
              <CardHeader className="bg-slate-50 dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800">
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="h-5 w-5 text-green-500" />
                  <CardTitle>تقرير {ANALYSIS_TYPES.find(t => t.value === result.analysis_type)?.label}</CardTitle>
                </div>
              </CardHeader>
              <CardContent className="p-6 md:p-8">
                <div className="prose prose-slate dark:prose-invert max-w-none prose-headings:font-bold prose-h1:text-3xl prose-h2:text-2xl prose-h2:mt-8 prose-h2:mb-4 prose-p:leading-relaxed prose-li:marker:text-primary">
                  <ReactMarkdown>{result.report}</ReactMarkdown>
                </div>
              </CardContent>
            </Card>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;
