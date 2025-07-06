import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını doğru şekilde oku: ; ile ayrılmış ve ondalık , ile
df = pd.read_csv(
    r"C:\Users\Asus\Documents\GitHub\solar_maintenance_data.csv",
    sep=";",
    decimal=","
)

# Sütun adlarındaki boşlukları temizle
df.columns = df.columns.str.strip()

# Bakım yapılan ve yapılmayan günleri ayır
bakim_var = df[df["maintenance_done"] == 1]
bakim_yok = df[df["maintenance_done"] == 0]

# Ortalama enerji üretimlerini hesapla
ortalama_bakim_var = bakim_var["energy_output_kWh"].mean()
ortalama_bakim_yok = bakim_yok["energy_output_kWh"].mean()

# Sonuçları yazdır
print(f"✅ Bakım yapılan günlerde ortalama üretim: {ortalama_bakim_var:.2f} kWh")
print(f"❌ Bakım yapılmayan günlerde ortalama üretim: {ortalama_bakim_yok:.2f} kWh")

# Bar grafiği ile görselleştir
etiketler = ["Bakım Yapıldı", "Bakım Yapılmadı"]
ortalama_uretim = [ortalama_bakim_var, ortalama_bakim_yok]

plt.bar(etiketler, ortalama_uretim, color=["green", "red"])
plt.title("Bakım Durumuna Göre Ortalama Enerji Üretimi")
plt.ylabel("Ortalama Enerji Üretimi (kWh)")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df["date"], df["energy_output_kWh"], color="blue")
plt.title("Zamana Göre Enerji Üretimi")
plt.xlabel("Tarih")
plt.ylabel("Enerji Üretimi (kWh)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import seaborn as sns

sns.boxplot(x="maintenance_done", y="energy_output_kWh", data=df)
plt.title("Bakım Durumuna Göre Üretim Dağılımı")
plt.xlabel("Bakım (0 = Yok, 1 = Var)")
plt.ylabel("Enerji Üretimi (kWh)")
plt.show()

artis_yuzdesi = ((ortalama_bakim_var - ortalama_bakim_yok) / ortalama_bakim_yok) * 100
print(f"Bakım yapılan panellerde üretim % {artis_yuzdesi:.2f} daha fazla.")
