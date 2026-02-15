"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { isLoggedIn } from "@/src/lib/auth";
import { projects } from "@/src/lib/api";
import { Project, ProjectCreate, ProjectUpdate } from "@/src/types";
import { Input, Textarea } from "@/src/components/ui/Input";
import Button from "@/src/components/ui/Button";
import { Plus, Edit, Trash2, Save, Shield } from "lucide-react";

export default function AdminPanelPage() {
  const router = useRouter();
  const [activeTab, setActiveTab] =
    useState<"create" | "edit" | "delete">("create");

  const [projectList, setProjectList] = useState<Project[]>([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const [createForm, setCreateForm] = useState<ProjectCreate>({
    title: "",
    short_description: "",
    tech_stack: "",
    github_url: "",
    live_url: "",
  });

  const [selectedProject, setSelectedProject] = useState<Project | null>(null);
  const [editForm, setEditForm] = useState<ProjectUpdate>({});

  useEffect(() => {
    if (!isLoggedIn()) {
      router.push("/admin/login");
      return;
    }
    fetchProjects();
  }, [router]);

  const fetchProjects = async () => {
    try {
      const res = await projects.getAll();
      setProjectList(res.data);
    } catch {
      console.error("Failed to fetch projects");
    }
  };

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      await projects.create(createForm);
      setMessage("Project created successfully");
      setCreateForm({
        title: "",
        short_description: "",
        tech_stack: "",
        github_url: "",
        live_url: "",
      });
      fetchProjects();
    } catch {
      setMessage("Failed to create project");
    } finally {
      setLoading(false);
    }
  };

  const handleUpdate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedProject) return;

    setLoading(true);
    setMessage("");

    try {
      await projects.update(selectedProject.id, editForm);
      setMessage("Project updated successfully");
      fetchProjects();
    } catch {
      setMessage("Failed to update project");
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (!confirm("Are you sure you want to delete this project?")) return;

    setLoading(true);
    try {
      await projects.delete(id);
      setMessage("Project deleted successfully");
      fetchProjects();
    } catch {
      setMessage("Failed to delete project");
    } finally {
      setLoading(false);
    }
  };

  const loadProjectForEdit = (project: Project) => {
    setSelectedProject(project);
    setEditForm({
      title: project.title,
      short_description: project.short_description,
      problem_statement: project.problem_statement || "",
      why_built: project.why_built || "",
      architecture: project.architecture || "",
      implementation_details: project.implementation_details || "",
      challenges: project.challenges || "",
      learnings: project.learnings || "",
      future_improvements: project.future_improvements || "",
      tech_stack: project.tech_stack || "",
      github_url: project.github_url || "",
      live_url: project.live_url || "",
    });
  };

  const tabs = [
    { id: "create", label: "Create", icon: Plus },
    { id: "edit", label: "Edit", icon: Edit },
    { id: "delete", label: "Delete", icon: Trash2 },
  ] as const;

  return (
    <div className="min-h-screen bg-white dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 transition-colors duration-300">
      <div className="max-w-4xl mx-auto px-6 py-28">

        {/* Header */}
        <div className="mb-20">
          <div className="flex items-center gap-3 mb-4">
            <Shield size={22} />
            <h1 className="text-4xl font-light tracking-tight">
              Admin Dashboard
            </h1>
          </div>
          <p className="text-zinc-500 dark:text-zinc-400">
            Manage your portfolio projects
          </p>
        </div>

        {/* Tabs */}
        <div className="flex gap-10 mb-16 border-b border-zinc-200 dark:border-zinc-800">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center gap-2 pb-4 text-sm font-medium border-b-2 -mb-px transition ${
                activeTab === tab.id
                  ? "border-black dark:border-white"
                  : "border-transparent text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white"
              }`}
            >
              <tab.icon size={16} />
              {tab.label}
            </button>
          ))}
        </div>

        {/* Message */}
        {message && (
          <div className="mb-10 px-5 py-3 rounded-lg border border-zinc-300 dark:border-zinc-700 bg-zinc-100 dark:bg-zinc-800 text-sm text-zinc-700 dark:text-zinc-300">
            {message}
          </div>
        )}

        {/* CREATE */}
        {activeTab === "create" && (
          <Card title="Add New Project">
            <form onSubmit={handleCreate} className="space-y-6">
              <Input label="Title"
                value={createForm.title}
                onChange={(e) =>
                  setCreateForm({ ...createForm, title: e.target.value })
                }
                required
              />
              <Textarea
                label="Short Description"
                value={createForm.short_description}
                onChange={(e) =>
                  setCreateForm({
                    ...createForm,
                    short_description: e.target.value,
                  })
                }
                required
              />
              <Input
                label="Tech Stack (comma separated)"
                value={createForm.tech_stack}
                onChange={(e) =>
                  setCreateForm({ ...createForm, tech_stack: e.target.value })
                }
              />
              <Input
                label="GitHub URL"
                type="url"
                value={createForm.github_url}
                onChange={(e) =>
                  setCreateForm({ ...createForm, github_url: e.target.value })
                }
              />
              <Input
                label="Live URL"
                type="url"
                value={createForm.live_url}
                onChange={(e) =>
                  setCreateForm({ ...createForm, live_url: e.target.value })
                }
              />

              <Button type="submit" isLoading={loading} className="w-full rounded-full">
                <Plus size={16} />
                Create Project
              </Button>
            </form>
          </Card>
        )}

        {/* EDIT */}
        {activeTab === "edit" && (
          <div className="space-y-10">

            <Card title="Select Project to Edit">
              <select
                className="w-full px-4 py-3 rounded-xl border border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 text-sm focus:outline-none focus:ring-2 focus:ring-zinc-400 dark:focus:ring-zinc-600 transition"
                onChange={(e) => {
                  const project = projectList.find(
                    (p) => p.id === Number(e.target.value)
                  );
                  if (project) loadProjectForEdit(project);
                }}
                value={selectedProject?.id || ""}
              >
                <option value="">Choose a project...</option>
                {projectList.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.title}
                  </option>
                ))}
              </select>
            </Card>

            {selectedProject && (
              <Card title="Edit Project Details">
                <form onSubmit={handleUpdate} className="space-y-6">
                  {Object.keys(editForm).map((key) => (
                    <Textarea
                      key={key}
                      label={key.replace(/_/g, " ")}
                      value={(editForm as any)[key] || ""}
                      onChange={(e) =>
                        setEditForm({ ...editForm, [key]: e.target.value })
                      }
                    />
                  ))}

                  <Button type="submit" isLoading={loading} className="w-full rounded-full">
                    <Save size={16} />
                    Save Changes
                  </Button>
                </form>
              </Card>
            )}
          </div>
        )}

        {/* DELETE */}
        {activeTab === "delete" && (
          <Card title="Delete Project">
            <div className="space-y-6">
              {projectList.map((project) => (
                <div
                  key={project.id}
                  className="flex items-center justify-between p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-900 transition"
                >
                  <div>
                    <h3 className="font-medium mb-1">{project.title}</h3>
                    <p className="text-sm text-zinc-500 dark:text-zinc-400">
                      {project.short_description}
                    </p>
                  </div>
                  <Button
                    variant="danger"
                    size="sm"
                    onClick={() => handleDelete(project.id)}
                    isLoading={loading}
                  >
                    <Trash2 size={16} />
                    Delete
                  </Button>
                </div>
              ))}
            </div>
          </Card>
        )}

      </div>
    </div>
  );
}

/* Reusable Card */
function Card({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div className="rounded-2xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 shadow-sm p-10">
      <h2 className="text-xl font-medium mb-8">{title}</h2>
      {children}
    </div>
  );
}
