import Link from "next/link";
import { Project } from "@/src/types";
import { Github, ExternalLink, ArrowRight } from "lucide-react";

interface ProjectCardProps {
  project: Project;
}

export default function ProjectCard({ project }: ProjectCardProps) {
  const techStack =
    project.tech_stack
      ?.split(",")
      .map((t) => t.trim())
      .filter(Boolean) || [];

  return (
    <div className="group surface rounded-2xl p-8 hover:shadow-lg transition-all duration-300">

      <div className="p-8">

        {/* Header */}
        <div className="mb-5">
          <h3 className="text-xl font-medium tracking-tight mb-2 transition group-hover:opacity-80">
            {project.title}
          </h3>

          <p className="text-sm text-zinc-500 dark:text-zinc-400">
            {new Date(project.created_at).toLocaleDateString("en-US", {
              year: "numeric",
              month: "long",
            })}
          </p>
        </div>

        {/* Description */}
        <p className="text-zinc-700 dark:text-zinc-400 mb-8 leading-relaxed line-clamp-3">
          {project.short_description}
        </p>

        {/* Tech Stack */}
        {techStack.length > 0 && (
          <div className="mb-8">
            <p className="text-xs uppercase tracking-wide text-zinc-500 dark:text-zinc-400 mb-3">
              Technologies
            </p>

            <div className="flex flex-wrap gap-x-4 gap-y-2 text-sm text-zinc-600 dark:text-zinc-400">
              {techStack.slice(0, 5).map((tech) => (
                <span key={tech}>{tech}</span>
              ))}

              {techStack.length > 5 && (
                <span className="text-zinc-400">
                  +{techStack.length - 5} more
                </span>
              )}
            </div>
          </div>
        )}

        {/* Actions */}
        <div className="flex items-center gap-4 pt-6 border-t border-zinc-200 dark:border-zinc-800">

          <Link
            href={`/projects/${project.id}`}
            className="flex items-center gap-2 text-sm font-medium hover:opacity-80 transition"
          >
            View Details
            <ArrowRight size={16} />
          </Link>

          <div className="flex items-center gap-5 ml-auto">
            {project.github_url && (
              <a
                href={project.github_url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white transition"
                aria-label="View source code"
              >
                <Github size={16} />
              </a>
            )}

            {project.live_url && (
              <a
                href={project.live_url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white transition"
                aria-label="View live demo"
              >
                <ExternalLink size={16} />
              </a>
            )}
          </div>

        </div>
      </div>
    </div>
  );
}
