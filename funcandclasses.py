def cal_area(length, width):
    return length * width

def print_area(result):
    print("The area is:", result)

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

area = cal_area(l, b)
print_area(area)

