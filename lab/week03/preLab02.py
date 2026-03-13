def sec_to_hms(s) -> list:
    h = s // 3600
    s = s % 3600
    m = s // 60
    s = s % 60

    return h,m,s

second = int(input("초를 입력하세요. :"))
ans = sec_to_hms(second)

print(f"{second}초는 {ans[0]}시간 {ans[1]}분 {ans[2]}초 입니다. ")