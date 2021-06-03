import cv2 as cv

#Reading the image
img = cv.imread('photo.jpg')


#Convert the image to gray scale
gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Invert the Image
inverted_gray_image = 255 - gray_scale

#Blur the image by gussian function
blurred_img = cv.GaussianBlur(inverted_gray_image, (21,21), 0)

#Invert the blurred image
inverted_blurred_img = 255 - blurred_img

#Creating pencil sketch Image
pencil_sketch_image = cv.divide(gray_scale,inverted_blurred_img,scale=256.0,)


#Displaying the image
#cv.imshow('Original Image',img)
#cv.imshow('Gray scale image', gray_scale)
#cv.imshow('inverted Gray scale image', inverted_gray_image)
#cv.imshow('blurred image', blurred_img)
#cv.imshow('Inverted blurred image', inverted_blurred_img)
#cv.imshow('pencil sketch image', pencil_sketch_image)



#waiting the image to close until done manually
#cv.waitKey(0)

#Saving the pencil sketch Image
cv.imwrite("final.png",pencil_sketch_image)
