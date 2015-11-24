function [x,y,L,T]=m4_3_2(t)
H=120;Ve=90;Vw=450;
x(1)=0;y(1)=0;T(1)=0;
for i=1:10e6
    M=(Ve*T(i)-x(i))/(H-y(i));
    xx(i+1)=x(i)+Vw*t/sqrt(1+1/M.^2);
    yy(i+1)=y(i)+Vw*t/sqrt(1+M.^2);
    T(i+1)=i*t;
    N=(Ve*T(i+1)-xx(i+1))/(H-yy(i+1));
    x(i+1)=0.5*(xx(i+1)+x(i)+Vw*t/sqrt(1+1/N.^2));
    y(i+1)=0.5*(yy(i+1)+y(i)+Vw*t/sqrt(1+N.^2));
    if y(i+1)>=H
        break
    end
end
L=x(i+1);
T=x(i+1)/Ve;