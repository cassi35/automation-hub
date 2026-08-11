import { defineConfig } from "orval";

export default defineConfig({
  api: {
    input: "http://0.0.0.0:8000/openapi.json",
    output: {
      target: "./app/api/generated.ts",
      client: "react-query",
      override: {
        mutator: {
          path: "./app/api/axios.ts",
          name: "api",
        },
      },
    },
  },
});
