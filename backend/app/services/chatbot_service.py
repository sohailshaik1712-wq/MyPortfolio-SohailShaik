"""
AI Chatbot Service
Handles chatbot functionality with tool calling for portfolio assistant
"""

import json
import os
from typing import Any, Dict, List, Optional

import requests
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionToolParam
from pypdf import PdfReader


class ChatbotService:
    def __init__(
        self, gemini_api_key: str, pushover_user: str = "", pushover_token: str = ""
    ):
        """Initialize chatbot service with OpenAI-compatible Gemini API"""
        self.client = OpenAI(
            api_key=gemini_api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )
        self.model_name = (
            "gemini-2.5-flash"  # Fixed: was "gemini-2.5-flash" which doesn't exist
        )
        self.pushover_user = pushover_user
        self.pushover_token = pushover_token
        self.pushover_url = "https://api.pushover.net/1/messages.json"

        # Professional Identity
        self.name = "Sohail Shaik"
        self.title = "Data Platform Engineer"
        self.company = "Tata Consultancy Services"

        # Load portfolio context and tools
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        resume_path = os.path.join(base_dir, "resources", "resume.pdf")
        summary_path = os.path.join(base_dir, "resources", "summary.txt")
        summary = ""
        resume = ""
        try:
            if os.path.exists(resume_path):
                reader = PdfReader(resume_path)
                resume = "".join([p.extract_text() or "" for p in reader.pages])
        except Exception as e:
            print(f"Resume read error: {e}")

        try:
            if os.path.exists(summary_path):
                with open(summary_path, "r", encoding="utf-8") as f:
                    summary = f.read()
        except Exception as e:
            print(f"Summary read error: {e}")

        name = "Sohail Shaik"
        self.system_prompt = self._build_system_prompt(
            name=name, summary=summary, resume=resume
        )
        # tools list needs to be cast for the OpenAI SDK type checker
        self.tools: List[ChatCompletionToolParam] = self._define_tools()  # type: ignore

    def _push_notification(self, message: str):
        """Send push notification via Pushover"""
        if self.pushover_user and self.pushover_token:
            try:
                payload = {
                    "user": self.pushover_user,
                    "token": self.pushover_token,
                    "message": message,
                }
                response = requests.post(self.pushover_url, data=payload, timeout=5)
                print(f"Pushover response: {response.status_code} {response.text}")
            except Exception as e:
                print(f"Push notification failed: {e}")
        else:
            print(
                f"Pushover skipped: user={bool(self.pushover_user)} token={bool(self.pushover_token)}"
            )

    def _record_user_details(
        self, email: str, name: str = "Not provided", notes: str = "Not provided"
    ):
        """Tool function: Record user contact information"""
        print(f"DEBUG tool called: record_user_details email={email} name={name}")
        self._push_notification(f"📧 New contact: {name} ({email})\nNotes: {notes}")
        return {"recorded": "ok", "message": "Thank you! I'll get back to you soon."}

    def _record_unknown_question(self, question: str):
        """Tool function: Record questions the AI couldn't answer"""
        print(f"DEBUG tool called: record_unknown_question question={question}")
        self._push_notification(f"❓ Unknown question: {question}")
        return {"recorded": "ok"}

    def _define_tools(self) -> List[Dict[str, Any]]:
        """Define schema for available tools"""
        return [
            {
                "type": "function",
                "function": {
                    "name": "record_user_details",
                    "description": "Call this when a user wants to connect, hire, or leave their contact details.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "email": {
                                "type": "string",
                                "description": "User email address",
                            },
                            "name": {"type": "string", "description": "User's name"},
                            "notes": {
                                "type": "string",
                                "description": "Context about why they want to connect",
                            },
                        },
                        "required": ["email"],
                        "additionalProperties": False,
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "record_unknown_question",
                    "description": "Call this if you are asked a specific technical or personal question about Sohail that is not in your context.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "question": {
                                "type": "string",
                                "description": "The unanswered question",
                            }
                        },
                        "required": ["question"],
                        "additionalProperties": False,
                    },
                },
            },
        ]

    def _build_system_prompt(self, name, summary, resume) -> str:
        system_prompt = f"You are acting as {name}. You are answering questions on {name}'s website, \
        particularly questions related to {name}'s career, background, skills and experience. \
        Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
        You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
        Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
        If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
        If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

        system_prompt += f"\n\n## Summary:\n{summary}\n\n## Resume:\n{resume}\n\n"
        system_prompt += f"With this context, please chat with the user, always staying in character as {name}."

        return system_prompt

    def _handle_tool_calls(self, tool_calls) -> List[Dict[str, Any]]:
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            print(f"DEBUG handling tool: {tool_name} args={arguments}")

            if tool_name == "record_user_details":
                result = self._record_user_details(**arguments)
            elif tool_name == "record_unknown_question":
                result = self._record_unknown_question(**arguments)
            else:
                result = {"error": "Unknown tool"}

            results.append(
                {
                    "role": "tool",
                    "content": json.dumps(result),
                    "tool_call_id": tool_call.id,
                }
            )
        return results

    def chat(self, message: str, history: Optional[List[Dict[str, str]]] = None) -> str:
        """Main chat entry point with tool loop"""
        safe_history = history if history is not None else []

        # Build message history for the API
        messages: List[ChatCompletionMessageParam] = [
            {"role": "system", "content": self.system_prompt}
        ]

        # Ensure history is strictly role/content to avoid Pydantic extra fields
        for msg in safe_history:
            if msg.get("role") in ["user", "assistant"]:
                messages.append({"role": msg["role"], "content": msg["content"]})  # type: ignore

        messages.append({"role": "user", "content": message})

        try:
            done = False
            final_response = "I'm having trouble processing that right now."

            while not done:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    tools=self.tools,  # type: ignore
                )

                choice = response.choices[0]
                message_obj = choice.message

                print(f"DEBUG finish_reason: {choice.finish_reason}")
                print(f"DEBUG tool_calls: {message_obj.tool_calls}")

                if choice.finish_reason == "tool_calls" and message_obj.tool_calls:
                    # Must append the assistant message that requested tool calls first
                    messages.append(message_obj)  # type: ignore

                    tool_results = self._handle_tool_calls(message_obj.tool_calls)
                    messages.extend(tool_results)  # type: ignore
                else:
                    final_response = (
                        message_obj.content or "I've processed your request."
                    )
                    done = True

            return final_response

        except Exception as e:
            print(f"OpenAI/Gemini Call Error: {e}")
            return f"Error: {str(e)}"
