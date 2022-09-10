#자료형

# 애완동물을 소개해 주세요~
'''
점 세개도 주석이 된다 ~ control # 하면 여러 문장을 동시에 주석처리할 수 있음
'''
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "를 아주 좋아해요") # 변수 후에 콤마(,)가 들어갔을때 띄어쓰기가 됨 name, age, 
print(name + "는 어른일까요? " + str(is_adult))