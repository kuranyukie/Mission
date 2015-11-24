function [x,y,L,T]=m4_4(t)
H=120;Ve=90;Vw=450;
x(1)=0;y(1)=0;
for i=1:10e6
    M=sqrt(((i-1)*Ve*t-x(i)).^2+(H-y(i)).^b b2);
    ctheta=((i-1)*Ve*t-x(i))./M;
    stheta=(H-y(i))./M;
    x(i+1)=x(i)+Vw*t*ctheta;
    y(i+1)=y(i)+Vw*t*stheta;
    if y(i+1)>=H
        break;
    end
end
L=x(i+1);
T=x(i+1)/Ve;