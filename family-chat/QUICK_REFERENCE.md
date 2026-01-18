# 🚀 Quick Reference Card

## 📁 New Structure:

```
agents/
├── __init__.py          → Imports all agents
├── mom_agent.py         → Mom (35 yo, concerned)
├── arvashu_agent.py     → Son (9 yo, gamer)
└── README.md            → Documentation
```

## 💻 Import Agents:

```python
from agents import create_mom_agent, create_arvashu_agent
```

## 🎭 Agents:

### Mom 👩

- **Age:** 35 | **Role:** Concerned mother
- **Goal:** Make son study
- **Temp:** 0.7

```python
mom = create_mom_agent(api_key, model="gpt-3.5-turbo")
```

### Arvashu 👦

- **Age:** 9 | **Role:** Playful son
- **Goal:** Play games, avoid studying
- **Temp:** 0.8

```python
arvashu = create_arvashu_agent(api_key, model="gpt-3.5-turbo")
```

## 🧪 Test:

```powershell
# Test both agents
python test_agents.py

# Run web app
streamlit run app.py
```

## 📝 Status:

- ✅ Step 1: Mom agent
- ✅ Step 2: Arvashu agent
- ⏳ Step 3: Agent conversations

## 🔑 Key Files:

- `agents/` → All agents
- `app.py` → Web interface
- `test_agents.py` → Quick test
- `SUMMARY.md` → Full details

---

**Next:** Make them talk to each other! 🎭
