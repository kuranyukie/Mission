function m4_4_plot(tt)
axis equal
ylim([0,120]);
for t=tt
    [x,y,L,T]=m4_4(t);
    plot(x,y,'.-');
    hold on
    t
    L
    T
end
set(gca,'XTick',0:2:30);
set(gca,'YTick',0:10:140);
title('ทยีๆ');
xlabel('x');
ylabel('y');
box off
