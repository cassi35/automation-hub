import { useListAutomations } from "~/api/generated";
import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "New React Router App" },
    { name: "description", content: "Welcome to React Router!" },
  ];
}

export default function Home() {
  const { data, isLoading, isError } = useListAutomations();

  if (isLoading) return <p>Carregando...</p>;
  if (isError) return <p>Erro ao carregar automações.</p>;
  console.log(data?.data);
  return (
    <div>
      {data?.data.map((automation) => (
        <div key={automation.id}>slug: {automation.slug}</div>
      ))}
    </div>
  );
}
