import librosa
import librosa.display
import matplotlib.pyplot as plt

import random
import string
import os

directory_path = "E:\\Projects 2023-2024\\VR Project\\Speech Test\\Assets\\Audios"
# List to store the loaded data
data = []

# Iterate through files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".wav"):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)

        # Load the WAV file
        wav_data, sampling_rate = librosa.load(file_path)

        # Append the loaded data to the list
        data.append((wav_data, sampling_rate, filename))

# Now 'data' is a list containing tuples of (wav_data, sampling_rate, filename)
# You can iterate through the list and process each entry
for wav_data, sampling_rate, filename in data:
    # Your processing code here
    print(f"Processing {filename}: Data shape: {wav_data.shape}, Sampling rate: {sampling_rate}")
    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(wav_data,sr=sampling_rate)
    print(filename)



# In[15]:


from pydub import AudioSegment
import os

def split_and_save_audio(input_path, output_folder, chunk_length):
    # Reading audio from the input path
    sound = AudioSegment.from_wav(input_path)
    
    # Calculate the total duration of the audio
    total_duration = len(sound)
    
    # Calculate the number of chunks needed
    num_chunks = total_duration // chunk_length
    
    # Ensure the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Splitting audio into chunks
    for i in range(num_chunks):
        start_time = i * chunk_length
        end_time = (i + 1) * chunk_length
        chunk = sound[start_time:end_time]
        
        # Save each chunk to the output folder
        chunk.export(os.path.join(output_folder, f"chunk_{i+1}.wav"), format="wav")
        
    if(num_chunks==0):
        sound.export(os.path.join(output_folder, f"chunk_1.wav"), format="wav")

# Example usage

for filename in os.listdir(directory_path):
    input_audio_path = f"E:\\Projects 2023-2024\\VR Project\\Speech Test\\Assets\\Audios\\{filename}"
    if filename.endswith(".wav"):
        
        output_folder_path = f"E:\\Projects 2023-2024\\VR Project\\Speech Test\\Assets\\Interview_Questions\\question_number_{filename}\\One_Question_Chunks"

        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
            print(f"Folder '{output_folder_path}' created.")
        else:
            print(f"Folder '{output_folder_path}' already exists.")

        chunk_length_seconds = 5  # You can adjust this value

        split_and_save_audio(input_audio_path, output_folder_path, chunk_length_seconds * 1000)








