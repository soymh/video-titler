# Video Titler

## Overview
The Video Titler is a tool that automatically generates concise titles for video files in a specified directory. It uses the WhisperX model to transcribe audio from videos and an OpenAI API to generate titles based on the transcriptions.

## Features
- Extracts audio from video files.
- Transcribes audio using WhisperX.
- Generates concise video titles using OpenAI's API.
- Renames video files with the generated titles.

## Requirements
- Python 3.10
- Conda environment with PyTorch 2.0 and CUDA 11.8 (for GPU support)
- WhisperX library
- OpenAI API key

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Video-Titler.git
   cd Video-Titler
   ```

2. Run the setup script to create and activate the conda environment:
   ```bash
   ./setup.sh
   ```

3. Set your OpenAI API key in the `.env` file:
   ```bash
   cp .env.example .env
   nano .env
   ```
   Replace `ADD-OUR-API-KEY` with your actual OpenAI API key.

## Usage
Run the script with the `-d` flag followed by the directory containing your video files:
```bash
python titler.py -d /path/to/video/directory
```

## Directory Structure
- `titler.py`: Main script for processing video files.
- `vhisperx`: Bash script for extracting audio and running WhisperX.
- `setup.sh`: Script for setting up the conda environment and installing dependencies.
- `requirements.txt`: List of Python dependencies.
- `.env.example`: Example environment file.
- `.gitignore`: List of files to ignore in version control.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
