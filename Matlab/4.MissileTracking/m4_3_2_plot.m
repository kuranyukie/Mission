function m4_3_2_plot(tt)
axis equal
ylim([0,120]);
for t=tt
    [x,y,L,T]=m4_3_2(t);
    plot(x,y,'.-');
    hold on
    t
    L
    T
end
set(gca,'XTick',0:2:30);
set(gca,'YTick',0:10:140);
title('¸Ä½øEuler');
xlabel('x');
ylabel('y');
box off
