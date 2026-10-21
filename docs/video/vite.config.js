import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// `@/lib` es la hoja que el portal publica; grabar.mjs la trae a src/lib.
const AQUI = path.dirname(fileURLToPath(import.meta.url));
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: { alias: { '@/lib': path.join(AQUI, 'src', 'lib') } },
  logLevel: 'error',
});
