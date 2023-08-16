from pydub import AudioSegment
import math
import os

# Had to make sure ffmpeg package was added and also had to
# put 'pkgs.ffmpeg' into the hidden replit.nix file dependencies

'''
This sprogram currently splits the target audio into quarters as mp3 files, lowers the bitrate to 64kbps, and saves them into the segmented folder.
'''


def split_audio(input_file, output_folder):
  audio = AudioSegment.from_file(input_file)
  
  #reduce the bitrate and compression to reduce file size
  
  
  split_length = len(audio) // 4
  
  # Split the audio into 4 parts
  first_quarter = audio[:split_length]
  second_quarter = audio[split_length:split_length*2]
  third_quarter = audio[split_length*2:split_length*3]
  fourth_quarter = audio[split_length*3:split_length*4]


  # Save the first quarter
  first_quarter_filename = os.path.join(output_folder, "1-segment.mp3")
  first_quarter.export(first_quarter_filename, format="mp3", bitrate="64k")

  # Save the second quarter
  second_quarter_filename = os.path.join(output_folder, "2-segment.mp3")
  second_quarter.export(second_quarter_filename, format="mp3", bitrate="64k")

  # Save the third quarter
  third_quarter_filename = os.path.join(output_folder, "3-segment.mp3")
  third_quarter.export(third_quarter_filename, format="mp3", bitrate="64k")

  # Save the fourth quarter
  fourth_quarter_filename = os.path.join(output_folder, "4-segment.mp3")
  fourth_quarter.export(fourth_quarter_filename, format="mp3", bitrate="64k")



if __name__ == "__main__":
  input_file_path = "audio-file-to-segment.mp3" #input the mp3 file to segment
  output_folder_path = "segmented"

  if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

  split_audio(input_file_path, output_folder_path)