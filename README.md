# WMA to MP3 Utility

Automatically stream YouTube video to audio file.

## Setup

Tools:
* Docker Engine (or Desktop)
* VSCode with plugins:
  - "ms-vscode-remote.remote-containers"
  - "ms-azuretools.vscode-docker"

Code:
```bash
mkdir yt2mp3 && cd yt2mp3
git remote add origin https://github.com/sunshine55/python-practice
git fetch origin feature/yt2mp3
```

### Start the Docker container
Use the provided docker-compose configuration to start the container:
```bash
docker compose up -d
docker exec -it yt2mp3 bash
```

### Install Poetry and dependencies
```bash
apt update
apt install pipx ffmpeg
pipx ensurepath
pipx install poetry
poetry install
eval $(poetry env activate)
```

## Usage

```bash
cp src/prompt.example prompt.gemini.txt
python src/main.py prompt.gemini
```

## Notes

https://app.readthedocs.org/projects/python-pytube/downloads/pdf/stable/
https://pypi.org/project/pytubefix
