function m4_6_plot(t,alphas)
%axis equal
i=1;

for alpha=alphas
    [xw,yw,xe,ye,k,distance,T]=m4_6(t,alpha);
    plot(xw,yw,'.-');
    hold on
    plot(xe,ye,'x-');
    hold on
    alpha
    T
    Ts(i)=T;
    i=i+1;
end
title('ทยีๆ-Question5');
axis([0 100 0 200]);
set(gca,'XTick',0:20:200);
set(gca,'YTick',0:20:200);
xlabel('x');
ylabel('y');
box off
% alphas
% Ts
% plot(alphas, Ts);
% title('alpha-T');