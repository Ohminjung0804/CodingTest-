'''
타일을 'R', 'G', 'B' 색으로 칠하려 합니다.
R 색으로는 3칸을 한 번에, G 색으로는 2칸을 한 번에 칠할 수 있으며, B 색으로는 1칸을 칠할 수 있습니다.
색은 R, G, B 순서로 한 번씩 번갈아 가면서 사용해야 하며, 타일의 길이를 넘겨서 칠할 수는 없습니다.

예를 들어, 타일 길이가 11이면 "RRRGGBRRRGG"의 색으로 칠할 수 있습니다.

타일 길이가 매개변수 tile_length로 주어질 때, 타일을 색칠한 순서를 문자열로 return하는 solution 함수를 작성하려 합니다.
빈칸을 채워 전체 코드를 완성해주세요.

순서에 맞게 타일을 칠할 수 없다면 -1을 return 해주세요.

'''
def solution(tile_length):
   answer = ''
   com = 'RRRGGB'
   if tile_length%6 == 1 or tile_length%6 == 2 or tile_length%6 == 3:
       answer = '-1'
   else:
       for i in range(tile_length):
           answer += com[i % 6]
   return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
tile_length1 = 11
ret1 = solution(tile_length1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

tile_length2 = 16
ret2 = solution(tile_length2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")