sentence = input("번역하고 싶은 문장을 입력하세요 : ")
key_word = input("변환에 필요한 단어를 입력하세요 : ")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translated = ""

for i in range(len(sentence)):
    original_index = alphabet.index(sentence[i])  # 원문의 문자 위치
    key_index = alphabet.index(key_word[i % len(key_word)])  # 암호화 키의 문자 위치
    new_index = (original_index + key_index) % len(alphabet)  # 새로운 문자 위치 (원문의 위치에서 암호화 키의 위치만큼 이동)
    translated += alphabet[new_index]  # 새로운 문자를 추가

print(f"번역된 문장 : {translated}")
