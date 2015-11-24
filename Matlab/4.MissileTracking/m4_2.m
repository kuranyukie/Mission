function m4_2(N)
k=1;
H=120;
for n=N
    h=H/n;
    lambda=90/450;
    x0=0;p0=0;
    for i=0:n-1
        x1=x0+h*p0;
        p1=p0+h*(lambda*sqrt(1+p0^2)/(H-i*h));
        x0=x1;
        p0=p1;
    end
    L(k)=x1;
    T(k)=x1/90;
    k=k+1;
end
N
L
T
