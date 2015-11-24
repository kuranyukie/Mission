function [x,y,L,T]=m4_3_3(t)
H=120;Ve=90;Vw=450;
x(1)=0;y(1)=0;T(1)=0;
for i=1:10e6
    M=(Ve*T(i)-x(i))/(H-y(i));
    x(i+1)=x(i)+Vw*t/sqrt(1+1/M.^2);
    y(i+1)=y(i)+Vw*t/sqrt(1+M.^2);
    T(i+1)=T(i)+t;
    if y(i+1)>=H
       x(i+1)=x(i);
       y(i+1)=y(i);
       T(i+1)=T(i);
       t=t/10;
    end
    if t<1e-8
        break
    end
end
L=x(i+1);
T=x(i+1)/Ve;