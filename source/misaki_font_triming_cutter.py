#美咲フォントpng画像は白地に黒色なので反転して黒地に白文字にします
#そしてそのあとpyxeleditorで読み込める256x256ドットサイズのpngに分割してやります

import cv2
 
img = cv2.imread('assets/fonts/k8x12s_jisx0208.png')
cv2.imshow('original_font', img)
#反転作業
for y in range(752):
    for x in range(1128):
        pic_col_blue = img[x,y,0] #座標(x,y)の青色の画素値を取得
        if int(pic_col_blue) == 255: #255だと白い点だということなので・・
            img[x,y] = [0,0,0] #黒色のデータを書き込む
        else:
            img[x,y] = [255,255,255] #元が黒色なら白色のデータを書き込む

cv2.imshow('reverse_font', img)

#img[top:bottom, left:right]
#左上の座標がx1,y1 右下の座標がx2,y2の場合は・・・
#img[y1:y2, x1:x2]となります
#################################################左端1列目 A
x1,y1 =   0,0
x2,y2 = 256,256
img1a = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___001a.png',img1a)
cv2.imshow('font__001a', img1a)

x1,y1 =   0,256
x2,y2 = 256,512
img2a = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___002a.png',img2a)
cv2.imshow('font__002a', img2a)

x1,y1 =   0,512
x2,y2 = 256,768
img3a = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___003a.png',img3a)
cv2.imshow('font__003a', img3a)

x1,y1 =   0,768
x2,y2 = 256,1024
img4a = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___004a.png',img4a)
cv2.imshow('font__004a', img4a)

#################################################真ん中2列目 B
x1,y1 = 256,0
x2,y2 = 512,256
img1b = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___001b.png',img1b)
cv2.imshow('font__001b', img1b)

x1,y1 = 256,256
x2,y2 = 512,512
img2b = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___002b.png',img2b)
cv2.imshow('font__002b', img2b)

x1,y1 = 256,512
x2,y2 = 512,768
img3b = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___003b.png',img3b)
cv2.imshow('font__003b', img3b)

x1,y1 = 256,768
x2,y2 = 512,1024
img4b = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___004b.png',img4b)
cv2.imshow('font__004b', img4b)

#################################################右端3列目 C
x1,y1 = 512,0
x2,y2 = 752,256
img1c = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___001c.png',img1c)
cv2.imshow('font__001c', img1c)

x1,y1 = 512,256
x2,y2 = 752,512
img2c = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___002c.png',img2c)
cv2.imshow('font__002c', img2c)

x1,y1 = 512,512
x2,y2 = 752,768
img3c = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___003c.png',img3c)
cv2.imshow('font__003c', img3c)

x1,y1 = 512,768
x2,y2 = 752,1024
img4c = img[y1:y2, x1:x2]
cv2.imwrite('assets/fonts/k8x12s_jisx0208___004c.png',img4c)
cv2.imshow('font__004c', img4c)

#-----------------------------------wait
cv2.waitKey(0)
cv2.destroyAllWindows()