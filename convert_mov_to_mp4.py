import os
import subprocess
import glob

def convert_mov_to_mp4(input_path, output_path=None):
    """
    Convert a .mov file to .mp4 (H.264 + AAC) for web playback.
    
    Args:
        input_path (str): Path to the input .mov file
        output_path (str, optional): Path to save the .mp4 file. 
                                     If None, saves in the same folder as input.
    
    Returns:
        str: Path to the converted .mp4 file
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = base + ".mp4"
    
    command = [
        "ffmpeg",
        "-y",                     # overwrite output if exists
        "-i", input_path,         # input file
        "-vcodec", "libx264",     # video codec
        "-acodec", "aac",         # audio codec
        "-movflags", "faststart", # allow web playback to start quickly
        output_path
    ]
    
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Converted: {input_path} -> {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_path}: {e.stderr.decode()}")
        return None
    
    return output_path

# ===== Example: Convert all .mov files in a folder =====
folder = "videos"  # folder containing .mov files
mov_files = glob.glob(os.path.join(folder, "*.mov"))

for mov in mov_files:
    convert_mov_to_mp4(mov)
