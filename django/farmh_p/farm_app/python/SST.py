#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class SpeechToText():
    def run_quickstart(path):
        # [START speech_quickstart]
        import io
        import os

        # Imports the Google Cloud client library
        # [START migration_import]
        from google.cloud import speech
        
        # [END migration_import]

        # Instantiates a client
        # [START migration_client]
        client = speech.SpeechClient()
        # [END migration_client]
        chdir="C:\\Users\\smhrd\\Anaconda3\\envs\\django\\farmh_p\\media\\audio\\"
        # The name of the audio file to transcribe
        file_name = chdir+path
        print(file_name,"testfilename")  
            
           

        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='ko-KR')

        # Detects speech in the audio file
        response = client.recognize(config=config, audio=audio)
        text=""
        for result in response.results:
            text+=result.alternatives[0].transcript
            print('Transcript: {}'.format(result.alternatives[0].transcript))
        # [END speech_quickstart]
        return text
