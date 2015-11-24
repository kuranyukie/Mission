function m4_5_plot(tt)
axis equal
ylim([0,120]);
for t=tt
    [xw,yw,xe,ye,k,distance,T]=m4_5(t);
    plot(xw,yw,'.-');
    hold on
    plot(xe,ye,'x-');
    hold on
    t
    xw(k+1)
    yw(k+1)
    distance
    T
end
set(gca,'XTick',0:5:100);
set(gca,'YTick',0:10:140);
title('ทยีๆ-Question4');
xlabel('x');
ylabel('y');
box off
