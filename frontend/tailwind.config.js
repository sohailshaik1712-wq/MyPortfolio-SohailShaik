/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",

  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],

  theme: {
    extend: {
      colors: {
        // Neutral Apple-style grayscale tokens
        surface: {
          light: "#ffffff",
          dark: "#09090b",   // zinc-950 equivalent
        },

        muted: {
          light: "#71717a",  // zinc-500
          dark: "#a1a1aa",   // zinc-400
        },

        border: {
          light: "#e4e4e7",  // zinc-200
          dark: "#27272a",   // zinc-800
        },
      },

      fontFamily: {
        sans: [
          "-apple-system",
          "BlinkMacSystemFont",
          "SF Pro Display",
          "Inter",
          "Segoe UI",
          "Roboto",
          "Helvetica Neue",
          "Arial",
          "sans-serif",
        ],
      },

      boxShadow: {
        subtle: "0 1px 2px rgba(0,0,0,0.05)",
        medium: "0 4px 12px rgba(0,0,0,0.08)",
      },

      borderRadius: {
        xl2: "1.25rem", // smoother Apple rounding
      },
    },
  },

  plugins: [],
};
