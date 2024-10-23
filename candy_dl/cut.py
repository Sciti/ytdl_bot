import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip

# Set up argument parsing
parser = argparse.ArgumentParser(description="Cut a section from a video.")
parser.add_argument("input_file", help="The input video file")
parser.add_argument("start_time", help="Start time in format (HH:MM:SS or seconds)")
parser.add_argument("end_time", help="End time in format (HH:MM:SS or seconds)")
parser.add_argument("output_file", help="The output video file")

args = parser.parse_args()

# Convert time string to seconds
def time_to_seconds(time_str):
    parts = time_str.split(':')
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    elif len(parts) == 2:
        return int(parts[0]) * 60 + float(parts[1])
    else:
        return float(parts[0])


def cut_video(input_file, start_time, end_time, output_file):
    video = VideoFileClip(input_file)
    video_cut = video.subclip(start_time, end_time)
    video_cut.write_videofile(output_file, codec="libx264")


def cut_video_orig(input_file, start_time, end_time, output_file):
    # Load the video file
    video = VideoFileClip(args.input_file)

    # Convert start and end times to seconds
    start_time = time_to_seconds(args.start_time)
    end_time = time_to_seconds(args.end_time)

    # Cut the section from the video
    video_cut = video.subclip(start_time, end_time)

    # Write the result to the output file
    video_cut.write_videofile(args.output_file, codec="libx264")
