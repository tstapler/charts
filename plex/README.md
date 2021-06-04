# plex

![Version: 0.3.2](https://img.shields.io/badge/Version-0.3.2-informational?style=flat-square)

A chart for deploying plex (https://plex.tv) to kubernetes

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"plexinc/pms-docker"` |  |
| image.tag | string | `"latest"` |  |
| ingress.enabled | bool | `true` |  |
| ingress.hosts[0] | string | `"plex.staplerstation.com"` |  |
| plexClaim | string | `"claim-something"` |  |
| resources.limits.memory | string | `"4Gi"` |  |
| resources.requests.cpu | int | `2` |  |
| resources.requests.memory | string | `"2Gi"` |  |
| service.name | string | `"plex"` |  |
| service.type | string | `"ClusterIP"` |  |
| tz | string | `"America/Chicago"` |  |
| volumeMounts[0].mountPath | string | `"/config"` |  |
| volumeMounts[0].name | string | `"plex-config"` |  |
| volumeMounts[1].mountPath | string | `"/data/movies"` |  |
| volumeMounts[1].name | string | `"plex-movies"` |  |
| volumes[0].hostPath.path | string | `"/data"` |  |
| volumes[0].name | string | `"plex-config"` |  |
| volumes[1].hostPath.path | string | `"/data"` |  |
| volumes[1].name | string | `"plex-movies"` |  |

