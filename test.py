# 1.
# input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა
# სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ
# არა სიმბოლოები, რიცხვები, დიდი/პატარა ასოები (ლათინურად) თუ ქართულს შემოიტანს
# უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”
# **უნდა გვქონდეს 4 ინფუთი - სიგრძე / რიცხვები უნდა თუ არა / დიდი და პატარა ასოები თუ
# უნდა / თუ უნდა სიმბოლოები
# **უნდა დაწეროთ ლოგიკა იმის მიხედვით რასაც აირჩევს მომხმარებელი და ბოლოს
# დაუგენერიროთ პაროლი.
import dataclasses
import random
import string


# length = input("აირჩიეთ პაროლის სასურველი სიგრძე: ")
#
# if not length.isdigit():
#     print("შეიყვანე რიცხვი")
#     exit()
#
# length = int(length)
#
# is_number = input("გსურს რიცხვების გამოყენება? დაწერე დიახ ან არა: ")
# lower_upper = input("გსურს დიდი და პატარა ასოების გამოყენება? დაწერე დიახ ან არა: ")
# symb = input("გსურს სიმბოლოების გამოყენება? დაწერე დიახ ან არა: ")
#
#
# password = ""
#
#
# if is_number == "დიახ":
#     password += "0123456789"
#
# if lower_upper == "დიახ":
#     password += string.ascii_letters
#
# if symb == "დიახ":
#     password += string.punctuation
#
# passcode = ""
# for n in range(length):
#     passcode += random.choice(password)
#
# print(f"შენი ახალი პაროლის არის {passcode}")

# 3 .

# import random
# from html.parser import charref
# from random import shuffle
#
#
# while True:
#     inp = input("შემოიყვანეთ სასურველი სახელი: ").strip()
#
#     word = inp.split()
#     word = str(*word)
#     if len(word) == 1 and word[0] in string.ascii_letters:
#         break
#
#     if len(word) > 1:
#         print("გთხოვთ შემოიყვანოთ მხოლოდ ერთი სიტყვა")
#
#     words1 = "ზედმეტი", "სახელი", "პროგრამისტი", "რობოტი", "კიბორგი"
#     words2 = "კარგი", "ცუდი", "ბოროტი", "კეთილი", "დაღლილი"
#     words3 = "ექიმი", "ინჟინერი", "მათემატიკოსი", "ქართველი", "ჟირაფი"
#
#     zedmetsaxeli = []
#
#     zedmetsaxeli.append(f"{random.choice(words1)} {word}")
#     zedmetsaxeli.append(f"{word} {random.choice(words2)}")
#     zedmetsaxeli.append(f"კეთილი {word}")
#     zedmetsaxeli.append(f"{random.choice(words3)} {word}")
#     zedmetsaxeli.append(f"ბოროტი {word}")
#
#     string = inp[0]
#     final_clean_data = word.strip("[]").strip("'")
#     print("\n".join(zedmetsaxeli))



# inp = str(input("შემოიყვანეთ სასურველი სახელი: ").strip())
# random_number = random.randint(1, 100)
#
# print("იხილეთ 5 ზედმეტსახელი, რომელიც პროგრამამ მოგიფიქრათ:")
# print(f"კარგი {inp}")
# print(f"ბოროტი {inp}")
# print(f"პროგრამისტი {inp}")
# print(f"{inp} მართალი")
# print(f"{inp}{random_number}")

# გამარტივებული ვერსია


# 4.

# inp = input("შეიყვანეთ რიცხვები: ").strip()
# strip = inp.split()
# num = [int(n) for n in strip]
#
# print("აირჩიეთ სორტირების მეთოდი")
# print("1 - კლებადობა")
# print("2 - ზრდადობა")
# print("3 - რენდომად")
# print("4 - მხოლოდ უნიკალური მონაცემები")
#
# x = input("აირჩიეთ რიცხვი 1-4-მდე: ")
#
# inp = int
# y = []
# if x == "1":
#     y = sorted(inp, reverse=True)
# elif x == "2":
#     y = sorted(inp)
# elif x == "3":
#     random.shuffle(num)
#     y = num
# elif x == "4":
#     y = list(set(num))
#
# print(f"იხილეთ სია")
# print(y)

# 5.

#მომხმარებელი შეჰყავს ტექსტი.
#ამოცანა: პროგრამამ უნდა წაშალოს ყველა ციფრი და სიმბოლო, დატოვოს მხოლოდ ასოები და
#სივრცეები.

# inp = input("შეიყვანეთ სასურველი ტექსტი: ")
# x = ""
#
# for char in inp:
#     if char in string.ascii_letters or char in string.whitespace:
#         x += char
# print(x)

# 6.

# პირამიდა
# მომხმარებელს შეჰყავს რიცხვების სია (მაგ. 3,5,7,2).
# ამოცანა: შექმენი “პირამიდა”, სადაც ყოველი ახალი რიგი ზემოთაა წინა ორი რიცხვის ჯამი.
# 3 5 7 2
# 8 12 9
# 20 21
# 41

# inp = input("შეიყვანე სასურველი რიცხვები პირამიდისთვის: ")
# inp = inp.split()
# inp = [int(n) for n in inp]
#
# x = inp
# print(*x)
#
# while len(x) > 0:
#     jami = []
#     for i in range(len(x) - 1):
#         jami.append(x[i] + x[i + 1])
#     print(*jami)
#     x = jami

# 7.

# inp = input("დაწერე წინადადება: ")
#
# mydict = {}
# split = inp.split()
#
# for i in split:
#     mydict[i] = len(i)
#
# print(mydict)



