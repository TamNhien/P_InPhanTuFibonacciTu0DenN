def fibonacci(n):
    fib_list = [0, 1]
    while fib_list[-1] < n: fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:-1]

def main():
    n = int(input("Nhập n: "))
    print("Các số Fibonacci từ 0 đến", n, "là :", fibonacci(n))

if __name__ == "__main__":
    main()
