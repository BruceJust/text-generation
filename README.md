# text-generation
text generation based on book Winston Churchil

本案例中尝试了从字符、词两个角度进行文本生成的训练
主要算法均是BI-LSTM，不同之处在于词模型下需要进行word embedding，而字符模型下不需要



词模型下训练了50个epoch， loss降到1.4855

55552/55552 [==============================] - 11s 199us/sample - loss: 1.4855

词模型下训练了50个epoch， loss降到2.1065

276730/276730 [==============================] - 53s 193us/sample - loss: 2.1065

测试：
直接python test.py 即可执行，内置了一句话用于预测，默认以词模型运行预测
也可以指定参数来选择模型和自定义初始文本

python test.py 
  --type='char' 
  --input='His object in coming to New York was to engage officers for'

注意：词模型下请保证输入词长度大于10， 字符模型下输入字符长度超过50.


测试input
词模型测试结果：
his object in coming to new york was to engage officers for the island of the island of the hawaiian isles and timok , and the f
irst cornelius the expedition was saved in the massive beams of the united states . in the time of the united states of the legitimists . the soun
ds were sharp and for them in the provisional government of the united states , bearded , and the bullets asked to prevent a dozen shells to the u
nited states , and acquitted . the first cornelius the legitimists were to be admitted to the united states . in this moment burnham was personall
y , and in the very time of the “ book ” of the rebellion , in the rebellion , in which he had been brought him to the viceroy , but i have been
 born in the new guinea , and stephen had been brought him to the sincere child of the house , when he had been sent , and the charm of the tuiler
ies that the shells bursting of the service and two hundred and fifty thousand . in the south war the enemy held the enemy and a quarrel on the st
age of chivalry , the general , with the influences of


字符模型测试结果：
 his object in coming to new york was to engage officers for the island of the island of the hawaiian isles and timok , and the f
irst cornelius the expedition was saved in the massive beams of the united states . in the time of the united states of the legitimists . the soun
ds were sharp and for them in the provisional government of the united states , bearded , and the bullets asked to prevent a dozen shells to the u
nited states , and acquitted . the first cornelius the legitimists were to be admitted to the united states . in this moment burnham was personall
y , and in the very time of the “ book ” of the rebellion , in the rebellion , in which he had been brought him to the viceroy , but i have been
 born in the new guinea , and stephen had been brought him to the sincere child of the house , when he had been sent , and the charm of the tuiler
ies that the shells bursting of the service and two hundred and fifty thousand . in the south war the enemy held the enemy and a quarrel on the st
age of chivalry , the general , with the influences of
