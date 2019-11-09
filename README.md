# MapaTasas

Comparativa de precios universitarios del territorio español.

Los navegadores utilizan estrictas políticas de permisos para prevenir que puedas leer archivos del sistema de ficheros. Para visualizar localmente el proyecto, debes acceder a través de un servidor web. Por ejemplo:

```bash
npm install -g http-server
http-server
```

Para validr los datos de `unis.yaml` contra el esquema, necesitamos el paquete de python3 `pykwalify` y ejecutar:

```bash
pykwalify -s data/uni/schema.yaml -d data/uni/unis.yaml -e data/uni/extensions.py
```

Para poder visualizarlo: https://vk496.github.io/MapaTasas/