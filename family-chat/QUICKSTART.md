# 🚀 QUICK START GUIDE

## ⚡ Get Started in 3 Steps:

### **1. Activate Virtual Environment**

```powershell
.venv\Scripts\activate
```

### **2. Make Sure API Key is Set**

Check your `.env` file has:

```
OPENAI_API_KEY=sk-your-key-here
```

### **3. Run the App**

```powershell
streamlit run app.py
```

---

## 🎯 What You'll See:

### **Sidebar (Left):**

- 🔑 API Key input
- 🤖 Model selector
- 💬 **Mode Selector** ← Choose here!
  - Single Chat
  - Group Chat

---

## 💬 MODE 1: SINGLE CHAT

**Use this to:** Chat directly with Mom agent

**Steps:**

1. Select "Single Chat" in sidebar
2. Type your message at bottom
3. Get response from Mom
4. Continue chatting

**Try asking:**

- "Should I study or play games?"
- "Why do I need to do homework?"
- "All my friends play games"

---

## 🎭 MODE 2: GROUP CHAT (THE COOL ONE!)

**Use this to:** Watch Mom and Arvashu argue about studying!

**Steps:**

1. Select "Group Chat" in sidebar
2. Adjust rounds if needed (default: 4)
3. **Either:**
   - Type your own topic, OR
   - Click a preset button:
     - 📚 Homework Discussion
     - 🎮 Screen Time Limit
     - 📖 Study for Exam
4. Click "🎬 Start Chat"
5. Watch the conversation unfold! 🍿

**Example Topics:**

- "Arvashu should clean his room"
- "Bedtime but gaming"
- "Too much YouTube"
- "Need to read books"

---

## 🧪 TEST WITHOUT UI:

```powershell
python test_agents.py
```

This will:

- ✅ Test Mom agent
- ✅ Test Arvashu agent
- ✅ Run a sample 4-round group chat

---

## 📊 WHAT HAPPENS IN GROUP CHAT:

```
You enter: "Homework vs Gaming"
    ↓
👩 Mom (Round 1): "Beta, finish your homework..."
    ↓
👦 Arvashu (Round 2): "Just 5 more minutes, Mom!"
    ↓
👩 Mom (Round 3): "You said that an hour ago!"
    ↓
👦 Arvashu (Round 4): "But my friend doesn't have to!"
    ↓
✅ Conversation Complete!
```

---

## 🎨 PRESET TOPICS EXPLAINED:

### **📚 Homework Discussion**

Mom wants homework done → Arvashu wants games

- Expect: Excuses, negotiation, firm responses

### **🎮 Screen Time Limit**

Too much gaming → Health concerns

- Expect: Health talk, time limits, protests

### **📖 Study for Exam**

Exam tomorrow → YouTube instead

- Expect: Urgency, last-minute panic, promises

---

## ⚙️ SETTINGS:

### **Conversation Rounds:**

- **2 rounds:** Quick exchange
- **4 rounds:** Balanced (recommended)
- **6-8 rounds:** Deep conversation

### **Models:**

- **gpt-3.5-turbo:** Fast, cheap ✅
- **gpt-4:** Better quality, slower
- **gpt-4-turbo:** Best balance

---

## 🐛 TROUBLESHOOTING:

### **"Module not found"**

```powershell
pip install -r requirements.txt
```

### **"API key error"**

Check `.env` file has valid key

### **"Import error"**

Make sure venv is activated:

```powershell
.venv\Scripts\activate
```

---

## 📝 FILE REFERENCE:

| File                      | Purpose            |
| ------------------------- | ------------------ |
| `app.py`                  | Main Streamlit app |
| `group_chat.py`           | Group chat logic   |
| `agents/mom_agent.py`     | Mom agent          |
| `agents/arvashu_agent.py` | Arvashu agent      |
| `test_agents.py`          | Quick test         |

---

## 💡 TIPS:

✅ **Start with presets** - Click preset buttons first  
✅ **Try 4 rounds** - Good balance of conversation  
✅ **Watch patterns** - See how agents respond  
✅ **Custom topics** - Get creative!  
✅ **Clear often** - Reset between topics

---

## 🎯 RECOMMENDED FLOW:

**First Time:**

1. Run `python test_agents.py` to verify setup
2. Run `streamlit run app.py`
3. Try Single Chat first (get familiar)
4. Switch to Group Chat
5. Try all 3 preset topics
6. Create your own topics!

---

## 🎭 FUN TOPICS TO TRY:

- "Arvashu wants pizza, Mom wants healthy food"
- "New game console vs saving money"
- "Going to friend's house vs studying"
- "Weekend plans - gaming vs outdoor"
- "Bedtime routine discussion"
- "Report card came today"

---

## ⏱️ ESTIMATED TIME:

- Setup: 2 minutes
- First test: 1 minute
- Single chat: 2-5 minutes
- Group chat: 1-2 minutes per conversation
- Playing around: Hours of fun! 🎉

---

## 🚀 READY?

```powershell
# Let's go!
.venv\Scripts\activate
streamlit run app.py
```

**Then click "Group Chat" and "📚 Homework Discussion"!**

Enjoy watching Mom and Arvashu argue! 🎭😄

---

**Questions? Check:** `PROJECT_COMPLETE.md` for full details!
