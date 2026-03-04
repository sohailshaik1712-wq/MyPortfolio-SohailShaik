"use client";

import { useState, useRef, useEffect } from "react";
import { chatbot } from "../lib/api";

interface Message {
  role: "user" | "assistant";
  content: string;
}

export default function Chatbot() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "Hey! I'm Sohail. I've built this AI version of myself to answer questions about my work. Feel free to ask about my experience at TCS, my MDM projects, or how we can collaborate!",
    },
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const scrollContainerRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    if (scrollContainerRef.current) {
      const { scrollHeight, clientHeight } = scrollContainerRef.current;
      scrollContainerRef.current.scrollTo({
        top: scrollHeight - clientHeight,
        behavior: "smooth",
      });
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage: Message = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const response = await chatbot.chat(input, messages);

      const assistantMessage: Message = {
        role: "assistant",
        content: response.data.response,
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error("Chat error:", error);
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Sorry about that! I hit a snag. Could you try asking that again?",
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const exampleQuestions = [
    "What's your experience with MDM?",
    "Tell me about your projects at TCS",
    "What technical tools do you use daily?",
    "How can I get in touch with you?",
  ];

  return (
    <div className="flex flex-col h-[600px] max-w-2xl mx-auto border border-black/10 dark:border-white/10 rounded-3xl shadow-2xl bg-white dark:bg-[#1C1C1E] text-black dark:text-white overflow-hidden font-sans transition-colors duration-300">
      {/* Apple Style Header */}
      <div className="bg-gray-50/80 dark:bg-[#2C2C2E]/80 backdrop-blur-md p-5 shrink-0 border-b border-black/5 dark:border-white/5">
        <div className="flex items-center space-x-4">
          <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center shadow-lg shadow-blue-500/20">
            <span className="text-2xl">👤</span>
          </div>
          <div>
            <h2 className="text-lg font-semibold tracking-tight text-gray-900 dark:text-white">
              Shaik Sohail
            </h2>
            <div className="flex items-center space-x-2">
              <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
              <p className="text-xs text-gray-500 dark:text-gray-400 font-medium uppercase tracking-widest">
                Online
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Messages Container */}
      <div
        ref={scrollContainerRef}
        className="flex-1 overflow-y-auto p-6 space-y-6 scroll-smooth bg-white dark:bg-[#1C1C1E]"
      >
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[80%] px-4 py-3 rounded-[20px] shadow-sm ${
                message.role === "user"
                  ? "bg-blue-600 text-white rounded-tr-md"
                  : "bg-gray-100 dark:bg-[#2C2C2E] text-gray-800 dark:text-[#E5E5E7] rounded-tl-md"
              }`}
            >
              <p className="whitespace-pre-wrap text-[15px] leading-relaxed">
                {message.content}
              </p>
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-100 dark:bg-[#2C2C2E] px-4 py-4 rounded-[20px] rounded-tl-md">
              <div className="flex space-x-1.5">
                <div className="w-1.5 h-1.5 bg-gray-400 dark:bg-gray-500 rounded-full animate-bounce"></div>
                <div className="w-1.5 h-1.5 bg-gray-400 dark:bg-gray-500 rounded-full animate-bounce [animation-delay:0.2s]"></div>
                <div className="w-1.5 h-1.5 bg-gray-400 dark:bg-gray-500 rounded-full animate-bounce [animation-delay:0.4s]"></div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Quick Actions */}
      {messages.length === 1 && (
        <div className="px-6 pb-4 bg-white dark:bg-[#1C1C1E]">
          <div className="flex flex-wrap gap-2">
            {exampleQuestions.map((question, index) => (
              <button
                key={index}
                onClick={() => setInput(question)}
                className="text-[13px] bg-gray-100 hover:bg-gray-200 dark:bg-[#2C2C2E] dark:hover:bg-[#3A3A3C] text-blue-600 dark:text-blue-400 border border-black/5 dark:border-white/5 px-4 py-2 rounded-full transition-all active:scale-95"
              >
                {question}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Input Area */}
      <div className="p-4 bg-white dark:bg-[#1C1C1E] border-t border-black/5 dark:border-white/5 shrink-0">
        <div className="flex items-center space-x-3 bg-gray-100 dark:bg-[#2C2C2E] rounded-full px-4 py-1.5 border border-black/5 dark:border-white/5 transition-all focus-within:border-blue-500/30">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="isn't sohail soo cool!!"
            disabled={isLoading}
            className="flex-1 bg-transparent py-2 text-gray-900 dark:text-white placeholder-gray-500 focus:outline-none focus:ring-0 border-none text-[15px]"
          />
          <button
            onClick={sendMessage}
            disabled={isLoading || !input.trim()}
            className="w-8 h-8 flex items-center justify-center bg-blue-600 text-white rounded-full hover:bg-blue-500 disabled:bg-gray-300 dark:disabled:bg-gray-700 disabled:text-gray-500 transition-all active:scale-90 shadow-lg shadow-blue-600/20"
          >
            <svg
              viewBox="0 0 24 24"
              className="w-5 h-5 fill-current"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" />
            </svg>
          </button>
        </div>
        <p className="text-[10px] text-gray-400 dark:text-gray-600 text-center mt-3 font-medium uppercase tracking-tighter">
          End-to-End Encrypted with Sohail
        </p>
      </div>
    </div>
  );
}
