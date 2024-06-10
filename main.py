import argparse
import moviepy.editor as mp

def extract_video_segment(input_path, output_path, start_time, end_time):
    # Load the video
    video = mp.VideoFileClip(input_path)
    
    # Extract the desired segment
    video_segment = video.subclip(start_time, end_time)
    
    # Save the extracted segment
    video_segment.write_videofile(output_path)
    print(f"Segment saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Extract a segment from a video file.")
    parser.add_argument("--input_path", required=True, help="Path to the input video file")
    parser.add_argument("--output_path", required=True, help="Path to save the extracted video segment")
    parser.add_argument("--start_time", type=float, required=True, help="Start time of the segment in seconds")
    parser.add_argument("--end_time", type=float, required=True, help="End time of the segment in seconds")
    
    args = parser.parse_args()
    
    extract_video_segment(args.input_path, args.output_path, args.start_time, args.end_time)

if __name__ == "__main__":
    main()
