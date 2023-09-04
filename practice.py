# import soundfile as sf
# import wave
# input_wav_file = "record_2023-08-10T18-16_26.wav"
# output_pcm_file = "converted_pcm.wav"
# data, sample_rate = sf.read(input_wav_file)
# pcm_data = (data * 32767).astype('int16')
# sf.write(output_pcm_file, pcm_data, sample_rate, subtype='PCM_16')
# with wave.open(output_pcm_file, 'rb') as obj:
#     print("Number of channels:", obj.getnchannels())
#     print("Sample width:", obj.getsampwidth())
#     print("Frame rate:", obj.getframerate())
#     print("Number of frames:", obj.getnframes())
#     print("Parameters:", obj.getparams())
#     t_audio = obj.getnframes()/obj.getframerate()
#     print(t_audio)
#     frames = obj.readframes(-1)
 
