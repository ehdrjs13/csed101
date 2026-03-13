def sec_to_hms(sec) -> list:
    h = sec // 3600
    s = sec % 3600
    m = s // 60
    s = s % 60

    return [h,m,s]

second = int(input("초를 입력하세요. :"))
ans = sec_to_hms(second)

print(f"{second}초는 {ans[0]}시간 {ans[1]}분 {ans[2]}초 입니다. ")
    