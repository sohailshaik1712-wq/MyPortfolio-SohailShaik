export interface Project {
  id: number;
  title: string;
  short_description: string;
  tech_stack?: string;
  github_url?: string;
  live_url?: string;
  created_at: string;
  problem_statement?: string;
  why_built?: string;
  architecture?: string;
  implementation_details?: string;
  challenges?: string;
  learnings?: string;
  future_improvements?: string;
}

export interface ProjectCreate {
  title: string;
  short_description: string;
  tech_stack?: string;
  github_url?: string;
  live_url?: string;
}

export interface ProjectUpdate {
  title?: string;
  short_description?: string;
  problem_statement?: string;
  why_built?: string;
  architecture?: string;
  implementation_details?: string;
  challenges?: string;
  learnings?: string;
  future_improvements?: string;
  tech_stack?: string;
  github_url?: string;
  live_url?: string;
}

export interface LoginCredentials {
  username: string;
  password: string;
}
