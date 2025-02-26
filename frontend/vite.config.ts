import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    port: 3000,
    strictPort: true,
    hmr: {
      clientPort: 443,
    },
    allowedHosts: [
      "localhost",
      "b61dab94-b73f-41d0-bc26-fda6c995fe66-00-frnrl3swvznd.janeway.replit.dev",
    ],
  },
});
