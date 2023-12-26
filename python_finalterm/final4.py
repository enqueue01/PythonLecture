from numpy import dot
from numpy.linalg import norm
import numpy as np


class Music:
    def __init__(self, title="", artist="", genre="", language=""):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.language = language

    def setTitle(self, title):
        self.title = title

    def setArtist(self, artist):
        self.artist = artist

    def setGenre(self, genre):
        self.genre = genre

    def setLanguage(self, lang):
        self.language = lang

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def getGenre(self):
        return self.genre

    def getLanguage(self):
        return self.language

    def __str__(self):
        return f'제목 : {self.title.replace("**,", ",")}\n가수 : {self.artist.replace("**,", ",")}\n장르 : {self.genre}\n언어 : {self.language}\n'


class InvailedInput(Exception):
    def __init__(self):
        super().__init__("잘못된 입력입니다!")


def checkMusic():
    toggleC = 0
    if len(musics) == 0:
        print("빈 파일입니다.")
        return 1
    commandNum2 = input('음원을 조회합니다\n[조건옵션] 1: 제목, 2: 아티스트, 3: 장르, 4: 언어 : ')
    if commandNum2 == "1":
        musicInfo = input("[1] 음원의 제목을 입력하세요: ").replace(",", "**,")
        for music in musics:
            if music.getTitle() == musicInfo:
                print(music)
                toggleC = 1
        if toggleC == 0:
            print("정보가 없습니다.")
            return 1
    elif commandNum2 == "2":
        musicInfo = input("[2] 음원의 아티스트을 입력하세요: ").replace(",", "**,")
        for music in musics:
            if music.getArtist() == musicInfo:
                print(music)
                toggleC = 1
        if toggleC == 0:
            print("정보가 없습니다.")
            return 1
    elif commandNum2 == "3":
        musicInfo = input("[3] 음원의 장르를 입력하세요: ")
        for music in musics:
            if music.getGenre() == musicInfo:
                print(music)
                toggleC = 1
        if toggleC == 0:
            print("정보가 없습니다.")
            return 1
    elif commandNum2 == "4":
        musicInfo = input("[4] 음원의 언어를 입력하세요: ")
        for music in musics:
            if music.getLanguage() == musicInfo:
                print(music)
                toggleC = 1
        if toggleC == 0:
            print("정보가 없습니다.")
            return 1
    else:
        print("잘못입력하였습니다.")
        return 1


def codeexit(str):
    print(f"{str}종료합니다..")
    exit(0)


if __name__ == "__main__":
    genreType = ["발라드", "댄스", "힙합", "록", "트로트"]
    languageType = ["한국어", "영어", "일본어"]
    musics = []
    try:
        with open("music.dat", "r", encoding="utf-8") as f:
            for line in f:
                data = line.replace("**,", "{}").split(",")
                if len(data) == 4:
                    data[0] = data[0].replace("{}", "**,")
                    data[1] = data[1].replace("{}", "**,")
                    musics.append(Music(*map(str.strip, data)))
                else:
                    codeexit('지정된 형식의 dat 파일이 아닙니다. ","의 개수와 파일정보를 확인하세요.')
            for music in musics:
                if music.getGenre() not in genreType or music.getLanguage() not in languageType:
                    codeexit("지정된 형식의 장르 또는 언어가 아닙니다.")
    except FileNotFoundError:
        pass

    while True:
        commandNum = input("[메뉴] 1: 음원 저장, 2: 음원 조회, 3: 음원 수정, 4: 음원 삭제, 5: 음원 추천, 6: 종료 및 저장 : ")
        if commandNum == "1":  # 음원 저장
            try:
                musicTitle = input('[저장] 저장할 음원의 제목을 입력하세요 : ').replace(",", "**,")
                musicArtist = input('[저장] 저장할 음원의 가수를 입력하세요 : ').replace(",", "**,")
                musicGenre = input('[저장] 저장할 음원의 장르를 입력하세요 : ')
                if musicGenre not in genreType:
                    raise InvailedInput

                musicLanguage = input('[저장] 저장할 음원의 언어를 입력하세요 : ')
                if musicLanguage not in languageType:
                    raise InvailedInput

                if len(musics) == 0:
                    musics.append(Music(musicTitle, musicArtist, musicGenre, musicLanguage))
                else:
                    check = True
                    for music in musics:
                        if music.getTitle() == musicTitle and music.getArtist() == musicArtist and music.getGenre() == musicGenre and music.getLanguage() == musicLanguage:
                            print("이미 존재하는 음원입니다.")
                            check = False
                            break
                    if check:
                        musics.append(Music(musicTitle, musicArtist, musicGenre, musicLanguage))

            except InvailedInput as e:
                print(e)
                continue
        elif commandNum == "2":  # 음원 조회
            checkMusic()
        elif commandNum == "3":  # 음원 수정
            toggle3 = checkMusic()
            if toggle3 == 1:
                continue
            try:
                musicInfo1 = input('[수정] 수정할 음원의 제목 : ').replace(",", "**,")
                musicInfo2 = input('[수정] 수정할 음원의 가수 : ').replace(",", "**,")

                musicInfo3 = input('[수정] 수정할 음원의 장르 : ')
                if musicInfo3 not in genreType:
                    raise InvailedInput

                musicInfo4 = input('[수정] 수정할 음원의 언어 : ')
                if musicInfo4 not in languageType:
                    raise InvailedInput

            except InvailedInput as e:
                print(e)
                continue
            try:
                find_music = 0  # 0 : ( 존재하지 않는 음원에 대한 검색 실패 ) , 1 : ( 이미 존재하는 음원으로의 내용 변경 ) , 2 : ( 성공 )
                for music in musics:
                    if music.getTitle() == musicInfo1 and music.getArtist() == musicInfo2 and music.getGenre() == musicInfo3 and music.getLanguage() == musicInfo4:
                        print("음원 수정을 시작합니다.")
                        newInfo1 = input('[수정] 새로운 음원의 제목 : ').replace(",", "**,")
                        newInfo2 = input('[수정] 새로운 음원의 가수 : ').replace(",", "**,")

                        newInfo3 = input('[수정] 새로운 음원의 장르 : ')
                        if newInfo3 not in genreType:
                            raise InvailedInput
                        newInfo4 = input('[수정] 새로운 음원의 언어 : ')
                        if newInfo4 not in languageType:
                            raise InvailedInput

                        for chk_music in musics:
                            if chk_music.getTitle() == newInfo1 and chk_music.getArtist() == newInfo2 and chk_music.getGenre() == newInfo3 and chk_music.getLanguage() == newInfo4:
                                find_music = 1
                                break
                        if find_music == 1:
                            break

                        music.setTitle(newInfo1)
                        music.setArtist(newInfo2)
                        music.setGenre(newInfo3)
                        music.setLanguage(newInfo4)
                        print("음원 정보가 수정되었습니다...")
                        find_music = 2
                        break
                if find_music == 0:
                    print("해당 정보의 음원을 찾을 수 없습니다.")
                elif find_music == 1:
                    print("해당 음원이 이미 존재합니다.")
            except InvailedInput as e:
                print(e)
                continue
            except:
                codeexit("오류발생 프로그램 종료...")
        elif commandNum == "4":  # 음원 삭제
            toggle4 = checkMusic()
            if toggle4 == 1:
                continue
            if len(musics) == 0:
                print("빈 파일입니다.")
                continue
            musicInfo1 = input('[삭제] 삭제할 음원의 제목 : ').replace(",", "**,")
            musicInfo2 = input('[삭제] 삭제할 음원의 가수 : ').replace(",", "**,")
            musicInfo3 = input('[삭제] 삭제할 음원의 장르 : ')
            musicInfo4 = input('[삭제] 삭제할 음원의 언어 : ')

            for i, music in enumerate(musics):
                if music.getTitle() == musicInfo1 and music.getArtist() == musicInfo2 and music.getGenre() == \
                        musicInfo3 and music.getLanguage() == musicInfo4:
                    del musics[i]
                    print("음원이 삭제되었습니다.")
                    break
            else:
                print("해당 정보의 음원을 찾을 수 없습니다.")

        elif commandNum == "5":  # 음원 추천
            if len(musics) == 0:
                print("추천할 음원이 없습니다! 음원을 먼저 저장 해주세요!")
                continue
            try:
                with open("history.dat", "r", encoding="utf-8") as f:
                    histories = []
                    for line in f:
                        data = line.replace("**,", "{}").split(",")
                        if len(data) == 4:
                            data[0] = data[0].replace("{}", "**,")
                            data[1] = data[1].replace("{}", "**,")
                            histories.append(Music(*map(str.strip, data)))
                        else:
                            print('지정된 형식의 dat 파일이 아닙니다. history파일의 ","의 개수와 정보를 확인하세요. ')
                            continue

                    if len(histories) == 0:
                        print("history 파일이 비었습니다. 파일의 정보를 확인하세요")
                        continue
                    max_sim = -1  # 범위 : -1 <= cos_sim <= 1 이므로 최솟값 지정
                    max_music = None
                    for history in histories:
                        for music in musics:
                            his_vector = np.array(
                                [sum(map(ord, history.artist.replace("**,", ","))), sum(map(ord, history.genre)),
                                 sum(map(ord, history.language))])
                            music_vector = np.array(
                                [sum(map(ord, music.artist.replace("**,", ","))), sum(map(ord, music.genre)),
                                 sum(map(ord, music.language))])

                            cos_sim = dot(his_vector, music_vector) / (norm(his_vector) * norm(music_vector))

                            if cos_sim > max_sim:
                                max_sim = cos_sim
                                max_music = music

                    print(f"[추천 음원]\n{max_music}")
            except FileNotFoundError:
                print("지정된 파일이 존재하지 않습니다. 파일 위치를 확인해주세요.")
                continue

        elif commandNum == "6":  # 종료
            print("종료합니다...", end="")
            exitNum = "1"
            break
        else:
            print("잘못된 입력입니다.")

    if exitNum == "1":  # 저장
        with open("music.dat", "w", encoding="utf-8") as f:
            f.write('\n'.join(f"{music.title}, {music.artist}, {music.genre}, {music.language}" for music in musics))
            print("저장완료...")
