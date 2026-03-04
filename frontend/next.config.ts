/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: "standalone",

  // Fix cross-origin warning (optional)
  experimental: {
    allowedDevOrigins: ["localhost:3000", "127.0.0.1:3000", "192.168.0.5:3000"],
  },

  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: `${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/:path*`,
        // Changed from 8080 to 8000 ^^^^
      },
    ];
  },
};

module.exports = nextConfig;
