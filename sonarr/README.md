# sonarr

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square)

Sonarr - An application for downloading TV shows via Usenet and Bittorrent

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"linuxserver/sonarr"` |  |
| image.tag | string | `"latest"` |  |
| internalPort | int | `8989` |  |
| name | string | `"sonarr"` |  |
| readinessProbe.failureThreshold | int | `3` |  |
| readinessProbe.httpGet.path | string | `"/"` |  |
| readinessProbe.httpGet.port | int | `8989` |  |
| readinessProbe.periodSeconds | int | `10` |  |
| replicaCount | int | `1` |  |
| resources.limits.memory | string | `"2Gi"` |  |
| resources.requests.cpu | float | `0.5` |  |
| resources.requests.memory | string | `"2Gi"` |  |
| timezone | string | `"America/Chicago"` |  |
| userId | int | `1000` |  |
| volumeMounts[0].mountPath | string | `"/config"` |  |
| volumeMounts[0].name | string | `"sonarr-config"` |  |
| volumeMounts[1].mountPath | string | `"/tv"` |  |
| volumeMounts[1].name | string | `"television-library"` |  |
| volumeMounts[2].mountPath | string | `"/downloads"` |  |
| volumeMounts[2].name | string | `"torrent-downloads"` |  |
| volumes[0].hostPath.path | string | `"/dev/net/tun"` |  |
| volumes[0].name | string | `"dev-net-tun"` |  |
| volumes[1].hostPath.path | string | `"/data"` |  |
| volumes[1].name | string | `"sonarr-config"` |  |
| volumes[2].hostPath.path | string | `"/data"` |  |
| volumes[2].name | string | `"television-library"` |  |
| volumes[3].hostPath.path | string | `"/data"` |  |
| volumes[3].name | string | `"torrent-downloads"` |  |

