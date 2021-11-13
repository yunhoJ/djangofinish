import os
import time
class Change():
    def changem4a(path):
        #현재 경로를 음성데이터 있는곳으로 변경
        os.chdir("C:\\Users\\smhrd\\Anaconda3\\envs\\django\\farmh_p\\media\\audio")
        #결과값 있으면 하나씩 올리는 아웃풋 페스
        outputPath="./result1.wav"
        uniq=1 
        while os.path.exists(outputPath):
            uniq+=1
            outputPath="./result"+str(uniq)+".wav"
       # 파일 명만 가져오기     
        outputPath=outputPath.split("/")
    #    path 경로 수정 
        testpath=""
        testpath=str(path).replace(" ","_")
      
        # time.sleep(3)
        #cmd 명령어 ffmpeg다운 파일 확장자 변경 
        os.system("ffmpeg -i "+str(testpath)+" "+outputPath[-1])
        return outputPath[-1]