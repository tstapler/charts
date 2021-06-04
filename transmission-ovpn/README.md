# transmission-ovpn

![Version: 1.2.0](https://img.shields.io/badge/Version-1.2.0-informational?style=flat-square)

A chart for deploying https://github.com/haugene/docker-transmission-openvpn

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| env.CREATE_TUN_DEVICE | bool | `true` |  |
| env.DOCKER_LOG | bool | `true` |  |
| env.LOCAL_NETWORK | string | `"10.233.0.0/18"` |  |
| env.OPENVPN_CONFIG | string | `"Netherlands"` |  |
| env.OPENVPN_PASSWORD | string | `"password"` |  |
| env.OPENVPN_PROVIDER | string | `"PIA"` |  |
| env.OPENVPN_USERNAME | string | `"p0000000"` |  |
| env.PIA_OPENVPN_CONFIG_BUNDLE | string | `"openvpn"` |  |
| env.TRANSMISSION_SCRIPT_TORRENT_DONE_ENABLED | bool | `true` |  |
| env.TRANSMISSION_SCRIPT_TORRENT_DONE_FILENAME | string | `"/scripts/unrar.sh"` |  |
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"haugene/transmission-openvpn"` |  |
| image.tag | string | `"3.1"` |  |
| internalPort | int | `9091` |  |
| name | string | `"transmission-ovpn"` |  |
| net_admin | bool | `true` |  |
| readinessProbe.exec.command[0] | string | `"/etc/scripts/healthcheck.sh"` |  |
| readinessProbe.initialDelaySeconds | int | `120` |  |
| readinessProbe.periodSeconds | int | `120` |  |
| replicaCount | int | `1` |  |
| timezone | string | `"America/Chicago"` |  |
| userId | int | `1000` |  |
| volumeMounts[0].mountPath | string | `"/data"` |  |
| volumeMounts[0].name | string | `"torrent-downloads"` |  |

