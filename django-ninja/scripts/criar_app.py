# ./scripts/criar_app.py

import os
import sys

def criar_app(app_name):
    base_path = f"src/apps/{app_name}"
    
    directories = [
        base_path,
        f"{base_path}/data",
        f"{base_path}/management",
        f"{base_path}/management/commands",
        f"{base_path}/models",
        f"{base_path}/schemas",
        f"{base_path}/services",
        f"{base_path}/views"
    ]
    
    files = {
        f"{base_path}/data/__init__.py": "",
        f"{base_path}/management/__init__.py": "",
        f"{base_path}/management/commands/__init__.py": "",
        f"{base_path}/models/__init__.py": "# ./src/apps/{app_name}/models/__init__.py\n\n# from .entidade import Entidade",
        f"{base_path}/schemas/__init__.py": "",
        f"{base_path}/services/__init__.py": "",
        f"{base_path}/views/__init__.py": "",
        f"{base_path}/__init__.py": "",
        f"{base_path}/admin.py": f"# ./src/apps/{app_name}/admin.py\n\nfrom django.contrib import admin\n\n# Register your models here.",
        f"{base_path}/apps.py": (
            f"# ./src/apps/{app_name}/apps.py\n\n"
            f"from django.apps import AppConfig\n\n"
            f"class {app_name.capitalize()}Config(AppConfig):\n"
            f"\tdefault_auto_field = 'django.db.models.BigAutoField'\n"
            f"\tname = 'apps.{app_name}'\n\n"
            f"# TODO: não esqueça de adicionar o seguinte conteúdo no INSTALLED_APPS do settings.py: 'apps.{app_name}',"
        ),
        f"{base_path}/api.py": (
            f"# ./src/apps/{app_name}/api.py\n\n"
            f"from ninja import NinjaAPI\n"
            f"#from .views.produto_view import produto_router as router_produto\n\n"
            f"api = NinjaAPI(urls_namespace='{app_name}-api')\n"
            f"#api.add_router('produto', router_produto)"
        ),
        f"{base_path}/urls.py": (
            f"# ./src/apps/{app_name}/urls.py\n\n"
            f"from django.urls import path, include\n"
            f"from .api import api\n\n"
            f"urlpatterns = [\n"
            f"\tpath('', include(api.urls())),\n"
            f"]"
        )
    }
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    for file_path, content in files.items():
        with open(file_path, "w") as file:
            file.write(content)
    print(f"App structure for '{app_name}' created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 criar_app.py <app_name>")
        sys.exit(1)
    
    app_name = sys.argv[1]
    criar_app(app_name)
