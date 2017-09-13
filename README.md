# FaceDetectMajordomo
Определение пользователя по датчику движения http://blog.gelezako.com

Настройка:
1. Скачать видео плеер ffmpeg и положить его в папку C:\_majordomo\apps. Необходим что бы делать фото, когда будет зафиксировано движение.
2. Создать папку facedetect в C:\_majordomo\apps\ и положить туда содержимое проекта.
3. Подменить файлы standard_Alex.jpg на свои и разархивировать архивы.
4. В Majordomo создать свойства Euclid_Vika и Euclid_Alex для хранения значение от нейронной сети. Создать методы CheckFaceAlex и CheckFaceVika. В настройках этих свойств указать что запускать соотвествующий метод при изменении. Создать метод Morning.
5. Подключить Arduino+Ethernet+HC-SR501 датчик для опредления движения. https://github.com/Gelezako/MQ2-MQ135-DHT22-HC-SR501-MQTT-Ethernet-Majordomo/blob/master/HC-SR501-Ethernet-Majordomo.ino
6. Приявзать значение датчика к свойству Kitchen.HCSR501. В настройках свойства указать что запускать метод Kitchen.HCSR501Move при изменении.
