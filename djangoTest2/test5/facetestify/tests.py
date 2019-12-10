from django.test import TestCase
import os
from datetime import time
import base64
# Create your tests here.
def loginFaceCheck(request):
   ## 人脸登陆验证
   if request.method == "POST" and request.is_ajax():
       # 获取base64格式的图片
       faceImage = request.POST.get('faceImg')
       # 提取出base64格式，并进行转换为图片
       index = faceImage.find('base64,')
       base64Str = faceImage[index+6:]
       img = base64.b64decode(base64Str)
       # 将文件保存
       backupDate = time.strftime("%Y%m%d_%H%M%S")
       if int(request.POST.get('id')) == 0 :
           fileName = BASE_LOGIN_LEFT_PATH +"LeftImg_%s.jpg" % (backupDate)
       else:
           fileName = BASE_LOGIN_RIGHT_PATH + "RightImg_%s.jpg" % (backupDate)
       file = open(fileName, 'wb')
       file.write(img)
       file.close()
       # 删除多余的图片
       filesLeft = os.listdir(BASE_LOGIN_LEFT_PATH)
       filesLeft.sort()
       leftImgCount = filesLeft.__len__()
       filesRight = os.listdir(BASE_LOGIN_RIGHT_PATH)
       filesRight.sort()
       RightImgCount = filesRight.__len__()

       if leftImgCount > 100:
           # 图片超过100个，删除一个
           os.unlink(BASE_LOGIN_LEFT_PATH +filesLeft[0])
       if RightImgCount > 100:
           # 图片超过100个，删除一个
           os.unlink(BASE_LOGIN_RIGHT_PATH + filesRight[0])

       # 对图片进行人脸识别比对
       canLogin = False
       AuthName = "未授权用户"

       # 1> 加载相机刚拍摄的人脸
       unknown_face = face_recognition.load_image_file(fileName)
       unknown_face_tmp_encoding = []
       try:
           unknown_face_tmp_encoding = face_recognition.face_encodings(unknown_face)[0]
       except IndexError:
           canLogin = False  # 图片中未发现人脸

       # 2> 进行比对

       ### 第一种方法
       # results = face_recognition.face_distance(known_face,unknown_face_tmp_encoding)
       # 小于0.6即对比成功。但是效果不好，因此我们设置阈值为0.4,
       # for i, face_distance in enumerate(results):
       #     if face_distance <= 0.4:
       #         canLogin = True
       #         AuthName = os.listdir(BASE_LOGIN_AUTH_PATH)[i][:-4]

       ### 第二中方法
       results1 = face_recognition.compare_faces(known_face,unknown_face_tmp_encoding,0.4)
       for i, face_distance in enumerate(results1):
           if face_distance == True:
               canLogin = True
               AuthName = os.listdir(BASE_LOGIN_AUTH_PATH)[i][:-4]

       JsonBackInfo = {
           "canLogin": canLogin,
           "AuthName": AuthName
       }

       return JsonResponse(JsonBackInfo)
