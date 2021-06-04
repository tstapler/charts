# radarr

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square)

Radarr - An application for downloading movies over Usenet and Bittorrent

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"linuxserver/radarr"` |  |
| image.tag | string | `"latest"` |  |
| internalPort | int | `7878` |  |
| name | string | `"radarr"` |  |
| readinessProbe.failureThreshold | int | `3` |  |
| readinessProbe.httpGet.path | string | `"/"` |  |
| readinessProbe.httpGet.port | int | `7878` |  |
| readinessProbe.periodSeconds | int | `10` |  |
| replicaCount | int | `1` |  |
| resources.limits.memory | string | `"2Gi"` |  |
| resources.requests.cpu | float | `0.5` |  |
| resources.requests.memory | string | `"2Gi"` |  |
| timezone | string | `"America/Chicago"` |  |
| userId | int | `1000` |  |
| volumeMounts[0].mountPath | string | `"/config"` |  |
| volumeMounts[0].name | string | `"radarr-config"` |  |
| volumeMounts[1].mountPath | string | `"/movies"` |  |
| volumeMounts[1].name | string | `"movie-library"` |  |
| volumeMounts[2].mountPath | string | `"/downloads"` |  |
| volumeMounts[2].name | string | `"torrent-downloads"` |  |
| volumes[0].hostPath.path | string | `"/data"` |  |
| volumes[0].name | string | `"radarr-config"` |  |
| volumes[1].hostPath.path | string | `"/data"` |  |
| volumes[1].name | string | `"movie-library"` |  |

