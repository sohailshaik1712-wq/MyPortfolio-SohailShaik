"use client";

import { useState, useRef, useEffect } from "react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { isLoggedIn, logout } from "@/src/lib/auth";
import { Menu, X, Shield, Moon, Sun } from "lucide-react";

export default function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [adminDropdownOpen, setAdminDropdownOpen] = useState(false);
  const [dark, setDark] = useState(false);

  const pathname = usePathname();
  const router = useRouter();
  const loggedIn = isLoggedIn();

  const navRef = useRef<HTMLDivElement>(null);
  const indicatorRef = useRef<HTMLSpanElement>(null);

  const navLinks = [
    { href: "/", label: "Home" },
    { href: "/projects", label: "Projects" },
  ];

  const handleLogout = () => {
    logout();
    setAdminDropdownOpen(false);
    router.push("/");
  };

  // ---- DARK MODE INIT ----
  useEffect(() => {
    const saved = localStorage.getItem("theme");

    if (saved) {
      const isDark = saved === "dark";
      setDark(isDark);
      document.documentElement.classList.toggle("dark", isDark);
    } else {
      const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      setDark(prefersDark);
      document.documentElement.classList.toggle("dark", prefersDark);
    }
  }, []);

  const toggleTheme = () => {
    const newTheme = !dark;
    setDark(newTheme);
    localStorage.setItem("theme", newTheme ? "dark" : "light");
    document.documentElement.classList.toggle("dark", newTheme);
  };

  // ---- Sliding underline ----
  useEffect(() => {
    const activeLink = navRef.current?.querySelector(
      `[data-active="true"]`
    ) as HTMLElement;

    if (activeLink && indicatorRef.current) {
      indicatorRef.current.style.width = `${activeLink.offsetWidth}px`;
      indicatorRef.current.style.left = `${activeLink.offsetLeft}px`;
    }
  }, [pathname]);

  return (
    <nav className="sticky top-0 z-50 backdrop-blur-2xl bg-white/60 dark:bg-[#0d0d0f]/60 border-b border-[#e5e5ea] dark:border-[#2c2c2e] transition-colors">
      <div className="max-w-6xl mx-auto px-6">
        <div className="flex items-center justify-between h-16">

          {/* Logo */}
          <Link
            href="/"
            className="text-lg font-medium tracking-tight hover:opacity-80 transition"
          >
            Sohail Shaik
          </Link>

          {/* Desktop Nav */}
          <div
            ref={navRef}
            className="hidden md:flex relative items-center gap-10"
          >
            {navLinks.map((link) => {
              const active = pathname === link.href;
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  data-active={active}
                  className={`relative text-sm font-medium transition transform ${
                    active
                      ? "text-[#0071e3] dark:text-[#2997ff]"
                      : "text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] hover:scale-105"
                  }`}
                >
                  {link.label}

                  {active && (
                    <span className="absolute inset-0 rounded-lg blur-md opacity-20 bg-[#2997ff] dark:opacity-30 -z-10 hidden dark:block" />
                  )}
                </Link>
              );
            })}

            <span
              ref={indicatorRef}
              className="absolute -bottom-2 h-[2px] bg-[#0071e3] dark:bg-[#2997ff] rounded-full transition-all duration-300 ease-out"
            />
          </div>

          {/* Right Controls */}
          <div className="hidden md:flex items-center gap-6">

            {/* Theme Toggle */}
            <button
              onClick={toggleTheme}
              className="text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition"
              aria-label="Toggle theme"
            >
              {dark ? <Sun size={18} /> : <Moon size={18} />}
            </button>

            {/* Admin/Auth */}
            {loggedIn ? (
              <div className="relative">
                <button
                  onClick={() => setAdminDropdownOpen(!adminDropdownOpen)}
                  className="flex items-center gap-2 text-sm font-medium text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition"
                >
                  <Shield size={14} />
                  Admin
                </button>

                {adminDropdownOpen && (
                  <>
                    <div
                      className="fixed inset-0 z-10"
                      onClick={() => setAdminDropdownOpen(false)}
                    />
                    <div className="absolute right-0 mt-3 w-48 rounded-xl border border-[#e5e5ea] dark:border-[#2c2c2e] bg-white dark:bg-[#1c1c1e] shadow-xl overflow-hidden z-20">

                      <Link
                        href="/admin"
                        onClick={() => setAdminDropdownOpen(false)}
                        className="block px-4 py-3 text-sm text-[#6e6e73] dark:text-[#a1a1a6] hover:bg-[#f2f2f5] dark:hover:bg-[#2c2c2e] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition"
                      >
                        Admin Panel
                      </Link>

                      <button
                        onClick={handleLogout}
                        className="w-full text-left px-4 py-3 text-sm text-[#6e6e73] dark:text-[#a1a1a6] hover:bg-[#f2f2f5] dark:hover:bg-[#2c2c2e] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition border-t border-[#e5e5ea] dark:border-[#2c2c2e]"
                      >
                        Logout
                      </button>
                    </div>
                  </>
                )}
              </div>
            ) : (
              <Link
                href="/admin/login"
                className="text-sm font-medium text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition"
              >
                Login
              </Link>
            )}
          </div>

          {/* Mobile Toggle */}
          <button
            className="md:hidden text-[#6e6e73] dark:text-[#a1a1a6] hover:text-[#0071e3] dark:hover:text-[#2997ff] transition"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
      </div>
    </nav>
  );
}
