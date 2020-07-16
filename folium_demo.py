import pandas as pd
import folium
from folium import Marker
from folium.plugins import MarkerCluster

map_1 = folium.Map(location=[41.20,29], tiles='openstreetmap', zoom_start=9)

########## İtfaiye İstasyonları Lokasyon Veri Seti, dosyanın lokasyonu belirtilerek "read_csv" fonksiyonu ile okunmalıdır! 

fire_stations = pd.read_csv("itfaiye_lokasyon.csv", encoding='UTF-8', sep= ';') 
print(fire_stations.head())

fire_stations.dropna(subset = ['ENLEM','BOYLAM','ITFAIYE_LOKASYON'], inplace=True)

marker_cluster = MarkerCluster()
for index, row in fire_stations.iterrows():
    # Marker([row['ENLEM'], row['BOYLAM']],popup=row['ITFAIYE_BIRIM_ADI']).add_to(map_1)
    marker_cluster.add_child(Marker([row['ENLEM'], row['BOYLAM']],popup=row['ITFAIYE_BIRIM_ADI']))
map_1.add_child(marker_cluster)


####Çıktı dosyanın ismi, kaydedileceği konum "save" fonksiyonunun içine yazılmalıdır.
####Bu haliyle '.py' uzantılı bu dosyanın bulunduğu konuma kaydedilecektir.

map_1.save('folium_demo.html') 
