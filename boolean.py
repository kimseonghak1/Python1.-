# 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 애완동물을 소개해 주세요~
animal = "고양이"
name = "코카"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " +animal+"의 이름은 "+name+"에요")
hobby = "공놀이"
# print(name+ "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요")
print(name+"는 어른일까요? " + str(is_adult))

# 주석은 ctrl + /
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

# Quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명
# : station

# 변수값
# : "사당", "신도림", "인천공항" 순서대로 입력

# 출력 문장
# : XX 행 열차가 들어오고 있습니다.

station = "사당"
print(station +"행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다")