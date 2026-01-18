"""
Group Chat Manager - Handles multi-agent conversations
"""
import asyncio
from typing import List, Dict
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage, ChatMessage
from autogen_agentchat.base import Response


class GroupChatManager:
    """
    Manages conversations between multiple agents
    """
    
    def __init__(self, agents: List[AssistantAgent]):
        """
        Initialize group chat with multiple agents
        
        Args:
            agents: List of AssistantAgent instances
        """
        self.agents = agents
        self.conversation_history: List[Dict[str, str]] = []
    
    async def start_conversation(
        self, 
        topic: str, 
        max_rounds: int = 4,
        starter_agent: AssistantAgent = None
    ) -> List[Dict[str, str]]:
        """
        Start a conversation between agents
        
        Args:
            topic: The topic to discuss
            max_rounds: Maximum number of conversation rounds
            starter_agent: Which agent starts (default: first agent)
            
        Returns:
            List of conversation messages with agent names and content
        """
        if not self.agents:
            raise ValueError("No agents provided for group chat")
        
        # Reset conversation history
        self.conversation_history = []
        
        # Determine starting agent
        current_agent_idx = 0
        if starter_agent:
            try:
                current_agent_idx = self.agents.index(starter_agent)
            except ValueError:
                pass  # Use default if not found
        
        # Initial message context
        current_message = topic
        
        # Conversation rounds
        for round_num in range(max_rounds):
            current_agent = self.agents[current_agent_idx]
            
            # Get response from current agent
            response = await current_agent.on_messages(
                [TextMessage(content=current_message, source="system")],
                cancellation_token=None
            )
            
            agent_response = response.chat_message.content
            
            # Store in history
            self.conversation_history.append({
                "agent": current_agent.name,
                "message": agent_response,
                "round": round_num + 1
            })
            
            # Prepare message for next agent
            current_message = agent_response
            
            # Switch to next agent (alternate between agents)
            current_agent_idx = (current_agent_idx + 1) % len(self.agents)
        
        return self.conversation_history
    
    def get_conversation_as_text(self) -> str:
        """
        Get the conversation history as formatted text
        
        Returns:
            Formatted conversation string
        """
        if not self.conversation_history:
            return "No conversation yet."
        
        text = []
        for msg in self.conversation_history:
            text.append(f"**{msg['agent']}** (Round {msg['round']}):\n{msg['message']}\n")
        
        return "\n".join(text)
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []


async def run_mom_arvashu_conversation(
    mom_agent: AssistantAgent,
    arvashu_agent: AssistantAgent,
    topic: str,
    rounds: int = 4
) -> List[Dict[str, str]]:
    """
    Convenience function to run a conversation between Mom and Arvashu
    
    Args:
        mom_agent: The mom agent instance
        arvashu_agent: The Arvashu agent instance
        topic: What they should discuss
        rounds: Number of conversation rounds (default: 4)
        
    Returns:
        List of conversation messages
    """
    manager = GroupChatManager([mom_agent, arvashu_agent])
    conversation = await manager.start_conversation(
        topic=topic,
        max_rounds=rounds,
        starter_agent=mom_agent  # Mom starts the conversation
    )
    return conversation
