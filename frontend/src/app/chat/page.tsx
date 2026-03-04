import Chatbot from "@/src/components/chatbot";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";

export default function ChatPage() {
  return (
    <div className="min-h-screen transition-colors duration-300">
      {/* Hero Section */}
      <section className="border-b border-[#e5e5ea] dark:border-[#2c2c2e]">
        <div className="max-w-6xl mx-auto px-6 py-20">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-sm text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition mb-8"
          >
            <ArrowLeft size={16} />
            Back to Home
          </Link>

          <h1 className="text-5xl md:text-6xl font-light tracking-tight mb-6">
            Hey There!
          </h1>

          <p className="text-xl text-[#6e6e73] dark:text-[#a1a1a6] max-w-2xl">
            Chat with me to learn about my experience in data platform
            engineering, Master Data Management, technical skills, and current
            projects.
          </p>
        </div>
      </section>

      {/* Chatbot Section */}
      <section className="border-b border-[#e5e5ea] dark:border-[#2c2c2e]">
        <div className="max-w-6xl mx-auto px-6 py-20">
          <Chatbot />
        </div>
      </section>

      {/* Info Section */}
      <section className="border-b border-[#e5e5ea] dark:border-[#2c2c2e]">
        <div className="max-w-6xl mx-auto px-6 py-20">
          <div className="grid md:grid-cols-3 gap-12">
            <div>
              <h3 className="text-lg font-medium mb-4">What to Ask</h3>
              <ul className="space-y-3 text-[#6e6e73] dark:text-[#a1a1a6] text-sm">
                <li>• Data engineering experience</li>
                <li>• MDM and data governance projects</li>
                <li>• Technical skills and certifications</li>
                <li>• Current work at TCS</li>
                <li>• Career opportunities</li>
              </ul>
            </div>

            <div>
              <h3 className="text-lg font-medium mb-4">How It Works</h3>
              <p className="text-[#6e6e73] dark:text-[#a1a1a6] text-sm leading-relaxed">
                This AI assistant is powered by Gemini and trained on my
                professional background, experience, and skills. It can answer
                questions and help you connect with me for opportunities.
              </p>
            </div>

            <div>
              <h3 className="text-lg font-medium mb-4">Get in Touch</h3>
              <p className="text-[#6e6e73] dark:text-[#a1a1a6] text-sm leading-relaxed mb-4">
                Interested in discussing a project or opportunity? Share your
                email through the chat, and I'll get back to you promptly.
              </p>
              <a
                href="mailto:sohailshaik1712@gmail.com"
                className="text-sm text-[#0071e3] dark:text-[#2997ff] hover:underline"
              >
                Or email me directly →
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="border-b border-[#e5e5ea] dark:border-[#2c2c2e]">
        <div className="max-w-6xl mx-auto px-6 py-20">
          <h2 className="text-3xl font-light mb-12">Assistant Capabilities</h2>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <FeatureCard
              emoji="🎯"
              title="Context-Aware"
              description="Trained on my actual resume, projects, and experience"
            />
            <FeatureCard
              emoji="🔍"
              title="Smart Matching"
              description="Understands technical questions about data engineering"
            />
            <FeatureCard
              emoji="📧"
              title="Contact Collection"
              description="Can record your email for follow-up discussions"
            />
            <FeatureCard
              emoji="🚀"
              title="Always Learning"
              description="Tracks unknown questions to improve responses"
            />
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section>
        <div className="max-w-6xl mx-auto px-6 py-20 text-center">
          <h2 className="text-3xl font-light mb-6">Want to see my work?</h2>
          <p className="text-[#6e6e73] dark:text-[#a1a1a6] mb-10 max-w-xl mx-auto">
            Check out my projects to see what I've built in data engineering,
            MLOps, and full-stack development.
          </p>

          <div className="flex gap-4 justify-center">
            <Link
              href="/projects"
              className="px-8 py-3 bg-[#0071e3] text-white rounded-full text-sm font-medium hover:bg-[#0066cc] transition"
            >
              View Projects
            </Link>

            <a
              href="/Sohail-Shaik-Resume.pdf"
              target="_blank"
              className="px-8 py-3 rounded-full border border-[#e5e5ea] dark:border-[#2c2c2e] text-sm hover:opacity-80 transition"
            >
              Download Resume
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}

function FeatureCard({
  emoji,
  title,
  description,
}: {
  emoji: string;
  title: string;
  description: string;
}) {
  return (
    <div className="text-center">
      <div className="text-4xl mb-4">{emoji}</div>
      <h3 className="font-medium mb-2">{title}</h3>
      <p className="text-sm text-[#6e6e73] dark:text-[#a1a1a6]">
        {description}
      </p>
    </div>
  );
}
