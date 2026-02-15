export const isLoggedIn = (): boolean => {
  if (typeof window === "undefined") return false;
  return !!localStorage.getItem("token");
};

export const logout = (): void => {
  localStorage.removeItem("token");
};

export const setToken = (token: string): void => {
  localStorage.setItem("token", token);
};

export const getToken = (): string | null => {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("token");
};
