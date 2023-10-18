import cv2 as cv
import shutil
import os

sourcepath = "C:/Users/vivek/OneDrive/Desktop/New folder/insta_post_downloader/downloaded_photo/"
dest1 = "C:/Users/vivek/OneDrive/Desktop/New folder/insta_post_downloader/semi/"
dest2 = "C:/Users/vivek/OneDrive/Desktop/New folder/insta_post_downloader/non_semi/"

prev = None
cv.namedWindow("image", cv.WINDOW_NORMAL)

# Using resizeWindow()
cv.resizeWindow("image", 440, 740)
count = 0
for filepath in os.listdir(sourcepath):
    count += 1
    imgpath = sourcepath + filepath
    img = cv.imread(imgpath)
    cv.imshow("image", img)

    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()
        break
    elif k == ord('y') or k == ord('Y'):
        shutil.move(imgpath, dest1 + filepath)
    elif k == ord('d') or k == ord('D'):
        os.remove(imgpath)
    else:
        shutil.move(imgpath, dest2 + filepath)
print(count)
    