import importlib
from pathlib import Path
from automations_hub.infra.automation_repository import AutomationRepository

def sync_all_manifests() -> None:
    repo = AutomationRepository()
    packages_dir = Path(__file__).parent.parent.parent / "packages"
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
                # o manifest.py realmente não existe nesse pacote — ok, pula
                print(f"SEM MANIFEST: {pkg_path.name} (esperado se não for automação)")
            else:
                # o manifest existe, mas quebrou tentando importar outra coisa
                print(f"ERRO DENTRO DO MANIFEST de {pkg_path.name}: faltou '{e.name}'")
                raise  # não engole o erro real, deixa estourar pra você ver o traceback completo

sync_all_manifests()