class Square:
    def __init__(self):
        self.square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>> '))

        if self.square == 1:
            print('직사각형 함수는 rect()입니다.')
            print(self.rect())  # 직사각형 함수 실행 및 출력

        elif self.square == 2:
            print('평행사변형 함수는 par()입니다.')
            print(self.par())  # 평행사변형 함수 실행 및 출력

        elif self.square == 3:
            print('사다리꼴 함수는 trape()입니다.')
            print(self.trape())  # 사다리꼴 함수 실행 및 출력

        else:
            print('1, 2, 3 중에서 다시 입력해주세요')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>> ').split(','))
        area = width * vertical
        return f'직사각형의 넓이는 : {area}'

    def par(self):
        base, height = map(int, input('밑변, 높이를 입력하세요. 예시 : 밑변,높이\n >>> ').split(','))
        area = base * height
        return f'평행사변형의 넓이는 : {area}'

    def trape(self):
        top, bottom, height = map(int, input('윗변, 아랫변, 높이를 입력하세요. 예시 : 윗변,아랫변,높이\n >>> ').split(','))
        area = (top + bottom) * height / 2
        return f'사다리꼴의 넓이는 : {area}'

a = Square()
