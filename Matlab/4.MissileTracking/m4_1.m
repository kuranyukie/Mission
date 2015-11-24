function m4_1(n)
H=120;
h=H/n;
lambda=90/450;
x(1)=0;p(1)=0;
y=0:h:H;
for i=0:n-1
    x(i+2)=x(i+1)+h*p(i+1);
    p(i+2)=p(i+1)+h*(lambda*sqrt(1+p(i+1)^2)/(H-y(i+1)));
end

x
p
L=x(n+1)
T=x(n+1)/90