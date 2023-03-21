# Mo file input va doc du lieu
with open("/home/ibeos/Python/ex3Py/input.txt", 'r') as file:
    numbers = list(map(int, file.read().split()))

# tao bien de luu so luong so chan, le, so nguyen, so nguyen to, so xuat hien nhieu nhat
even_count = 0
odd_count = 0
# prime_count = 0
max_count = 0
most_frequent = None

# !tao danh sach luu cac so nguyen to da tim thay trong input
primes = set()

# duyet qua tung phan tu trong list, kiem tra dieu kien de tang gia tri bien
for num in numbers:
    # *Chan,le
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # so nguyen to (bao gom cac so trung nhau)
    # is_prime = True
    # if num < 2:
    #     is_prime = False
    # else:
    #     for i in range(2, int(num**0.5) + 1):
    #         if num % i == 0:
    #             is_prime = False
    #             break
    # if is_prime:
    #     prime_count += 1

    # *So nguyen to (da loai tru cac so trung nhau)
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        primes.add(num)

    # *Xuat hien nhieu nhat
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        most_frequent = num

print(f"Co {even_count} so chan")
print(f"Co {odd_count} le")
# print(f"Co {prime_count} so nguyen to")
print(f"So luong so nguyen to: {len(primes)}")
print(f"So xuat hien nhieu nhat la: {most_frequent} ({max_count} lan)")