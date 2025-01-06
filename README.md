Projenin amacı deprem anında proje kullanıcılarına uyarı vermek aynı zaman binada hasarın olup olmadığını ilgili kurumlara bildirmektir. Deprem titreşimini (sw420), duvar eğimini (jiroskop) ölçen uyarı vermek için ses (buzzer) ve ışık (led) çıkaran donanımlar projede kullanılmıştır. Proje Raspberry pi gömülü bilgisayarı üzerinde ayağa kaldırılmıştır
Sistemdeki  jiroskop modülü sistemin sabitlenmiş olduğu duvarın yıkılma veya herhangi bir hasar alması durumunda duvar eğimindeki değişiklikleri hesaplayarak uyarısını vermektedir. 
Bu proje deprem bölgelerindeki riskli binalara entegre edilerek depremden dakikalar sonra bir hasar raporunun alınmasını mümkün kılabilir. Projenin bu anlamda hayata geçmesi için en önemli etken ise 
bu gömülü sistemin bağlı olduğu network'ün deprem anında çökmeden bildirimlerin ilgili kurumlara iletilmesini sağlamaktan geçmekterdir.



Ana proje görseli.
![resim](https://github.com/user-attachments/assets/f659023c-6ed5-47b3-ab4d-883ecdf7891e)


Proje uygulamasında kullanılan donanımlar detaylı olarak şu şekildedir.
1.	MPU6050 jiroskop modülü
2.	SW-420 titreşim modülü
3.	11 adet jumper kablo
4.	1 adet led
5.	1 adet direnç
6.	1 adet buzzer
7.	1 adet breadboard
8.	1 adet Raspberry pi
Yukarıda listelediğim modüllerin gpio bağlantıları ise şu şekildir.
buzzer_pin = 24
led_pin = 27
sw-420 = 17
jireskop i2c üzerinden haberleşmektedir ve adresi = 0x68.



![resim](https://github.com/user-attachments/assets/e2b0855e-afb8-44aa-aefb-39bbe9c9eefa)

![resim](https://github.com/user-attachments/assets/f7912139-12a6-453d-a61b-7f6210007bba)



Jiroskop, led, buzzer, sw-420

Projenin kodlama kısmında Python kullanılmıştır ve modüler bir kodlama sistemiyle kodlanmıştır. RPi.GPIO ,time, subprocess, smbus, math, EmailMessage, ssl, smtplib
adlı Python kütüphaneleri projeye dahil edilmiştir.

Proje son aşamada başarıyla çalışmıştır. Deprem sırasında uyarı verme, duvarın eğimini ölçüp ilgili kurumlara mail atma, ve deprem titreşimi algılama aşamalarının hepsini başarıyla geçmiştir.
