function net = BP_train(inputmar,outputmar)%������������ѵ���������0,1
%�������
bpinput = inputmar';
output = outputmar';
%net = newff( minmax(input) ,[4 4] ,{'logsig' 'purelin'},'traingdx'); 
net = newff(bpinput,output,[7 5 3]); 
%����ѵ������
net.trainparam.show=50;
net.trainparam.epochs=500;
net.trainparam.goal=0.01;
net.trainParam.lr=0.01;

net = train(net,bpinput,output);
end