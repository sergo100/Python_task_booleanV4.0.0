# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(int, input().split())
    print(a + b > c and a + c > b and b + c > a)
    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()