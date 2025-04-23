# WMA to MP3 Utility

Transform local music with old format (WMA) into the new audio format (MP3).

## Setup

Tools:
* Docker Engine (or Desktop)
* VSCode with plugins:
  - "ms-vscode-remote.remote-containers"
  - "ms-azuretools.vscode-docker"

Code:
```bash
mkdir wma2mp3 && cd wma2mp3
git remote add origin https://github.com/sunshine55/python-practice
git fetch origin feature/wma2mp3
```

### Start the Docker container
Use the provided docker-compose configuration to start the container:
```bash
docker compose up -d
docker exec -it wma2mp3 bash
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

### Create IO folders
Create the following folders in the root directory of the project:
* `music-oldcollection`: Place your .wma files here.
* `music-newcollection`: This folder will store the converted .mp3 files.

### Execute the scripts
```bash
# Transform .wma files into .mp3
poetry run python src/convert.py

# Count the number of .wma files in the music-oldcollection folder
poetry run python src/count.py

# Delete all .wma files after conversion
poetry run python src/cleanup.py
```

## Notes
* Ensure that the music-oldcollection folder contains only .wma files you want to convert.
* The converted .mp3 files will maintain the same directory structure as the original .wma files.
* This project uses the pydub library for audio conversion. Ensure that the required dependencies (e.g., ffmpeg) are installed in the Docker container.
