import os
import subprocess
import requests
import sys
import colorama
from colorama import Fore, Style

def get_video_files(directory):
    video_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            video_files.append(os.path.join(directory, filename))
    return video_files

def run_vhisperx(video_file):
    subprocess.run(["vhisperx", "--vid", video_file])

def read_output_file(video_name):
    output_file_path = os.path.join(video_name, "output_file.txt")
    with open(output_file_path, "r") as file:
        return file.read()

def send_to_api(text):
    api_url = "https://api.together.ai/your-endpoint"  # Replace with the actual API endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with your actual API key
    }
    data = {
        "text": text,
        "task": "pick_concise_name"
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.json().get("concise_name", "")

def rename_video(video_file, new_name):
    directory = os.path.dirname(video_file)
    new_video_file = os.path.join(directory, new_name + ".mp4")
    os.rename(video_file, new_video_file)
    return new_video_file

def log_task(log_file, task):
    with open(log_file, "a") as file:
        file.write(task + "\n")

def main():
    colorama.init(autoreset=True)
    if len(sys.argv) != 3 or sys.argv[1] != "-d":
        print(Fore.RED + "Usage: python script.py -d <directory>")
        sys.exit(1)

    directory = sys.argv[2]
    video_files = get_video_files(directory)
    log_file = "1video-titler.txt"

    if not video_files:
        print(Fore.YELLOW + "No video files found in the directory.")
        log_task(log_file, "No video files found in the directory.")
        sys.exit(0)

    for video_file in video_files:
        video_name = os.path.splitext(os.path.basename(video_file))[0]
        print(Fore.CYAN + f"Processing video: {video_name}")

        run_vhisperx(video_file)
        print(Fore.GREEN + f"vhisperx completed for {video_name}")

        output_text = read_output_file(video_name)
        print(Fore.GREEN + f"Output file read for {video_name}")

        concise_name = send_to_api(output_text)
        print(Fore.GREEN + f"Concise name received from API for {video_name}: {concise_name}")

        new_video_file = rename_video(video_file, concise_name)
        print(Fore.GREEN + f"Video renamed to: {new_video_file}")

        log_task(log_file, f"Processed {video_name} and renamed to {concise_name}")

    print(Fore.MAGENTA + "All tasks completed. Check 1video-titler.txt for the log.")

if __name__ == "__main__":
    main()
