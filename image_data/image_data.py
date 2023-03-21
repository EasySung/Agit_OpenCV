import cv2

# 이미지 파일을 읽어온다
img = cv2.imread('image_data/cat.jpeg')

# 읽어온 이미지 파일의 RGB값 출력
print(img)

# 읽어온 이미지를 화면에 보여준다
cv2.imshow('image', img)

# 키 입력을 기다린다
cv2.waitKey(0)

# 모든 창을 닫는다
cv2.destroyAllWindows()