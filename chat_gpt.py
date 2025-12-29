from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

# Register Unicode font
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

# Dark background
def dark_bg(canvas, doc):
    canvas.setFillColor(colors.HexColor("#0F1115"))
    canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], stroke=0, fill=1)
    canvas.setFillColor(colors.white)

# Styles
styles = getSampleStyleSheet()

title = ParagraphStyle(
    "title",
    fontName="HeiseiKakuGo-W5",
    fontSize=22,
    textColor=colors.white,
    alignment=1,
    spaceAfter=20
)

heading = ParagraphStyle(
    "heading",
    fontName="HeiseiKakuGo-W5",
    fontSize=14,
    textColor=colors.HexColor("#E6E6E6"),
    spaceBefore=12,
    spaceAfter=8
)

body = ParagraphStyle(
    "body",
    fontName="HeiseiKakuGo-W5",
    fontSize=11,
    leading=16,
    textColor=colors.HexColor("#CFCFCF"),
    spaceAfter=6
)

check = ParagraphStyle(
    "check",
    fontName="HeiseiKakuGo-W5",
    fontSize=11,
    leading=16,
    textColor=colors.HexColor("#B0FFB0"),
    spaceAfter=4
)

# Document
path = "/mnt/data/Section_1_Core_Agentic_AI_Interview_Premium.pdf"
doc = SimpleDocTemplate(path, pagesize=letter)

frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
template = PageTemplate(id="dark", frames=[frame], onPage=dark_bg)
doc.addPageTemplates([template])

content = []

# Title Page
content.append(Paragraph("SECTION 1 — Core Agentic AI Concepts", title))
content.append(Paragraph("Premium Interview Preparation PDF<br/>Junior Agentic AI Developer", body))
content.append(Spacer(1, 30))

# Interview questions
questions = [
    "What is Agentic AI?",
    "How is Agentic AI different from a chatbot?",
    "What is an AI Agent?",
    "Core components of an agentic system",
    "Explain the Agentic Loop",
    "Difference between LLM and Agent",
    "Why agents need tools",
    "What is autonomy in agents?",
    "Explain perception, reasoning, and action",
    "What is goal-oriented behavior?",
    "What is task decomposition?",
    "What is multi-step reasoning?",
    "Reactive vs deliberative agents",
    "Hybrid agents",
    "Learning agents",
    "Role of environment in agent systems",
    "Decision-making in agents",
    "Feedback loop in agents",
    "Real-world use cases of Agentic AI"
]

content.append(Paragraph("Key Interview Questions to Prepare", heading))

for q in questions:
    content.append(Paragraph(f"☐ {q}", check))

content.append(Spacer(1, 20))

# Definitions
content.append(Paragraph("Must-Memorize Definitions", heading))
content.append(Paragraph(
    "Agentic AI: AI systems that autonomously plan, decide, act, and use tools to achieve goals without continuous human intervention.",
    body
))
content.append(Paragraph(
    "Agentic Loop: A continuous cycle of perception → reasoning → action → feedback.",
    body
))

content.append(Spacer(1, 20))

content.append(Paragraph("Interview Tip", heading))
content.append(Paragraph(
    "Always explain agentic systems using a simple analogy (intern/assistant/employee) and then map it to system architecture.",
    body
))

doc.build(content)

path
