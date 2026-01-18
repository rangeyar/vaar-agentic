"""
Streamlit application for multi-agent chat
"""
import streamlit as st
import os
from dotenv import load_dotenv
import asyncio
from autogen_agentchat.messages import TextMessage
from agents import create_mom_agent, create_arvashu_agent
from group_chat import GroupChatManager, run_mom_arvashu_conversation

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Multi-Agent Chat Application",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Multi-Agent Chat Application")
st.subheader("Step 3: Group Chat - Mom & Arvashu")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API Key input
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
        help="Enter your OpenAI API key"
    )
    
    # Model selection
    model = st.selectbox(
        "Select Model",
        ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"],
        help="Choose the OpenAI model to use"
    )
    
    st.divider()
    
    # Chat mode selection
    st.header("💬 Chat Mode")
    chat_mode = st.radio(
        "Select Mode:",
        ["Single Chat", "Group Chat"],
        help="Single: Chat with one agent. Group: Watch agents talk to each other."
    )
    
    st.divider()
    
    # Agent information
    if chat_mode == "Single Chat":
        st.header("👩 Mom Agent")
        st.write("""
        **Role:** 35-year-old mother
        
        **Characteristics:**
        - Caring but firm
        - Wants son to study more
        - Concerned about screen time
        """)
    else:
        st.header("🎭 Group Chat")
        st.write("""
        **Participants:**
        - 👩 **Mom**: Concerned about studies
        - 👦 **Arvashu**: 9yo, loves games
        
        **Rounds:** 4 back-and-forth messages
        """)
    
    st.divider()
    
    # Group chat settings
    if chat_mode == "Group Chat":
        st.header("⚙️ Group Chat Settings")
        conversation_rounds = st.slider(
            "Conversation Rounds",
            min_value=2,
            max_value=8,
            value=4,
            help="Number of back-and-forth exchanges"
        )

# Main chat interface
if chat_mode == "Single Chat":
    st.header("💬 Chat with Mom Agent")
else:
    st.header("🎭 Group Chat: Mom & Arvashu Conversation")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent_initialized" not in st.session_state:
    st.session_state.agent_initialized = False

if "group_conversation" not in st.session_state:
    st.session_state.group_conversation = []

# SINGLE CHAT MODE
if chat_mode == "Single Chat":
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if api_key:
        user_input = st.chat_input("Type your message here...")
        
        if user_input:
            # Display user message
            with st.chat_message("user"):
                st.write(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Initialize agent if not already done
            if not st.session_state.agent_initialized:
                with st.spinner("Initializing Mom Agent..."):
                    try:
                        st.session_state.mom_agent = create_mom_agent(api_key, model)
                        st.session_state.agent_initialized = True
                    except Exception as e:
                        st.error(f"Error initializing agent: {str(e)}")
                        st.stop()
            
            # Get response from Mom agent
            with st.chat_message("assistant"):
                with st.spinner("Mom is typing..."):
                    try:
                        # Run the async function synchronously
                        async def get_response():
                            response = await st.session_state.mom_agent.on_messages(
                                [TextMessage(content=user_input, source="user")],
                                cancellation_token=None
                            )
                            return response.chat_message.content
                        
                        # Get response
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        response = loop.run_until_complete(get_response())
                        loop.close()
                        
                        st.write(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        
                    except Exception as e:
                        st.error(f"Error getting response: {str(e)}")
                        st.write("Sorry beta, I'm having trouble responding right now.")
    else:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar to start chatting.")

# GROUP CHAT MODE
else:
    if api_key:
        # Topic input
        st.write("**Enter a topic for Mom and Arvashu to discuss:**")
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            topic_input = st.text_input(
                "Conversation Topic",
                placeholder="e.g., 'Arvashu needs to finish his homework' or 'Too much video game time'",
                label_visibility="collapsed"
            )
        
        with col2:
            start_button = st.button("🎬 Start Chat", use_container_width=True)
        
        # Predefined topics
        st.write("**Or choose a preset topic:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📚 Homework Discussion"):
                topic_input = "Mom wants Arvashu to finish his homework but he wants to play games"
                start_button = True
        
        with col2:
            if st.button("🎮 Screen Time Limit"):
                topic_input = "Mom is concerned about Arvashu's excessive screen time and gaming"
                start_button = True
        
        with col3:
            if st.button("📖 Study for Exam"):
                topic_input = "Arvashu has an exam tomorrow but he's watching YouTube instead of studying"
                start_button = True
        
        # Start conversation
        if start_button and topic_input:
            with st.spinner("Initializing agents and starting conversation..."):
                try:
                    # Initialize agents if needed
                    if "mom_agent" not in st.session_state:
                        st.session_state.mom_agent = create_mom_agent(api_key, model)
                    
                    if "arvashu_agent" not in st.session_state:
                        st.session_state.arvashu_agent = create_arvashu_agent(api_key, model)
                    
                    # Run conversation
                    async def run_conversation():
                        return await run_mom_arvashu_conversation(
                            st.session_state.mom_agent,
                            st.session_state.arvashu_agent,
                            topic=topic_input,
                            rounds=conversation_rounds
                        )
                    
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    st.session_state.group_conversation = loop.run_until_complete(run_conversation())
                    loop.close()
                    
                    st.success(f"✅ Conversation completed! ({conversation_rounds} rounds)")
                    
                except Exception as e:
                    st.error(f"Error during conversation: {str(e)}")
        
        # Display conversation
        if st.session_state.group_conversation:
            st.divider()
            st.subheader("💬 Conversation:")
            
            for msg in st.session_state.group_conversation:
                agent_name = msg["agent"]
                agent_emoji = "👩" if agent_name == "Mom" else "👦"
                
                with st.chat_message("assistant", avatar=agent_emoji):
                    st.markdown(f"**{agent_emoji} {agent_name}** (Round {msg['round']}):")
                    st.write(msg["message"])
            
            # Clear button
            if st.button("🗑️ Clear Conversation"):
                st.session_state.group_conversation = []
                st.rerun()
        
        elif not topic_input and start_button:
            st.warning("⚠️ Please enter a topic or choose a preset topic.")
    
    else:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar to start the group chat.")

# Footer
st.divider()
st.caption("Multi-Agent Chat Application - Step 3: Group Chat | Built with AutoGen, Streamlit, and OpenAI")
