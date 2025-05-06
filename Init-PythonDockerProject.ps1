# .\Init-PythonDockerProject.ps1 -ProjectName "nazev_projektu"

param (
    [string]$ProjectName = "my_project"
)

# 1. Vytvoření složky projektu
New-Item -ItemType Directory -Force -Path $ProjectName
Set-Location $ProjectName

# 2. Inicializace git
git init
@"
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.env
*.env
.DS_Store
*.vscode/
"@ | Out-File ".gitignore" -Encoding utf8

# 3. Vytvoření main.py
@"
def main():
    print(\"Hello from Dockerized Python!\")

if __name__ == \"__main__\":
    main()
"@ | Out-File "main.py" -Encoding utf8

# 4. requirements.txt (prázdný)
"" | Out-File "requirements.txt"

# 5. Dockerfile
@"
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [\"python\", \"main.py\"]
"@ | Out-File "Dockerfile" -Encoding utf8

# 6. .dockerignore
@"
venv/
__pycache__/
*.pyc
"@ | Out-File ".dockerignore" -Encoding utf8

# 7. docker-compose.yml
@"
version: '3.8'

services:
  app:
    build: .
    container_name: ${ProjectName}-container
    volumes:
      - .:/app
    working_dir: /app
    command: python main.py
"@ | Out-File "docker-compose.yml" -Encoding utf8

# 8. .devcontainer/devcontainer.json
New-Item -ItemType Directory -Force -Path ".devcontainer"
@"
{
  \"name\": \"Python Dev Container\",
  \"dockerComposeFile\": \"../docker-compose.yml\",
  \"service\": \"app\",
  \"workspaceFolder\": \"/app\",
  \"settings\": {
    \"python.pythonPath\": \"/usr/local/bin/python\"
  },
  \"extensions\": [
    \"ms-python.python\",
    \"ms-python.vscode-pylance\"
  ],
  \"postCreateCommand\": \"pip install -r requirements.txt\"
}
"@ | Out-File ".devcontainer/devcontainer.json" -Encoding utf8

# 9. Vytvoření venv (volitelné)
python -m venv venv

Write-Host "✅ Projekt '$ProjectName' byl úspěšně vytvořen."
Write-Host "📁 Struktura: Docker + DevContainer + Git + Python"

