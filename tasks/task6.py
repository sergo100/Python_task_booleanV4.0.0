# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(int, input().split())
    hyp = max(a, b, c)
    print(a * a + b * b + c * c == 2 * hyp * hyp)
   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()