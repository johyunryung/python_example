import area2 as ar
import sys
ar.print_area(10, 20)
ar.print_area(20, 30)

print(__name__)
print(ar.__name__)

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 3:
        ar.print_area(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print('python area_main.py 너비 높이')