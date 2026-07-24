import importlib
from pathlib import Path
def sync_all_manifests() -> None:pass
    # repo = AutomationRepository()
    # packages_dir = Path(__file__).parent.parent.parent.parent.parent / "packages"

    # for pkg_path in packages_dir.iterdir():
    #     if not pkg_path.is_dir():
    #         continue
    #     module_name = pkg_path.name.replace("-", "_") + ".manifest"
    #     try:
    #         mod = importlib.import_module(module_name)
    #         repo.upsert_automation(mod.manifest)   # INSERT ou UPDATE no banco
    #     except ModuleNotFoundError:
    #         continue   # pacote sem manifest (ex: shared) — ignora e segue