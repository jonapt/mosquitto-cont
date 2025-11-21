# mosquitto-cont
Contenedor con mqtt


Instalación del contenedor
Intancia aws linux

### Instalar Git y Docker
```
sudo dnf install -y git
sudo dnf install -y docker
```

### Entrar a carpeta
```
git clone https://github.com/jonapt/mosquitto-cont.git
cd mosquitto-cont
```

### Habilitar docker
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
```


