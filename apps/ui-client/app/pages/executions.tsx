import { useEffect, useState } from "react";
import {
  connectExecutionWebSocket,
  type ExecutionEvent,
} from "~/services/executions-websocket";

type Step = {
  id: number;
  name: string;
  status: string;
};

type Execution = {
  id: number;
  status: string;
  steps: Step[];
};

function Executions() {
  const [execution, setExecution] = useState<Execution | null>(null);
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    const socket = connectExecutionWebSocket((event: ExecutionEvent) => {
      setExecution((current) => {
        switch (event.type) {
          case "execution.started":
            return {
              id: event.execution_id,
              status: event.status,
              steps: [],
            };

          case "step.started":
            if (!current) {
              return current;
            }

            return {
              ...current,
              steps: [
                ...current.steps,
                {
                  id: event.step_id!,
                  name: event.step_name!,
                  status: event.status,
                },
              ],
            };

          case "step.finished":
            if (!current) {
              return current;
            }

            return {
              ...current,
              steps: current.steps.map((step) =>
                step.id === event.step_id
                  ? {
                      ...step,
                      status: event.status,
                    }
                  : step,
              ),
            };

          case "execution.finished":
            if (!current) {
              return current;
            }

            return {
              ...current,
              status: event.status,
            };

          default:
            return current;
        }
      });
    });

    socket.addEventListener("open", () => setIsConnected(true));
    socket.addEventListener("close", () => setIsConnected(false));

    return () => {
      socket.close();
    };
  }, []);

  if (!execution) {
    return (
      <section>
        <p>WebSocket: {isConnected ? "connected" : "connecting..."}</p>
        <p>Waiting for execution...</p>
      </section>
    );
  }

  return (
    <section>
      <p>WebSocket: {isConnected ? "connected" : "disconnected"}</p>
      <h1>Execution #{execution.id}</h1>

      <p>Status: {execution.status}</p>

      <div>
        {execution.steps.map((step) => (
          <div key={step.id}>
            <strong>{step.name}</strong>

            <span>{step.status}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Executions;
