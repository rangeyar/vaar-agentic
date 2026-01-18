# Multi-Agent Chat Application

An agentic AI application where multiple agents chat with each other, built with AutoGen, Streamlit, and OpenAI.

## Current Status: Step 1 - Mom Agent

### Mom Agent 👩

- **Role:** 35-year-old Indian middle-class mother
- **Goal:** Convince her son to reduce screen time and focus on studies
- **Characteristics:**
  - Caring but firm approach
  - Uses emotional and practical reasoning
  - References traditional Indian values about education
  - Concerned about health and academic performance

## Setup

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. Clone or navigate to this directory

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file (copy from `.env.example`):

```bash
copy .env.example .env
```

4. Add your OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Using the Application

1. Enter your OpenAI API key in the sidebar (if not already in `.env` file)
2. Select your preferred model (gpt-3.5-turbo, gpt-4, etc.)
3. Start chatting with the Mom agent
4. Try topics like:
   - "I want to play video games"
   - "Why should I study?"
   - "All my friends use phones"
   - "I'll study later"

## Project Structure

```
autogen-group-chat/
├── agents/                    # Agent definitions folder
│   ├── __init__.py           # Package initialization
│   ├── mom_agent.py          # Mom agent
│   ├── arvashu_agent.py      # Arvashu (son) agent
│   └── README.md             # Detailed agent documentation
├── app.py                    # Streamlit application
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── .env                      # Your API keys (not in git)
├── .gitignore               # Git ignore file
├── CODE_EXPLANATION.md       # Detailed code explanation
└── README.md                 # This file
```

## Technology Stack

- **AutoGen**: Multi-agent framework
- **Streamlit**: Web interface
- **OpenAI**: Language model provider
- **Python**: Programming language

## Future Steps

- ✅ Step 1: Mom agent (DONE)
- ✅ Step 2: Arvashu (Son) agent (DONE)
- ⏳ Step 3: Enable Mom-Arvashu conversation
- ⏳ Step 4: Add Teacher agent
- ⏳ Step 5: Add Friend agent
- ⏳ Step 6: Multi-agent group chat scenarios

## Notes

- Two agents are now available: Mom and Arvashu
- Each agent has a distinct personality and communication style
- Different OpenAI models provide different quality responses (GPT-4 > GPT-3.5-turbo)
- You can modify agent personalities in the `agents/` folder
- See `agents/README.md` for detailed agent documentation
- See `CODE_EXPLANATION.md` for detailed code walkthrough

## License

MIT License
