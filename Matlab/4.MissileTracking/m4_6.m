function [xw,yw,xe,ye,k,distance,T]=m4_6(t,alpha)
H=120;
Ve=135;Vw=450;
xw(1)=0;yw(1)=0;xe(1)=0;ye(1)=H;
T=0;
for k=1:10e6
    distance=sqrt((yw(k)-ye(k))^2+(xw(k)-xe(k))^2);
    theta=abs(atan((ye(k)-yw(k))/(xe(k)-xw(k))));
    ctheta=cos(theta)*sign(xe(k)-xw(k));
    stheta=sin(theta)*sign(ye(k)-yw(k));
    xw(k+1)=xw(k)+Vw*t*ctheta;
    yw(k+1)=yw(k)+Vw*t*stheta;
    theta=theta+pi*alpha/180;
    ctheta=cos(theta)*sign(xe(k)-xw(k));
    stheta=sin(theta)*sign(ye(k)-yw(k));
    xe(k+1)=xe(k)+Ve*t*stheta;
    ye(k+1)=ye(k)-Ve*t*ctheta;
    T=T+t;
    new_distance=sqrt((yw(k+1)-ye(k+1))^2+(xw(k+1)-xe(k+1))^2);
    if abs(new_distance-distance)<t*(Vw-Ve);
        break;
    end
end