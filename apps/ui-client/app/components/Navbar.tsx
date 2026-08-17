import { NavLink } from "react-router";

function Navbar() {
  return (
    <aside className="fixed inset-y-0 left-0 z-50 w-56 border-r border-white/10 bg-[#11161d]">
      <nav className="flex h-full flex-col gap-1 p-3">
        <NavLink
          to="/dashboard"
          className={({ isActive }) =>
            `rounded-md px-3 py-2 text-sm ${
              isActive
                ? "bg-blue-600 text-white"
                : "text-slate-400 hover:bg-white/5 hover:text-white"
            }`
          }
        >
          Dashboard
        </NavLink>

        <NavLink
          to="/automations"
          className={({ isActive }) =>
            `rounded-md px-3 py-2 text-sm ${
              isActive
                ? "bg-blue-600 text-white"
                : "text-slate-400 hover:bg-white/5 hover:text-white"
            }`
          }
        >
          Automations
        </NavLink>

        <NavLink
          to="/executions"
          className={({ isActive }) =>
            `rounded-md px-3 py-2 text-sm ${
              isActive
                ? "bg-blue-600 text-white"
                : "text-slate-400 hover:bg-white/5 hover:text-white"
            }`
          }
        >
          Executions
        </NavLink>

        <NavLink
          to="/logs"
          className={({ isActive }) =>
            `rounded-md px-3 py-2 text-sm ${
              isActive
                ? "bg-blue-600 text-white"
                : "text-slate-400 hover:bg-white/5 hover:text-white"
            }`
          }
        >
          Logs
        </NavLink>

        <NavLink
          to="/metrics"
          className={({ isActive }) =>
            `rounded-md px-3 py-2 text-sm ${
              isActive
                ? "bg-blue-600 text-white"
                : "text-slate-400 hover:bg-white/5 hover:text-white"
            }`
          }
        >
          Metrics
        </NavLink>

        <NavLink
          to="/runners"
          className={({ isActive }) =>
            `rounded-md px-3 py-2 text-sm ${
              isActive
                ? "bg-blue-600 text-white"
                : "text-slate-400 hover:bg-white/5 hover:text-white"
            }`
          }
        >
          Runners
        </NavLink>

        <NavLink
          to="/settings"
          className={({ isActive }) =>
            `rounded-md px-3 py-2 text-sm ${
              isActive
                ? "bg-blue-600 text-white"
                : "text-slate-400 hover:bg-white/5 hover:text-white"
            }`
          }
        >
          Settings
        </NavLink>
      </nav>
    </aside>
  );
}

export default Navbar;
