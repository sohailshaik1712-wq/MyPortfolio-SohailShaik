import axios from "axios";
import {
  Project,
  ProjectCreate,
  ProjectUpdate,
  LoginCredentials,
} from "../types";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const auth = {
  login: (credentials: LoginCredentials) => {
    const formData = new FormData();
    formData.append("username", credentials.username);
    formData.append("password", credentials.password);

    return api.post("/auth/login", formData, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
  },
};

export const projects = {
  getAll: () => api.get<Project[]>("/projects/"),
  getById: (id: number) => api.get<Project>(`/projects/${id}`),
  create: (data: ProjectCreate) => api.post<Project>("/projects/", data),
  update: (id: number, data: ProjectUpdate) =>
    api.patch<Project>(`/projects/${id}`, data),
  delete: (id: number) => api.delete(`/projects/${id}`),
};

export default api;
