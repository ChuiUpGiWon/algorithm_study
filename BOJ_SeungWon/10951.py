while True:
    try: # 정수 a,b를 입력받은 경우 a+b출력
        a,b=map(int,input().split())
        print(a+b)
    except: # try에러 발생한 경우 (여기서는 입력없는 경우)
        break # while 종료
