import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
  index("routes/home.tsx"),
  route("executions", "pages/executions.tsx"),
  route("automations", "pages/automations.tsx"),
  route("dashboard", "pages/dashboard.tsx"),
  route("metrics", "pages/metrics.tsx"),
  route("runners", "pages/runners.tsx"),
  route("settings", "pages/settings.tsx"),
  route("logs", "pages/logs.tsx"),
] satisfies RouteConfig;
