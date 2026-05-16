a=8000*10
b=20000*10
i=2026
while a<b:
   a=((3/100)*a)+a
   b=((1.5/100)*b)+b
   print("-"*50)
   print(f"em {i}/ cidade A={a:.2f}/ cidade B={b:.2f}")
   i=i+1
   
