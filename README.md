# Connect-4
This is connect 4 game. It was made within the scope of File Organization course. There are special requirements. Please read  for the explanation of these requirements.




File Organization Projesi 2023

Projede dosya yapıları kullanarak Connect 4 oyunu kodlanacaktır.

Aşağıdaki resimdeki gibi dik duran örnek tahta üzerinde oynanmaktadır. Tahta dik durduğundan
yerçekimi dolayısıyla herhangi bir kolon üzerinden bırakılan pul bir pula rastlayana kadar aşağı
düşmeye devam edecektir. Her kolon birbirinden bağımsızdır. Bu yüzden bir kolondan bırakılan
taş başka kolona kayıp düşememektedir. (Aşağıdaki hareketli gif dosyasında da görüldüğü gibi)
Oyundaki amaç diğer oyuncudan daha önce kendi rengindeki pulları çapraz, yatay veya düşey
olarak 4 pulunu hizalamaktır. Aşağıdaki örnekte kırmızı pullara sahip oyuncu oyunu 4 pulunu
çapraz olarak hizalayarak kazanmaktadır.

2 oyuncu oynayabilmektedir. 2 farklı renkte pullarla oynanacaktır. Pulların renk veya gösterim
şeklini tamamen öğrenci belirleyecektir. Yukarıdaki örnek gif dosyasında 7x6 lık tahtada
oynanmaktadır. Fakat bu proje 9x9 tahta üzerinde gerçekleştirilecektir.
Oyunun kuralları:
1. Oyuna başlamak için oyucuların hangi tipte(renkte) pulla oynayacağı kura ile
seçilecektir.
2. Sonrasında kurayı kazanan oyuncu ilk pulunu oynar.

3. Ardından oyuncular hep sırayla(Round Robin) oynamaya devam eder.
4. Her oyuncunun 40 tane pulu vardır. 80 adet pul oynandığında hala kazanan yoksa oyunun
berebere bittiği oyunculara bildirilerek oyun sonlandırılır.
5. Herhangi bir şekilde oyunun bir anında bir oyuncu oyunu kazanmasını sağlayan duruma
gelirse kazanan olarak belirlenecektir.
6. Oyunculara birer isim baştan verilerek daha sonra karışıklık olması engellenecektir.
Yukarıdaki tahta ister konsolda çizdirilecek ister görsel kullanılıp pulların yeri gösterilecek.
Oyunda iki tane metin dosyası kullanılacak. Biri Tahta.txt(9x9 luk tahtada her slot boş veya
herhangi bir oyuncunun pulu ile işgal edildiği kaydedilecek ve her oyuncunun hamlesi sonrası
güncellenecek)Diğer dosyanın ismi de Hamle.txt olacak ve Her oyuncunun yaptığı hamle oraya
işlenecek(yine her hamle sonrası) Tahta önce satır sonra sütun olarak adreslenecek ve oynanan her
pul hangi adrese yerleşti o durum dosyaya yazılacaktır. (mesela 57 dendiğinde 5.satır 7.sütun
anlamına gelecektir vb.
Oyunu her oyuncu istediği ana yarıda bırakıp çıkılabilecektir. Başlangıç menüsünde oyuna devam
et seçeneği seçildiğinde dosyalardan durum okunup oyun kaldığı yerden devam edecek.
