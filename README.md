# FaceDetectMajordomo
Определение пользователя по датчику движения, видео инструкции:
Часть #1 https://www.youtube.com/watch?v=7k9tDY_ajrY
Часть #2 https://www.youtube.com/watch?v=rQYZWZetQ6Y

Блог http://blog.gelezako.com

Настройка:
1. Скачать видео плеер ffmpeg и положить его в папку C:\_majordomo\apps. Необходим что бы делать фото, когда будет зафиксировано движение.
Либо подключить IP камеру через простые устройства и делать скриншот используя встроенный метод.
2. Создать папку facedetect в C:\_majordomo\apps\ и положить туда содержимое проекта.
3. Подменить файлы standard_Alex.jpg на свои и разархивировать архивы.
4. В Majordomo создать свойство EuclidValue для хранения значение от нейронной сети. Создать метод CheckFace. В настройках этих свойств указать что запускать соотвествующий метод при изменении. Создать метод Morning.
5. Подключить Arduino+Ethernet+HC-SR501 датчик для опредления движения. https://github.com/Gelezako/MQ2-MQ135-DHT22-HC-SR501-MQTT-Ethernet-Majordomo/blob/master/HC-SR501-Ethernet-Majordomo.ino либо использовать Xiaomi датчик.
6. Приявзать значение датчика к свойству Kitchen.HCSR501. В настройках свойства указать что запускать метод Kitchen.HCSR501Move при изменении. Либо использовать метод motionDetected если датчик добавлен через модуль "простые устрйоства".
