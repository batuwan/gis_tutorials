import geopandas as gpd
import matplotlib.pyplot as plt

# Çalışılacak katmanın içe aktarılması.
# Istanbul_Nufus_Geopandas klasöründe bulunan "shapefile" dosyası okutulmalıdır !
istanbul_nufus = gpd.read_file("istanbul_nufus.shp")

fig = istanbul_nufus.plot(column = "2019_pop", #Kullanılacak sütun
                          scheme = "quantiles", #Sınıflandırma şeması
                          cmap = "autumn_r", #Renk paleti
                          legend = "True", #Lejant ekleme
                          figsize =(15,10)) #Şeklin boyutu

plt.title("İstanbul İlçe Nüfusları",fontsize = '20')
plt.show()
