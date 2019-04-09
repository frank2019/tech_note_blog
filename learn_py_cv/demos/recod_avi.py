import cv2
 
cap = cv2.VideoCapture(0)
cap.set(3,320)#宽
cap.set(4,240)#高
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
       int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 为保存视频做准备
fourcc = cv2.VideoWriter_fourcc(*'mpeg')
fps=25
out = cv2.VideoWriter('./videoCapture/output2.avi', fourcc,fps,sz)

while True:
    # 一帧一帧的获取图像
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
        # 在帧上进行操作
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 开始保存视频
        out.write(frame)
        # 显示结果帧
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 释放摄像头资源
cap.release()
out.release()
cv2.destroyAllWindows()
