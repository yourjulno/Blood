
##########################################################################################################################################################################

###################################################################       Без физ нагрузки       #########################################################################
restData, duration, count = blood.read('rest.txt')
t = np.linspace(0, duration, count)
plt.plot(t, np.polyval(np.polyfit(adc, pressures, 1), restData),  marker = '.', markersize = 7, markevery=[54000, 493000], mfc = 'r', mec = 'r')
plt.text(3.8, 248, 'Сатирические давление', fontsize = 13)
plt.text(33, 64, 'Диастолическое давление', fontsize = 13)
plt.title('Зависимость давления от времени без физ. нагрузки', fontsize = 20)
plt.ylabel('P, mmHg', fontsize = 20)
plt.xlabel('t, с', fontsize = 20)
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)
plt.show()
####################################################################################
temp = np.polyval(np.polyfit(adc, pressures, 1), restData)  
k = np.polyfit(t[150000:300000], np.polyval(np.polyfit(adc, pressures, 1), restData)[150000:300000], 1)[0]
b = np.polyfit(t[150000:300000], np.polyval(np.polyfit(adc, pressures, 1), restData)[150000:300000], 1)[1]
for i in range(300000):
    temp[i] = temp[i] - k * t[i] - b
plt.title('Пульс до физической нагрузки', fontsize = 20, )
plt.ylabel('Изменение давления в артерии [мм рт. ст.]', fontsize = 20)
plt.xlabel('Время [с]', fontsize = 20)
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)

plt.plot(t[150000:300000], temp[150000:300000])
plt.show()
##########################################################################################################################################################################

################################################################       С физ нагрузки       ##############################################################################
fitnessData, duration, count = blood.read('fitness.txt')
t = np.linspace(0, duration, count)
plt.plot(t, np.polyval(np.polyfit(adc, pressures, 1), fitnessData), marker = '.', markersize = 7, markevery=[97500, 500000], mfc = 'r', mec = 'r')
plt.text(7, 248, 'Сатирические давление', fontsize = 13)
plt.text(33, 64, 'Диастолическое давление', fontsize = 13)
plt.title('Зависимость давления от времени с физ. нагрузкой', fontsize = 20)
plt.ylabel('P, mmHg', fontsize = 20)
plt.xlabel('t, с', fontsize = 20)
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)
plt.show()
####################################################################################
temp = np.polyval(np.polyfit(adc, pressures, 1), fitnessData)  
k = np.polyfit(t[150000:300000], np.polyval(np.polyfit(adc, pressures, 1), fitnessData)[150000:300000], 1)[0]
b = np.polyfit(t[150000:300000], np.polyval(np.polyfit(adc, pressures, 1), fitnessData)[150000:300000], 1)[1]
for i in range(300000):
    temp[i] = temp[i] - k * t[i] - b
plt.title('Пульс после физической нагрузки', fontsize = 20)
plt.ylabel('Изменение давления в артерии [мм рт. ст.]', fontsize = 20)
plt.xlabel('Время [с]', fontsize = 20)
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)

plt.plot(t[150000:300000], temp[150000:300000])
plt.show()
##########################################################################################################################################################################
