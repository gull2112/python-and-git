
#colortype 클래스
#퍼스널 컬러의 색상 유형을 정의합니다
class ColorType:
    def __init__(self, name, hex_code, rgb_values):
        self.name = name  # 색상 이름
        self.hex_code = hex_code  # 헥스 코드
        self.rgb_values = rgb_values  # RGB 값

    def display_info(self):
        return f"{self.name}: {self.hex_code}, RGB: {self.rgb_values}"

#season 클래스
#퍼스널 컬러의 계절을 정의합니다
class Season:
    def __init__(self, name, dominant_colors):
        self.name = name  # 계절 이름
        self.dominant_colors = dominant_colors  # 주요 색상 리스트

    def add_color(self, color):
        self.dominant_colors.append(color)  # 주요 색상 추가

    def get_colors(self):
        return [color.display_info() for color in self.dominant_colors]  # 색상 정보 반환

#PersonalColor 클래스
#개인의 퍼스널 컬러를 정의합니다
class PersonalColor:
    def __init__(self, name, season, characteristics):
        self.name = name  # 개인 이름
        self.season = season  # 계절 객체
        self.characteristics = characteristics  # 특성

    def recommend_colors(self):
        return self.season.get_colors()  # 추천 색상 반환

    def display_info(self):
        return f"Name: {self.name}, Season: {self.season.name}, Characteristics: {self.characteristics}"

    def add_season_color(self, color):
        self.season.add_color(color)  # 계절에 색상 추가
#사용 예시
# 색상 생성
red = ColorType("Red", "#FF0000", (255, 0, 0))
blue = ColorType("Blue", "#0000FF", (0, 0, 255))
green = ColorType("Green", "#00FF00", (0, 255, 0))

# 계절 생성
summer = Season("Summer", [red, blue])

# 개인 컬러 생성
person = PersonalColor("Alice", summer, "Warm undertones")

# 색상 추천
print(person.recommend_colors())

# 개인 정보 출력
print(person.display_info())

# 새로운 색상 추가
yellow = ColorType("Yellow", "#FFFF00", (255, 255, 0))
person.add_season_color(yellow)

# 업데이트된 색상 추천
print(person.recommend_colors())










