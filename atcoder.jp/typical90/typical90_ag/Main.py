##コーナーケース(条件で完全に含まれる2✖️2を参照する→1✖️nは不適切でない)

H,W=map(int,input().split())

if min(H,W)==1:
    print(max(H,W))
else:
    print(((H+1)//2)*((W+1)//2))  #Hが奇数偶数でも切り捨てなので正解