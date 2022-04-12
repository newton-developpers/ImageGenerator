#ライブラリインポート
import cv2
import math

#触る場所 ここから =================================================================
BASE_FILE_PATH = "C:/Users/81904/development/generativeImage/"
IMAGE1_FOLDER_NAME = "img1/"
IMAGE2_FOLDER_NAME = "img2/"
IMAGE3_FOLDER_NAME = "img3/"
OUTPUT_FOLDER_NAME = "output/"

FILENAME_ARR_LAYER1 = [ \
                      "newton.png", \
                      "newton2.png", \
                      "newton3.png", \
                      ]

FILENAME_ARR_LAYER2 = [ \
                      "face.png", \
                      "face2.png", \
                      "face3.png", \
                      ]

FILENAME_ARR_LAYER3 = [ \
                      "eyes.png", \
                      "eyes2.png", \
                      "eyes3.png", \
                      ]
#触る場所 ここまで =================================================================

def putSprite_mask(back, front4, pos):
    x, y = pos
    fh, fw = front4.shape[:2]
    bh, bw = back.shape[:2]
    x1, y1 = max(x, 0), max(y, 0)
    x2, y2 = min(x+fw, bw), min(y+fh, bh)
    if not ((-fw < x < bw) and (-fh < y < bh)) :
        return back
    front3 = front4[:, :, :3]
    mask1 = front4[:, :, 3]
    mask3 = 255 - cv2.merge((mask1, mask1, mask1))
    mask_roi = mask3[y1-y:y2-y, x1-x:x2-x]
    front_roi = front3[y1-y:y2-y, x1-x:x2-x]
    roi = back[y1:y2, x1:x2]
    tmp = cv2.bitwise_and(roi, mask_roi)
    tmp = cv2.bitwise_or(tmp, front_roi)
    back[y1:y2, x1:x2] = tmp
    return back



x = 0
y = 0

index_L1 = 0 #index初期化
for filename_layer1 in FILENAME_ARR_LAYER1:
    
    #合成①(一番下の背景を置くだけだから、合成関数putSprite_mask()使ってない)
    img_layer1 = cv2.imread(BASE_FILE_PATH + IMAGE1_FOLDER_NAME + filename_layer1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
    
    #合成②
    index_L2 = 0 #index初期化
    for filename_layer2 in FILENAME_ARR_LAYER2:
        img_layer2 = cv2.imread(BASE_FILE_PATH + IMAGE2_FOLDER_NAME + filename_layer2, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
        img = putSprite_mask(img_layer1, img_layer2, (x,y))
        #cv2.imshow('img', img)#ここは必要に応じて有効にしたり無効にしたりする

        #合成③
        index_L3 = 0 #index初期化
        for filename_layer3 in FILENAME_ARR_LAYER3:
            img_layer3 = cv2.imread(BASE_FILE_PATH + IMAGE3_FOLDER_NAME + filename_layer3, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
            img2 = img.copy()
            img3 = putSprite_mask(img2, img_layer3, (x,y))
            #cv2.imshow('img3', img3)#ここは必要に応じて有効にしたり無効にしたりする

            #合成④
            index_L4 = 0 #index初期化
            for filename_layer4 in FILENAME_ARR_LAYER4:
                img_layer4 = cv2.imread(BASE_FILE_PATH + IMAGE4_FOLDER_NAME + filename_layer4, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
                img4 = img3.copy()
                img5 = putSprite_mask(img4, img_layer4, (x,y))
                #cv2.imshow('img5', img5)#ここは必要に応じて有効にしたり無効にしたりする

                #合成⑤
                index_L5 = 0 #index初期化
                for filename_layer5 in FILENAME_ARR_LAYER5:
                    img_layer5 = cv2.imread(BASE_FILE_PATH + IMAGE5_FOLDER_NAME + filename_layer5, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
                    img6 = img3.copy()
                    img7 = putSprite_mask(img6, img_layer5, (x,y))
                    #cv2.imshow('img7', img7)#ここは必要に応じて有効にしたり無効にしたりする

                    #合成⑥
                    index_L6 = 0 #index初期化
                    for filename_layer6 in FILENAME_ARR_LAYER6:
                        img_layer6 = cv2.imread(BASE_FILE_PATH + IMAGE6_FOLDER_NAME + filename_layer6, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
                        img8 = img3.copy()
                        img9 = putSprite_mask(img8, img_layer6, (x,y))
                        #cv2.imshow('img9', img9)#ここは必要に応じて有効にしたり無効にしたりする
                        
                        #書き込み ここから(最後のループ内に入れる)=================
                        cv2.waitKey(0)
                        cv2.imwrite(BASE_FILE_PATH + OUTPUT_FOLDER_NAME + 'output_'+str(index_L1)+'_'+str(index_L2)+'_'+str(index_L3)+'.png', img9)#第二引数に最終的な出力画像をセットする
                        cv2.destroyAllWindows()
                        #書き込み ここまで =========================================

                        #index加算
                        index_L6 += 1
                    #index加算
                    index_L5 += 1
                #index加算
                index_L4 += 1
            #index加算
            index_L3 += 1
        #index加算
        index_L2 += 1
    #index加算
    index_L1 += 1










