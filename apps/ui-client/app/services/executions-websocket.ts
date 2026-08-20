export type ExecutionEvent = {
  type:
    | "execution.started"
    | "step.started"
    | "step.finished"
    | "execution.finished";
  execution_id: number;
  step_id?: number;
  step_name?: string;
  status: string;
};

export function connectExecutionWebSocket(
  onMessage: (event: ExecutionEvent) => void,
) {
  const automationHubUrl =
    import.meta.env.AUTOMATION_HUB ?? "http://localhost:8000";
  const websocketUrl = new URL("/api/0.1.0/ws/executions", automationHubUrl);
  websocketUrl.protocol = websocketUrl.protocol === "https:" ? "wss:" : "ws:";

  console.log("Creating execution WebSocket:", websocketUrl.href);
  const socket = new WebSocket(websocketUrl);

  socket.onopen = () => {
    console.log("Connected to automation-hub WebSocket");
  };

  socket.onmessage = (event) => {
    try {
      const data: ExecutionEvent = JSON.parse(event.data);

      console.info("Execution event received:", data);
      onMessage(data);
    } catch (error) {
      console.error("Invalid execution WebSocket message:", event.data, error);
    }
  };

  socket.onerror = (error) => {
    console.error("WebSocket error:", error);
  };

  socket.onclose = () => {
    console.log("CLOSING WEBSOCKET");
  };
  return socket;
}
