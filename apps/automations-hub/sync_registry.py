import importlib
from pathlib import Path
from automations_hub.infra.automation_repository import AutomationRepository
def sync_all_manifests() -> None:
    repo = AutomationRepository()

    packages_dir = (
        Path(__file__).parent.parent.parent / "packages"
    )
    print("PACKAGES:", packages_dir)

    for pkg_path in packages_dir.iterdir():

        if not pkg_path.is_dir():
            continue

        print("TESTANDO:", pkg_path.name)

        module_name = pkg_path.name.replace("-", "_") + ".manifest"

        try:
            print("IMPORTANDO:", module_name)

            mod = importlib.import_module(module_name)

            print("MANIFEST ENCONTRADO:", mod.manifest.slug)

            repo.upsert_automation(mod.manifest)

        except ModuleNotFoundError as e:
            print("NÃO ACHOU:", module_name, e)
            continue
sync_all_manifests()