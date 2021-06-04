# media-master

![Version: 0.4.2](https://img.shields.io/badge/Version-0.4.2-informational?style=flat-square)

A helm chart to manage your digital downloads

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| jackett.image.pullPolicy | string | `"Always"` |  |
| jackett.image.repository | string | `"linuxserver/jackett"` |  |
| jackett.image.tag | string | `"latest"` |  |
| jackett.internalPort | int | `9117` |  |
| jackett.name | string | `"jackett"` |  |
| jackett.resources.limits.memory | string | `"1Gi"` |  |
| jackett.resources.requests.cpu | float | `0.5` |  |
| jackett.resources.requests.memory | string | `"1Gi"` |  |
| jackett.volumeMounts[0].mountPath | string | `"/config"` |  |
| jackett.volumeMounts[0].name | string | `"jackett-config"` |  |
| jackett.volumeMounts[1].mountPath | string | `"/downloads"` |  |
| jackett.volumeMounts[1].name | string | `"torrent-downloads"` |  |
| radarr.image.pullPolicy | string | `"Always"` |  |
| radarr.image.repository | string | `"linuxserver/radarr"` |  |
| radarr.image.tag | string | `"latest"` |  |
| radarr.internalPort | int | `7878` |  |
| radarr.name | string | `"radarr"` |  |
| radarr.readinessProbe.httpGet.path | string | `"/"` |  |
| radarr.readinessProbe.httpGet.port | string | `"internal-port"` |  |
| radarr.readinessProbe.initialDelaySeconds | int | `120` |  |
| radarr.readinessProbe.periodSeconds | int | `15` |  |
| radarr.resources.limits.memory | string | `"2Gi"` |  |
| radarr.resources.requests.cpu | float | `0.5` |  |
| radarr.resources.requests.memory | string | `"2Gi"` |  |
| radarr.volumeMounts[0].mountPath | string | `"/config"` |  |
| radarr.volumeMounts[0].name | string | `"radarr-config"` |  |
| radarr.volumeMounts[1].mountPath | string | `"/movies"` |  |
| radarr.volumeMounts[1].name | string | `"movie-library"` |  |
| radarr.volumeMounts[2].mountPath | string | `"/downloads"` |  |
| radarr.volumeMounts[2].name | string | `"torrent-downloads"` |  |
| replicaCount | int | `1` |  |
| sonarr.image.pullPolicy | string | `"Always"` |  |
| sonarr.image.repository | string | `"gh0str1pp3r/sonarr"` |  |
| sonarr.image.tag | string | `"latest"` |  |
| sonarr.internalPort | int | `8989` |  |
| sonarr.name | string | `"sonarr"` |  |
| sonarr.readinessProbe.httpGet.path | string | `"/"` |  |
| sonarr.readinessProbe.httpGet.port | string | `"internal-port"` |  |
| sonarr.readinessProbe.initialDelaySeconds | int | `120` |  |
| sonarr.readinessProbe.periodSeconds | int | `15` |  |
| sonarr.resources.limits.memory | string | `"2Gi"` |  |
| sonarr.resources.requests.cpu | float | `0.5` |  |
| sonarr.resources.requests.memory | string | `"2Gi"` |  |
| sonarr.volumeMounts[0].mountPath | string | `"/config"` |  |
| sonarr.volumeMounts[0].name | string | `"sonarr-config"` |  |
| sonarr.volumeMounts[1].mountPath | string | `"/tv"` |  |
| sonarr.volumeMounts[1].name | string | `"television-library"` |  |
| sonarr.volumeMounts[2].mountPath | string | `"/downloads"` |  |
| sonarr.volumeMounts[2].name | string | `"torrent-downloads"` |  |
| timezone | string | `"America/Chicago"` |  |
| transmission_ovpn.env.LOCAL_NETWORK | string | `"10.233.0.0/18"` |  |
| transmission_ovpn.env.OPENVPN_CONFIG | string | `"Netherlands"` |  |
| transmission_ovpn.env.OPENVPN_PASSWORD | string | `"password"` |  |
| transmission_ovpn.env.OPENVPN_PROVIDER | string | `"PIA"` |  |
| transmission_ovpn.env.OPENVPN_USERNAME | string | `"p0000000"` |  |
| transmission_ovpn.image.pullPolicy | string | `"Always"` |  |
| transmission_ovpn.image.repository | string | `"haugene/transmission-openvpn"` |  |
| transmission_ovpn.image.tag | float | `2.6` |  |
| transmission_ovpn.internalPort | int | `9091` |  |
| transmission_ovpn.name | string | `"transmission-ovpn"` |  |
| transmission_ovpn.net_admin | bool | `true` |  |
| transmission_ovpn.resources.limits.memory | string | `"1Gi"` |  |
| transmission_ovpn.resources.requests.cpu | float | `0.25` |  |
| transmission_ovpn.resources.requests.memory | string | `"1Gi"` |  |
| transmission_ovpn.volumeMounts[0].mountPath | string | `"/data"` |  |
| transmission_ovpn.volumeMounts[0].name | string | `"torrent-downloads"` |  |
| userId | int | `1000` |  |
| volumes[0].hostPath.path | string | `"/dev/net/tun"` |  |
| volumes[0].name | string | `"dev-net-tun"` |  |
| volumes[1].hostPath.path | string | `"/data"` |  |
| volumes[1].name | string | `"sonarr-config"` |  |
| volumes[2].hostPath.path | string | `"/data"` |  |
| volumes[2].name | string | `"television-library"` |  |
| volumes[3].hostPath.path | string | `"/data"` |  |
| volumes[3].name | string | `"radarr-config"` |  |
| volumes[4].hostPath.path | string | `"/data"` |  |
| volumes[4].name | string | `"movie-library"` |  |
| volumes[5].hostPath.path | string | `"/data"` |  |
| volumes[5].name | string | `"jackett-config"` |  |
| volumes[6].hostPath.path | string | `"/data"` |  |
| volumes[6].name | string | `"torrent-downloads"` |  |

