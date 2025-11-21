# mosquitto-cont
Contenedor con mqtt


Instalación del contenedor
Intancia aws linux
- **Nota**: Se recomeindo ejecutar linea por linea los comandos


### Instalar Git
```
sudo dnf install -y git
```
### Instalar Docker
```
sudo dnf install -y docker
sudo dnf install -y curl
sudo mkdir -p /usr/local/lib/docker/cli-plugins

sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
  -o /usr/local/lib/docker/cli-plugins/docker-compose

sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

docker compose version

```
### Habilitar docker
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
```

### Iniciar el broker
```
git clone https://github.com/jonapt/mosquitto-cont.git
cd mosquitto-cont
sudo docker compose up -d
```

### Crear usuario
```
./users/create_user.sh [User] [Password]
```

### Reiniciar broker
```
docker compose down
docker compose up -d
```


