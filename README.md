# 📚 Academic Term Paper Bot

A production-ready Telegram bot that automatically generates formatted academic
term papers using **Google Gemini AI** and delivers them as professional **DOCX** files.

---

## ✨ Features

| Feature | Details |
|---|---|
| AI content generation | Google Gemini 1.5 Flash — formal, scholarly prose |
| Cover page | Matches `Sample Term Paper` layout exactly |
| Dynamic sections | 2–5 body sections, scaled to requested page count |
| Logo support | Upload your university logo or use the built-in default |
| Progress feedback | Three-step live progress messages during generation |
| Input validation | Page range check; graceful error messages |
| Clean DOCX | Times New Roman, justified body, APA references |
| Start-over flow | "Start over" button at the confirmation step |

---

## 🗂 Project Structure

```
term_paper_bot/
├── main.py                    # Entry point — polling loop
├── config.py                  # All settings (reads from .env)
├── requirements.txt
├── .env.example               # Copy → .env and fill in keys
├── assets/
│   └── default_logo.png       # Fallback university logo
├── output/                    # Temp output dir (auto-created)
├── handlers/
│   ├── __init__.py
│   ├── states.py              # FSM State enum
│   └── conversation.py        # All telegram handler functions
├── services/
│   ├── __init__.py
│   └── gemini_service.py      # Gemini API calls + PaperContent model
└── utils/
    ├── __init__.py
    └── document_generator.py  # python-docx DOCX builder
```

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10 or newer
- A Telegram Bot token from [@BotFather](https://t.me/BotFather)
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### 2. Clone & install

```bash
git clone https://github.com/your-org/term_paper_bot.git
cd term_paper_bot

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Configure environment

```bash
cp .env.example .env
# Edit .env and add your real keys:
#   TELEGRAM_BOT_TOKEN=...
#   GEMINI_API_KEY=...
```

### 4. Run

```bash
python main.py
```

Open Telegram, find your bot, and send `/start`.

---

## 🤖 Bot Conversation Flow

```
/start
  └─ University name
       └─ Department
            └─ Academic year / grade
                 └─ Student name
                      └─ Supervisor name
                           └─ Term paper title
                                └─ Number of pages (3–8)
                                     └─ Logo (upload / skip)
                                          └─ Confirm summary
                                               └─ [Generate] → sends .docx
```

---

## 📄 Output Document Layout

The generated DOCX exactly mirrors `Sample Term Paper.docx`:

```
Ministry of Higher Education and Scientific Research
{university_name}
{department_name}
{grade_year}

            {TERM PAPER TITLE}

SUBMITTED BY        {student_name}
SUPERVISED BY       {supervisor_name}

──────────────────────────────────────────────

Introduction
  <~150-word paragraph>

Section 1: {AI-generated subtitle}
  <body>

Section 2: {AI-generated subtitle}
  <body>

…

Conclusion
  <~150-word paragraph>

References
  1. …
  2. …
```

---

## ⚙️ Configuration Reference

| Variable | Default | Description |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | *(required)* | Token from @BotFather |
| `GEMINI_API_KEY` | *(required)* | Key from Google AI Studio |
| `GEMINI_MODEL` | `gemini-1.5-flash` | Model to use for generation |

---

## 🔒 Security Notes

- Never commit `.env` — it is in `.gitignore`
- The `output/` directory is ephemeral; files are deleted after sending
- User-uploaded logos are also deleted after each run

---

## 🛠 Extending the Bot

**Add PDF output** — install `docx2pdf` and call it after `generate_docx()`:

```python
from docx2pdf import convert
convert(docx_path, pdf_path)
```

**Switch to webhooks** — replace `run_polling()` in `main.py`:

```python
app.run_webhook(
    listen="0.0.0.0",
    port=8443,
    url_path=TELEGRAM_BOT_TOKEN,
    webhook_url=f"https://yourdomain.com/{TELEGRAM_BOT_TOKEN}",
)
```

**Persist user state** — swap `ContextTypes.DEFAULT_TYPE` for
`PicklePersistence` or a Redis-backed persistence class.

---

## 📝 License

MIT — use freely, attribution appreciated.
