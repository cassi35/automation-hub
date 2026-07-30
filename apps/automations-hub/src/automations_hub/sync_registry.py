import importlib
from pathlib import Path
from automations_hub.infra.automation_repository import AutomationRepository


def find_workspace_root(start: Path) -> Path:
    current = start
    while current != current.parent:
        if (current / "pyproject.toml").exists() and "packages" in [
            p.name for p in current.iterdir() if p.is_dir()
        ]:
            return current
        current = current.parent
    raise RuntimeError("workspace root não encontrado")


def sync_all_manifests() -> None:
    repo = AutomationRepository()
    root = find_workspace_root(Path(__file__).resolve())
    packages_dir = root / "packages"
    print("PACKAGES:", packages_dir)

    for pkg_path in packages_dir.iterdir():
        if not pkg_path.is_dir():
            continue

        module_name = pkg_path.name.replace("-", "_") + ".manifest"
        print("TESTANDO:", pkg_path.name)

        try:
            mod = importlib.import_module(module_name)
            print("MANIFEST ENCONTRADO:", mod.manifest.slug)
            repo.upsert_automation(mod.manifest)
        except ModuleNotFoundError as e:
            if e.name == module_name:
                print(f"SEM MANIFEST: {pkg_path.name} (esperado se não for automação)")
            else:
                print(f"ERRO DENTRO DO MANIFEST de {pkg_path.name}: faltou '{e.name}'")
                raise
