yosh=int(input("Yoshingiz nechida?>>>"))
if yosh<=4 or yosh>=60:
    narh=0
elif yosh<=18:
    narh=10000
elif yosh>18:
    narh=20000
print(f"Yoshingiz {yosh} bo'lganligi sabali,sizga chipta narxi {narh} so'm")    