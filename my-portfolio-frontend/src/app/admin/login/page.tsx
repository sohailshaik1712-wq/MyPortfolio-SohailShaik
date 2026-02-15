"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { auth } from "@/src/lib/api";
import { setToken } from "@/src/lib/auth";
import { Input } from "@/src/components/ui/Input";
import Button from "@/src/components/ui/Button";
import { Shield, Lock } from "lucide-react";

export default function AdminLoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await auth.login({ username, password });

      if (res.data && res.data.access_token) {
        setToken(res.data.access_token);
        router.push("/admin");
      } else {
        setError("Invalid response from server");
      }
    } catch (err: any) {
      setError(
        err?.response?.data?.detail ||
        err?.message ||
        "Invalid credentials"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-white dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 flex items-center justify-center px-6 transition-colors duration-300">
      <div className="w-full max-w-md">

        {/* Card */}
        <div className="rounded-2xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 shadow-sm p-10">

          {/* Header */}
          <div className="text-center mb-10">
            <div className="inline-flex items-center justify-center w-12 h-12 rounded-full border border-zinc-300 dark:border-zinc-700 mb-6">
              <Shield size={20} />
            </div>

            <h1 className="text-3xl font-light tracking-tight mb-3">
              Admin Login
            </h1>

            <p className="text-sm text-zinc-500 dark:text-zinc-400">
              Enter your credentials to access the admin panel
            </p>
          </div>

          {/* Error */}
          {error && (
            <div className="mb-6 px-4 py-3 rounded-lg border border-zinc-300 dark:border-zinc-700 bg-zinc-100 dark:bg-zinc-800 text-sm text-zinc-700 dark:text-zinc-300">
              {error}
            </div>
          )}

          {/* Form */}
          <form onSubmit={handleSubmit} className="space-y-6">

            <Input
              label="Username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              autoComplete="username"
            />

            <Input
              label="Password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              autoComplete="current-password"
            />

            <Button
              type="submit"
              variant="primary"
              className="w-full rounded-full"
              isLoading={loading}
            >
              <Lock size={16} />
              Login
            </Button>

          </form>

        </div>

      </div>
    </div>
  );
}
