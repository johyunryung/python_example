import module1
import module2

def main():
    print("insa_func 모듈 입니다")
    print("__name__ : ", __name__)
    module1.hello()
    module2.greeting()

main()