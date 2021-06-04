# jackett

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square)

Jackett - A proxy for applications like Sonarr, Radarr, SickRage, and CouchPotato.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"linuxserver/jackett"` |  |
| image.tag | string | `"latest"` |  |
| internalPort | int | `9117` |  |
| name | string | `"jackett"` |  |
| replicaCount | int | `1` |  |
| resources.limits.memory | string | `"1Gi"` |  |
| resources.requests.cpu | float | `0.5` |  |
| resources.requests.memory | string | `"1Gi"` |  |
| timezone | string | `"America/Chicago"` |  |
| userId | int | `1000` |  |
| volumeMounts[0].mountPath | string | `"/config"` |  |
| volumeMounts[0].name | string | `"jackett-config"` |  |
| volumeMounts[1].mountPath | string | `"/downloads"` |  |
| volumeMounts[1].name | string | `"torrent-downloads"` |  |
| volumes[0].hostPath.path | string | `"/data"` |  |
| volumes[0].name | string | `"jackett-config"` |  |

