# mosquitto-cont
Contenedor con mqtt


Instalación del contenedor
Intancia aws linux

### Instalar Git y Docker
```
sudo dnf install -y git
echo "Git Instalado"
sudo dnf install -y docker
echo "Docker Instalado"
git clone https://github.com/jonapt/mosquitto-cont.git
cd mosquitto-cont
```

### Habilitar docker
```
sudo systemctl enable docker
echo "Docker habilitado para cuando la instancia incie"
sudo systemctl start docker
echo "Docker iniciado"
sudo usermod -aG docker $USER
echo "Docker añadido al grupo"
```


