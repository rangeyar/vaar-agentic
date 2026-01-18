# 📖 Code Explanation - Multi-Agent Chat Application

## 🎯 Overview

This application creates a web interface where you can chat with an AI "Mom Agent" who tries to convince you to study more and reduce screen time.

---

## 🔄 Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│  USER runs: streamlit run app.py                             │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: app.py starts (Line 1)                              │
│  ├─ Import libraries (streamlit, asyncio, etc.)              │
│  ├─ Import create_mom_agent from agents.py                   │
│  └─ Load .env file (if exists) for API key                   │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Web Page Setup (Lines 14-22)                        │
│  ├─ Set page title, icon, layout                             │
│  └─ Display main title "Multi-Agent Chat Application"        │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Create Sidebar (Lines 24-59)                        │
│  ├─ Text input for OpenAI API Key                            │
│  ├─ Dropdown to select GPT model                             │
│  └─ Display Mom Agent information                            │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Initialize Session State (Lines 61-67)              │
│  ├─ st.session_state.messages = []  (chat history)           │
│  └─ st.session_state.agent_initialized = False               │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Display Chat History (Lines 69-72)                  │
│  └─ Loop through messages and display them                   │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 6: Wait for User Input (Line 76)                       │
│  └─ user_input = st.chat_input("Type...")                    │
└───────────────────┬─────────────────────────────────────────┘
                    │
        ┌───────────┴────────────┐
        │  USER TYPES MESSAGE    │
        └───────────┬────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 7: Process User Message (Lines 80-84)                  │
│  ├─ Display user message on screen                           │
│  └─ Add to session_state.messages                            │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 8: Initialize Agent (First Time Only) (Lines 86-93)    │
│  ├─ Check: if not agent_initialized?                         │
│  ├─ YES → Call create_mom_agent(api_key, model)              │
│  │         ↓                                                  │
│  │   ┌─────────────────────────────────────────────┐         │
│  │   │  Go to agents.py                             │         │
│  │   │  ├─ Create OpenAIChatCompletionClient        │         │
│  │   │  ├─ Set system_message (mom personality)     │         │
│  │   │  └─ Create AssistantAgent                    │         │
│  │   │  └─ Return mom_agent                         │         │
│  │   └─────────────────────────────────────────────┘         │
│  │         ↓                                                  │
│  ├─ Store agent in st.session_state.mom_agent                │
│  └─ Set agent_initialized = True                             │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 9: Get Mom Agent Response (Lines 96-118)               │
│  ├─ Create async function get_response()                     │
│  ├─ Call: mom_agent.on_messages([TextMessage(...)])          │
│  │    ↓                                                       │
│  │  This sends user message to OpenAI API                    │
│  │  OpenAI processes with mom's personality                  │
│  │  Returns response                                         │
│  │    ↓                                                       │
│  ├─ Use asyncio to run the async function                    │
│  ├─ Display response on screen                               │
│  └─ Add response to session_state.messages                   │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 10: Wait for Next User Input                           │
│  └─ Loop back to STEP 6                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 File Structure

### **1. app.py** (Main Application)

**Purpose:** Creates the web interface and handles user interactions

**Key Sections:**

- **Lines 1-12:** Imports and environment setup
- **Lines 14-22:** Page configuration
- **Lines 24-59:** Sidebar (API key input, model selection)
- **Lines 61-67:** Session state initialization (memory)
- **Lines 69-72:** Display chat history
- **Lines 74-120:** Main chat logic
- **Lines 122-136:** Instructions and footer

### **2. agents.py** (Agent Definition)

**Purpose:** Defines how to create the Mom Agent

**Key Sections:**

- **Lines 1-6:** Imports
- **Lines 9-57:** `create_mom_agent()` function
  - Lines 23-40: System message (mom's personality)
  - Lines 43-47: Create OpenAI client
  - Lines 49-53: Create AssistantAgent
  - Line 56: Return the agent

---

## 🔑 Key Concepts

### **1. Session State**

Streamlit re-runs the entire script on every interaction. Session state allows us to persist data:

```python
st.session_state.messages = []  # Remembers chat history
st.session_state.mom_agent = ...  # Remembers the agent
```

### **2. Agent Creation (agents.py)**

```python
# Step 1: Create OpenAI client
model_client = OpenAIChatCompletionClient(
    model="gpt-3.5-turbo",
    api_key=api_key,
    temperature=0.7  # Creativity level
)

# Step 2: Create agent with personality
mom_agent = AssistantAgent(
    name="Mom",
    system_message="You are a 35-year-old Indian mother...",
    model_client=model_client
)
```

### **3. Async Communication**

AutoGen's new API uses async (asynchronous) functions:

```python
# Create async function
async def get_response():
    response = await mom_agent.on_messages([TextMessage(...)])
    return response.chat_message.content

# Run it with asyncio
loop = asyncio.new_event_loop()
response = loop.run_until_complete(get_response())
```

---

## 🎮 User Journey Example

```
1. USER opens browser → sees Streamlit app

2. USER enters API key in sidebar

3. USER types: "I want to play video games"

4. APP checks: Is agent created? NO
   ├─ Calls create_mom_agent(api_key, "gpt-3.5-turbo")
   ├─ agents.py creates OpenAI client
   ├─ agents.py creates AssistantAgent with mom personality
   └─ Returns mom_agent to app.py

5. APP sends message to mom_agent
   ├─ mom_agent sends to OpenAI API
   ├─ OpenAI uses system message (mom personality)
   ├─ OpenAI generates response
   └─ Returns: "Beta, I know games are fun but..."

6. APP displays mom's response

7. USER types another message

8. APP checks: Is agent created? YES (skip step 4)

9. APP sends new message to existing mom_agent

10. Repeat...
```

---

## 🧩 Component Breakdown

### **Components in app.py:**

1. **Import Section** (Lines 1-9)
   - Libraries needed for the app

2. **Page Setup** (Lines 14-22)
   - Title, icon, layout

3. **Configuration UI** (Lines 24-59)
   - Where user inputs API key
   - Where user selects model

4. **Memory Management** (Lines 61-67)
   - Tracks conversation history
   - Tracks if agent is initialized

5. **Display Logic** (Lines 69-72)
   - Shows all previous messages

6. **Chat Logic** (Lines 74-120)
   - Handles user input
   - Creates agent (first time)
   - Gets AI response
   - Displays response

### **Components in agents.py:**

1. **Imports** (Lines 1-6)
   - AutoGen classes needed

2. **create_mom_agent() Function** (Lines 9-57)
   - **Input:** API key, model name
   - **Process:**
     - Define mom personality (system_message)
     - Create OpenAI client
     - Create AssistantAgent
   - **Output:** Configured mom agent

---

## 🚀 How to Run

### **Prerequisites:**

```powershell
# 1. Create virtual environment
python -m venv .venv

# 2. Activate it
.venv\Scripts\activate.ps1

# 3. Install packages
pip install -r requirements.txt
```

### **Run the app:**

```powershell
streamlit run app.py
```

### **What happens:**

1. Browser opens to http://localhost:8501
2. You see the Streamlit interface
3. Enter your OpenAI API key
4. Start chatting with Mom Agent!

---

## 🔧 Customization Points

### **To change Mom's personality:**

Edit `system_message` in `agents.py` (Lines 23-40)

### **To add more agents:**

Create new functions in `agents.py`:

```python
def create_son_agent(api_key, model):
    # Similar structure, different personality
    pass
```

### **To change UI:**

Edit `app.py` sidebar section (Lines 24-59)

---

## 🐛 Common Issues

### **"No module named autogen"**

- Solution: Run `pip install -r requirements.txt`

### **"API key not found"**

- Solution: Enter API key in sidebar OR create `.env` file

### **Agent not responding**

- Check: Is API key valid?
- Check: Do you have OpenAI credits?

---

## 📚 Next Steps

1. **Step 2:** Add Son Agent
2. **Step 3:** Add Teacher Agent
3. **Step 4:** Add Friend Agent
4. **Step 5:** Multi-agent group chat

---

## 💡 Key Takeaways

1. **app.py** = User Interface (Streamlit)
2. **agents.py** = Agent Definitions (AutoGen)
3. **Session State** = Memory between interactions
4. **Async** = Modern way to handle AI responses
5. **System Message** = Defines agent personality
