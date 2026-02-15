"use client";

import { cn } from "@/src/lib/utils";
import {
  forwardRef,
  InputHTMLAttributes,
  TextareaHTMLAttributes,
} from "react";

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, label, error, ...props }, ref) => {
    return (
      <div className="w-full">
        {label && (
          <label className="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">
            {label}
          </label>
        )}

        <input
          ref={ref}
          className={cn(
            "w-full rounded-xl",
            "bg-[#f5f5f7] dark:bg-[#1c1c1e]",
            "border border-[#e5e5ea] dark:border-[#2c2c2e]",
            "px-4 py-3 text-sm",
            "text-zinc-900 dark:text-zinc-100",
            "placeholder:text-zinc-400 dark:placeholder:text-zinc-500",
            "transition-all duration-200",
            "focus:outline-none focus:ring-2 focus:ring-[#0071e3] dark:focus:ring-[#2997ff] focus:border-transparent",
            error &&
              "border-red-500 focus:ring-red-500",
            className
          )}
          {...props}
        />

        {error && (
          <p className="mt-2 text-sm text-red-500">
            {error}
          </p>
        )}
      </div>
    );
  }
);

Input.displayName = "Input";

interface TextareaProps
  extends TextareaHTMLAttributes<HTMLTextAreaElement> {
  label?: string;
  error?: string;
}

export const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(
  ({ className, label, error, ...props }, ref) => {
    return (
      <div className="w-full">
        {label && (
          <label className="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-2">
            {label}
          </label>
        )}

        <textarea
          ref={ref}
          className={cn(
            "w-full rounded-xl",
            "bg-[#f5f5f7] dark:bg-[#1c1c1e]",
            "border border-[#e5e5ea] dark:border-[#2c2c2e]",
            "px-4 py-3 text-sm",
            "text-zinc-900 dark:text-zinc-100",
            "placeholder:text-zinc-400 dark:placeholder:text-zinc-500",
            "transition-all duration-200",
            "focus:outline-none focus:ring-2 focus:ring-[#0071e3] dark:focus:ring-[#2997ff] focus:border-transparent",
            "resize-y min-h-[120px]",
            error &&
              "border-red-500 focus:ring-red-500",
            className
          )}
          {...props}
        />

        {error && (
          <p className="mt-2 text-sm text-red-500">
            {error}
          </p>
        )}
      </div>
    );
  }
);

Textarea.displayName = "Textarea";
