# draw a isosceles triangle
def draw_triangle(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (i*2 + 1))

def main():
    done = False
    while not done:
        height = int(input("Please enter the height of a triangle: "))
        draw_triangle(height)
        ans = input("Do you want to quit? [Y/N]: ").upper()
        if ans == "Y":
            done = True
main()
