# ****** Лабораторная 3  Задание 1
import cv2
import numpy as nm
print("Введите целое положительное число N (больше 1):")

try:
 N = int(input())

 if N <= 1:
  print("Введите число больше 1")
 else:
  is_prime = True

 for i in range(2, int(N**0.5)+1):
  if N % i == 0:
    is_prime = False
  break

 if is_prime:
  print("Число", N, "является простым")
 else:
  print("Число", N, "не является простым")

except:
 print("введено некорректное число")

 #******* Задача 2
import cv2
image = cv2.imread('image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray_image)
cv2.imwrite('gray_image.jpg', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

