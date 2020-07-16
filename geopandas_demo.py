import geopandas as gpd
import matplotlib.pyplot as plt

# Çalışılacak katmanın içe aktarılması.
istanbul_nufus = gpd.read_file("/home/batu/Desktop/Bitirme/öznitelikler/istanbul_nufus.shp")

fig = istanbul_nufus.plot(column = "2019_pop", #Kullanılacak sütun
                          scheme = "quantiles", #Sınıflandırma şeması
                          cmap = "autumn_r", #Renk paleti
                          legend = "True", #Lejant ekleme
                          figsize =(15,10)) #Şeklin boyutu

plt.title("İstanbul İlçe Nüfusları",fontsize = '20')
plt.show()
