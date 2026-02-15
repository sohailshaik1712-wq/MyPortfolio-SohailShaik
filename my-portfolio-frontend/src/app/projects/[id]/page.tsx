"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { projects } from "@/src/lib/api";
import { Project } from "@/src/types";
import {
  Loader2,
  Github,
  ExternalLink,
  ArrowLeft,
} from "lucide-react";

export default function ProjectDetailsPage() {
  const params = useParams();
  const [project, setProject] = useState<Project | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProject = async () => {
      try {
        const res = await projects.getById(Number(params.id));
        setProject(res.data);
      } catch {
        setError("Project not found");
      } finally {
        setLoading(false);
      }
    };

    if (params.id) fetchProject();
  }, [params.id]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Loader2 className="w-6 h-6 animate-spin text-[#a1a1a6]" />
      </div>
    );
  }

  if (error || !project) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center text-center px-6">
        <p className="text-[#6e6e73] dark:text-[#a1a1a6] mb-8">{error}</p>
        <Link
          href="/projects"
          className="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-[#e5e5ea] dark:border-[#2c2c2e] text-sm hover:opacity-80 transition"
        >
          <ArrowLeft size={16} />
          Back to Projects
        </Link>
      </div>
    );
  }

  const formatText = (text?: string) => {
    if (!text) return null;
    return text.split("\n").map((line, idx) => (
      <p key={idx} className="mb-5 leading-relaxed">
        {line}
      </p>
    ));
  };

  const techStack =
    project.tech_stack?.split(",").map((t) => t.trim()).filter(Boolean) || [];

  return (
    <div className="min-h-screen transition-colors duration-300">

      <div className="max-w-4xl mx-auto px-6 py-32">

        {/* Back Link */}
        <Link
          href="/projects"
          className="inline-flex items-center gap-2 text-sm text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition mb-20"
        >
          <ArrowLeft size={16} />
          Back to Projects
        </Link>

        {/* Header */}
        <div className="mb-24 pb-24 border-b border-[#e5e5ea] dark:border-[#2c2c2e]">

          <h1 className="text-5xl md:text-6xl font-light tracking-tight mb-10">
            {project.title}
          </h1>

          <p className="text-xl text-[#6e6e73] dark:text-[#a1a1a6] leading-relaxed mb-14">
            {project.short_description}
          </p>

          {/* Tech Stack */}
          {techStack.length > 0 && (
            <div className="mb-14">
              <p className="text-xs uppercase tracking-wide text-[#8e8e93] dark:text-[#a1a1a6] mb-6">
                Technologies
              </p>
              <div className="flex flex-wrap gap-x-8 gap-y-4 text-sm text-[#6e6e73] dark:text-[#a1a1a6]">
                {techStack.map((tech) => (
                  <span key={tech}>{tech}</span>
                ))}
              </div>
            </div>
          )}

          {/* Links */}
          <div className="flex flex-wrap gap-5">

            {project.github_url && (
              <a
                href={project.github_url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#0071e3] text-white text-sm font-medium hover:bg-[#0066cc] transition"
              >
                <Github size={16} />
                View Source
              </a>
            )}

            {project.live_url && (
              <a
                href={project.live_url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-[#e5e5ea] dark:border-[#2c2c2e] text-sm hover:opacity-80 transition"
              >
                <ExternalLink size={16} />
                Live Demo
              </a>
            )}

          </div>
        </div>

        {/* Content Sections */}
        <div className="space-y-28">

          {project.problem_statement && (
            <Section title="Problem Statement">
              {formatText(project.problem_statement)}
            </Section>
          )}

          {project.why_built && (
            <Section title="Why This Was Built">
              {formatText(project.why_built)}
            </Section>
          )}

          {project.architecture && (
            <Section title="Architecture">
              <div className="whitespace-pre-line leading-relaxed text-[#6e6e73] dark:text-[#a1a1a6]">
                {project.architecture}
              </div>
            </Section>
          )}

          {project.implementation_details && (
            <Section title="Implementation Details">
              <div className="whitespace-pre-line leading-relaxed text-[#6e6e73] dark:text-[#a1a1a6]">
                {project.implementation_details}
              </div>
            </Section>
          )}

          {project.challenges && (
            <Section title="Challenges Encountered">
              <div className="whitespace-pre-line leading-relaxed text-[#6e6e73] dark:text-[#a1a1a6]">
                {project.challenges}
              </div>
            </Section>
          )}

          {project.learnings && (
            <Section title="Key Learnings">
              <div className="whitespace-pre-line leading-relaxed text-[#6e6e73] dark:text-[#a1a1a6]">
                {project.learnings}
              </div>
            </Section>
          )}

          {project.future_improvements && (
            <Section title="Future Improvements">
              <div className="whitespace-pre-line leading-relaxed text-[#6e6e73] dark:text-[#a1a1a6]">
                {project.future_improvements}
              </div>
            </Section>
          )}

        </div>

        {/* Footer */}
        <div className="mt-32 pt-14 border-t border-[#e5e5ea] dark:border-[#2c2c2e]">
          <Link
            href="/projects"
            className="inline-flex items-center gap-2 text-sm text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition"
          >
            <ArrowLeft size={16} />
            Back to Projects
          </Link>
        </div>

      </div>
    </div>
  );
}

/* Reusable Section */
function Section({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <section>
      <h2 className="text-xs uppercase tracking-[0.2em] text-[#8e8e93] dark:text-[#a1a1a6] mb-8">
        {title}
      </h2>
      <div className="text-[#6e6e73] dark:text-[#a1a1a6] text-base leading-relaxed">
        {children}
      </div>
    </section>
  );
}
