#ライブラリインポート
import cv2
import math

#触る場所 ここから =================================================================
BASE_FILE_PATH = "C:/Users/81904/development/generativeImage/"
IMAGE1_FOLDER_NAME = "img1/"
IMAGE2_FOLDER_NAME = "img2/"
IMAGE3_FOLDER_NAME = "img3/"
IMAGE4_FOLDER_NAME = "img4/"
IMAGE5_FOLDER_NAME = "img5/"
IMAGE6_FOLDER_NAME = "img6/"
IMAGE7_FOLDER_NAME = "img7/"
OUTPUT_FOLDER_NAME = "output/"

FILENAME_ARR_LAYER1 = [ \
                      "nitroid2.png", \
                      ]

FILENAME_ARR_LAYER2 = [ \
                      "face2.png", \
                      ]

FILENAME_ARR_LAYER3 = [ \
                      "eyes.png", \
                      ]

FILENAME_ARR_LAYER4 = [ \
                      "img4_1.png", \
                      ]

FILENAME_ARR_LAYER5 = [ \
                      "img5_1.png", \
                      ]

FILENAME_ARR_LAYER6 = [ \
                      "img6_1.png", \
                      ]

FILENAME_ARR_LAYER7 = [ \
                      "img7_1.png", \
                      ]

#触る場所 ここまで =================================================================

def putSprite_mask(back, front4, pos):
    x, y = pos
    fh, fw = front4.shape[:2]
    bh, bw = back.shape[:2]
    x1, y1 = max(x, 0), max(y, 0)
    x2, y2 = min(x+fw, bw), min(y+fh, bh)
#    if not ((-fw < x < bw) and (-fh < y < bh)) :
#        return back
#    front3 = front4[:, :, :3]
#    mask1 = front4[:, :, 3]
#    mask3 = 255 - cv2.merge((mask1, mask1, mask1))
#    mask_roi = mask3[y1-y:y2-y, x1-x:x2-x]
#    front_roi = front3[y1-y:y2-y, x1-x:x2-x]
#    roi = back[y1:y2, x1:x2]
#    tmp = cv2.bitwise_and(roi, mask_roi)
#    tmp = cv2.bitwise_or(tmp, front_roi)
#    back[y1:y2, x1:x2] = tmp
    back[y1:y2, x1:x2] = back[y1:y2, x1:x2] * (1 - front4[:, :, 3:] / 255) + \
                          front4[:, :, :3] * (front4[:, :, 3:] / 255)
    return back



x = 0
y = 0

index_L1 = 0 #index初期化
for filename_layer1 in FILENAME_ARR_LAYER1:
    
    #合成①(一番下の背景を置くだけだから、合成関数putSprite_mask()使ってない)
    img_layer1 = cv2.imread(BASE_FILE_PATH + IMAGE1_FOLDER_NAME + filename_layer1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
    cv2.imshow('img', img_layer1)#ここは必要に応じて有効にしたり無効にしたりする
    cv2.waitKey(0)
    #合成②
    index_L2 = 0 #index初期化
    for filename_layer2 in FILENAME_ARR_LAYER2:
        img_layer2 = cv2.imread(BASE_FILE_PATH + IMAGE2_FOLDER_NAME + filename_layer2, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
        img = putSprite_mask(img_layer1, img_layer2, (x,y))
        cv2.imshow('img', img)#ここは必要に応じて有効にしたり無効にしたりする
        cv2.waitKey(0)
        #合成③
        index_L3 = 0 #index初期化
        for filename_layer3 in FILENAME_ARR_LAYER3:
            img_layer3 = cv2.imread(BASE_FILE_PATH + IMAGE3_FOLDER_NAME + filename_layer3, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
            img_tmp = img.copy()
            img = putSprite_mask(img_tmp, img_layer3, (x,y))
            cv2.imshow('img', img)#ここは必要に応じて有効にしたり無効にしたりする
            cv2.waitKey(0)
            #合成④
            index_L4 = 0 #index初期化
            for filename_layer4 in FILENAME_ARR_LAYER4:
                img_layer4 = cv2.imread(BASE_FILE_PATH + IMAGE4_FOLDER_NAME + filename_layer4, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
                img_tmp = img.copy()
                img = putSprite_mask(img_tmp, img_layer4, (x,y))

                #合成⑤
                index_L5 = 0 #index初期化
                for filename_layer5 in FILENAME_ARR_LAYER5:
                    img_layer5 = cv2.imread(BASE_FILE_PATH + IMAGE5_FOLDER_NAME + filename_layer5, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
                    img_tmp = img.copy()
                    img = putSprite_mask(img_tmp, img_layer5, (x,y))

                    #合成⑥
                    index_L6 = 0 #index初期化
                    for filename_layer6 in FILENAME_ARR_LAYER6:
                        img_layer6 = cv2.imread(BASE_FILE_PATH + IMAGE6_FOLDER_NAME + filename_layer6, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
                        img_tmp = img.copy()
                        img = putSprite_mask(img_tmp, img_layer6, (x,y))

                        #合成⑦
                        index_L7 = 0 #index初期化
                        for filename_layer7 in FILENAME_ARR_LAYER7:
                            img_layer7 = cv2.imread(BASE_FILE_PATH + IMAGE7_FOLDER_NAME + filename_layer7, -1) #第二引数は -1:with alpha 0:GrayScale 1(or nothing):color
                            img_tmp = img.copy()
                            img = putSprite_mask(img_tmp, img_layer7, (x,y))
                            #cv2.imshow('img', img)#ここは必要に応じて有効にしたり無効にしたりする

                            #書き込み ここから(最後のループ内に入れる)=================
                            #cv2.waitKey(0)
                            cv2.imwrite(BASE_FILE_PATH + OUTPUT_FOLDER_NAME + 'output' \
                                        +'_'+str(index_L1) \
                                        +'_'+str(index_L2) \
                                        +'_'+str(index_L3) \
                                        +'_'+str(index_L4) \
                                        +'_'+str(index_L5) \
                                        +'_'+str(index_L6) \
                                        +'_'+str(index_L7) \
                                        +'.png', img)#第二引数に最終的な出力画像をセットする
                            cv2.destroyAllWindows()
                            #書き込み ここまで =========================================

                            #index加算
                            index_L7 += 1
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










