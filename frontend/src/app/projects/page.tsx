"use client";

import { useEffect, useState, useMemo } from "react";
import { projects } from "@/src/lib/api";
import { Project } from "@/src/types";
import ProjectCard from "@/src/components/ProjectCard";
import { Loader2, Search, X } from "lucide-react";

export default function ProjectsPage() {
  const [projectList, setProjectList] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [searchQuery, setSearchQuery] = useState("");
  const [selectedTech, setSelectedTech] = useState<string>("");
  const [sortBy, setSortBy] = useState<"date" | "title">("date");

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const res = await projects.getAll();
        setProjectList(res.data);
      } catch {
        setError("Failed to load projects");
      } finally {
        setLoading(false);
      }
    };

    fetchProjects();
  }, []);

  const allTechnologies = useMemo(() => {
    const techSet = new Set<string>();
    projectList.forEach((project) => {
      if (project.tech_stack) {
        project.tech_stack.split(",").forEach((tech) => {
          techSet.add(tech.trim());
        });
      }
    });
    return Array.from(techSet).sort();
  }, [projectList]);

  const filteredProjects = useMemo(() => {
    let filtered = [...projectList];

    if (searchQuery) {
      const query = searchQuery.toLowerCase();
      filtered = filtered.filter(
        (project) =>
          project.title.toLowerCase().includes(query) ||
          project.short_description.toLowerCase().includes(query) ||
          project.tech_stack?.toLowerCase().includes(query)
      );
    }

    if (selectedTech) {
      filtered = filtered.filter((project) =>
        project.tech_stack?.split(",").some((tech) => tech.trim() === selectedTech)
      );
    }

    filtered.sort((a, b) => {
      if (sortBy === "date") {
        return new Date(b.created_at).getTime() - new Date(a.created_at).getTime();
      } else {
        return a.title.localeCompare(b.title);
      }
    });

    return filtered;
  }, [projectList, searchQuery, selectedTech, sortBy]);

  const clearFilters = () => {
    setSearchQuery("");
    setSelectedTech("");
    setSortBy("date");
  };

  const hasActiveFilters = searchQuery || selectedTech || sortBy !== "date";

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Loader2 className="w-6 h-6 animate-spin text-[#a1a1a6]" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-[#6e6e73] dark:text-[#a1a1a6]">{error}</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen transition-colors duration-300">

      <div className="max-w-6xl mx-auto px-6 py-28">

        {/* Header */}
        <div className="mb-16">
          <h1 className="text-4xl font-light tracking-tight mb-4">
            Projects
          </h1>
          <p className="text-[#6e6e73] dark:text-[#a1a1a6]">
            {filteredProjects.length} of {projectList.length} project
            {projectList.length !== 1 ? "s" : ""}
          </p>
        </div>

        {/* Filters */}
        <div className="surface rounded-3xl p-8 mb-20 space-y-8">

          {/* Search */}
          <div className="relative">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-[#a1a1a6]" />
            <input
              type="text"
              placeholder="Search projects..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-11 pr-4 py-3 rounded-full bg-[#f5f5f7] dark:bg-[#2c2c2e] text-sm focus:outline-none focus:ring-2 focus:ring-[#0071e3] dark:focus:ring-[#2997ff] transition"
            />
          </div>

          {/* Filters Row */}
          <div className="grid sm:grid-cols-2 gap-6">

            <div>
              <label className="block text-sm text-[#6e6e73] dark:text-[#a1a1a6] mb-3">
                Technology
              </label>
              <select
                value={selectedTech}
                onChange={(e) => setSelectedTech(e.target.value)}
                className="w-full px-4 py-3 rounded-xl bg-[#f5f5f7] dark:bg-[#2c2c2e] text-sm focus:outline-none focus:ring-2 focus:ring-[#0071e3] dark:focus:ring-[#2997ff] transition"
              >
                <option value="">All Technologies</option>
                {allTechnologies.map((tech) => (
                  <option key={tech} value={tech}>
                    {tech}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-sm text-[#6e6e73] dark:text-[#a1a1a6] mb-3">
                Sort By
              </label>
              <select
                value={sortBy}
                onChange={(e) =>
                  setSortBy(e.target.value as "date" | "title")
                }
                className="w-full px-4 py-3 rounded-xl bg-[#f5f5f7] dark:bg-[#2c2c2e] text-sm focus:outline-none focus:ring-2 focus:ring-[#0071e3] dark:focus:ring-[#2997ff] transition"
              >
                <option value="date">Latest First</option>
                <option value="title">Title (A-Z)</option>
              </select>
            </div>

          </div>

          {hasActiveFilters && (
            <button
              onClick={clearFilters}
              className="inline-flex items-center gap-2 text-sm text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition"
            >
              <X size={14} />
              Clear all filters
            </button>
          )}
        </div>

        {/* Grid */}
        {filteredProjects.length > 0 ? (
          <div className="grid md:grid-cols-2 gap-12">
            {filteredProjects.map((project) => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
        ) : (
          <div className="text-center py-20">
            <p className="text-[#6e6e73] dark:text-[#a1a1a6] mb-6">
              No projects found
            </p>
            <button
              onClick={clearFilters}
              className="px-6 py-3 rounded-full border border-[#e5e5ea] dark:border-[#2c2c2e] text-sm hover:opacity-80 transition"
            >
              Clear filters
            </button>
          </div>
        )}

      </div>
    </div>
  );
}
