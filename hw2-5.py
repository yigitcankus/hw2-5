# """
# Seçeceğiniz herhangi bir şiiri bilgisayarına .txt dsyası olarak kaydedin.
# Şiirin kaç dizeden oluştuğunu hesaplayın ve başka bir dosyaya her dizenin ilk kelimesini yazdırın.
# """
#
# with open("odevsiir.txt", "r", encoding="utf8") as f:
#     lines = f.readlines()
#     f.seek(0)
#     count = 0
#     for i in f:
#         count += 1
# print(count)
#
# k = open("ilk_kelime.txt", 'w')
#
# for i in lines:
#     k.write(i)
#
# ##############
#
# """
# Parametre olarak girilen bir sayının asal sayı olup olmadığını belirten bir fonksiyon yazın.
# """
#
#  def asal_mi(x):
#
#     for i in range(2, x):
#         if x % i == 0:
#             print(x, "asal değildir.")
#             break
#     else:
#         print(x, "asaldır")
#
# asal_mi(7)
#
# ###############
# """
# Parametre olarak girilecek listenin elemanlarını yeni bir listeye her değer sadece bir kere geçecek şekilde aktaran bir fonksiyon yazın.
# Normalde bu işlemi set() komutu ile yapabiliriz ama bu seferlik bu komutu kullanmayalım.
# """
#
# def uniq_liste(lst):
#     new_list=[]
#     for i in lst:
#         if i not in new_list:
#             new_list.append(i)
#
#     print(new_list)
#
# uniq_liste([1,2,2,3,3,4,4,5])
#
# ################
#
# """
# Python'da hazır birçok modül bulunmaktadır.
# Zaman ile ilgili modüllerden birisini import ederek,
# parametre olarak doğum tarihi alan ve yaşı döndüren bir fonksiyon yazınız.
# """
# import  datetime
#
# def find_age(x):
#
#     print(datetime.datetime.now().year-x, "yaşındasınız.")
#
# find_age(1999)