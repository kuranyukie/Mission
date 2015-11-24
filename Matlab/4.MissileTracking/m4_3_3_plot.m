function m4_3_3_plot(tt)
axis equal
ylim([0,120]);
for t=tt
    [x,y,L,T]=m4_3(t);
    plot(x,y,'x-');
    hold on
end
t=tt(1);
[x,y,L,T]=m4_3_3(t);
plot(x,y,'o-');
hold on
t
L
T
set(gca,'XTick',0:2:30);
set(gca,'YTick',0:10:140);
title('Euler & ±ä²½³¤Euler');
xlabel('x');
ylabel('y');
box off
