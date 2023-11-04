import cv2 
#vid=cv2.VideoCapture(0)
vid=cv2.VideoCapture("project.mp4")
height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps=int(vid.get(cv2.CAP_PROP_FPS))
#out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))
while(True):
    ret,frame=vid.read()
    cv2.imshow("webcam",frame)
    #out.write(frame)
    if cv2.waitKey(25)==32:
        break
vid.release()
out.release()
