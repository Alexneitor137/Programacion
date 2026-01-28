Descargar:

https://www.mongodb.com/try/download/community

O bien Windows x64
O bien Ubuntu 24.04 x64

Si la instalación os dice de instalar
el MongoCompass: SI que lo queréis
(Es la UI por defecto para Mongo)

https://www.mongodb.com/docs/compass/install/?operating-system=linux&package-type=.deb

Download MongoDB Compass.

wget https://downloads.mongodb.com/compass/mongodb-compass_1.46.10_amd64.deb

Install MongoDB Compass.

sudo apt install ./mongodb-compass_1.46.10_amd64.deb

If your Linux distribution does not support using apt for installing local .deb files, run the following lines to install MongoDB Compass:

sudo dpkg -i mongodb-compass_1.46.10_amd64.deb
sudo apt-get install -f # This installs required compass dependencies

Start MongoDB Compass.

mongodb-compass