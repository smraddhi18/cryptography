j=0
p=[1,2,2,2]
k=[1,2,3,6]
T=[1,2,3,6,1,2,3,6]
S=[0,0,0,0,0,0,0,0]
c=0
for i in range(0,8):
    S[i]=i
for i in range(0,8):
    j=(j+S[i]+T[i])%8
    c=S[i]
    S[i]=S[j]
    S[j]=c
i=0
j=0
# for i in range (0,8):
#     print(S[i])
for q in range(0,4):
    i=(i+1)%8
   
    j=(j+S[i])%8
  
    c=S[i]
    S[i]=S[j]
    S[j]=c
    t=(S[i]+S[j])%8
    #print(t)
    k=S[t]
    # print(k)
    p[q]=p[q]^k

print("Encrypted Text",p)