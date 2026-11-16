import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// `@/lib` son las tablas que el portal publica y `@/components` sus componentes: grabar.mjs los trae a src/lib y src/portal.
const AQUI = path.dirname(fileURLToPath(import.meta.url));
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      '@/lib': path.join(AQUI, 'src', 'lib'),
      '@/components/agents': path.join(AQUI, 'src', 'portal'),
      '@/components/criterio': path.join(AQUI, 'src', 'portal'),
      // Lo que el componente del portal pide de Next y el video no usa.
      'next/head': path.join(AQUI, 'src', 'next', 'head.jsx'),
    },
  },
  // Los cuadros de cada grabación son miles de imágenes: vigilarlos agota el límite del sistema.
  server: { watch: { ignored: ['**/cuadros/**', '**/youtube/**', '**/uso/tomas/**'] } },
  logLevel: 'error',
});
