import openai
import anthropic
import requests
import config
from typing import Optional

class AIModel:
    """Base class for AI models"""
    
    def __init__(self):
        self.max_tokens = config.MAX_TOKENS
        self.temperature = config.TEMPERATURE
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        raise NotImplementedError


class GPT4Model(AIModel):
    """OpenAI GPT-4 implementation"""
    
    def __init__(self):
        super().__init__()
        openai.api_key = config.OPENAI_API_KEY
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate response using GPT-4"""
        try:
            messages = []
            
            if context:
                messages.append({
                    "role": "system",
                    "content": f"You are a helpful GitHub assistant. Context:\n{context}"
                })
            else:
                messages.append({
                    "role": "system",
                    "content": "You are a helpful GitHub assistant specializing in code review, documentation, and general coding assistance."
                })
            
            messages.append({
                "role": "user",
                "content": prompt
            })
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"


class ClaudeModel(AIModel):
    """Anthropic Claude implementation"""
    
    def __init__(self):
        super().__init__()
        self.client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate response using Claude"""
        try:
            system_prompt = "You are a helpful GitHub assistant specializing in code review, documentation, and general coding assistance."
            
            if context:
                system_prompt += f"\n\nContext:\n{context}"
            
            message = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=self.max_tokens,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return message.content[0].text
        except Exception as e:
            return f"Error generating response: {str(e)}"


class LlamaModel(AIModel):
    """Local Llama model via Ollama"""
    
    def __init__(self):
        super().__init__()
        self.api_url = config.LLAMA_API_URL
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate response using local Llama model"""
        try:
            full_prompt = prompt
            if context:
                full_prompt = f"Context:\n{context}\n\nQuestion: {prompt}"
            
            response = requests.post(
                f"{self.api_url}/api/generate",
                json={
                    "model": "llama2",
                    "prompt": full_prompt,
                    "stream": False,
                    "temperature": self.temperature,
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json().get("response", "No response generated")
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error connecting to Llama API: {str(e)}"


def get_ai_model() -> AIModel:
    """Factory function to get the appropriate AI model"""
    model_type = config.AI_MODEL.lower()
    
    if model_type == "gpt-4":
        return GPT4Model()
    elif model_type == "claude":
        return ClaudeModel()
    elif model_type == "llama":
        return LlamaModel()
    else:
        raise ValueError(f"Unknown AI model: {model_type}")
