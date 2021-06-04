# ombi

![Version: 1.1.0](https://img.shields.io/badge/Version-1.1.0-informational?style=flat-square) ![AppVersion: 1.0](https://img.shields.io/badge/AppVersion-1.0-informational?style=flat-square)

Ombi - Automatic downloader for movies :)

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| env[0].name | string | `"PUID"` |  |
| env[0].value | string | `"1000"` |  |
| env[1].name | string | `"PGID"` |  |
| env[1].value | string | `"1000"` |  |
| env[2].name | string | `"TZ"` |  |
| env[2].value | string | `"Europe/Paris"` |  |
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"linuxserver/ombi"` |  |
| image.tag | string | `"latest"` |  |
| ingress.annotations."cert-manager.io/cluster-issuer" | string | `"letsencrypt-prod"` |  |
| ingress.annotations."certmanager.k8s.io/cluster-issuer" | string | `"letsencrypt-prod"` |  |
| ingress.annotations."kubernetes.io/ssl-redirect" | string | `"true"` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0] | string | `"ombi.bananaspliff.org"` |  |
| ingress.path | string | `"/"` |  |
| ingress.tls[0].hosts[0] | string | `"ombi.bananaspliff.org"` |  |
| ingress.tls[0].secretName | string | `"ombi-bananaspliff-org"` |  |
| nodeSelector | object | `{}` |  |
| replicaCount | int | `1` |  |
| resources.limits.memory | string | `"1Gi"` |  |
| resources.requests.cpu | string | `"100m"` |  |
| resources.requests.memory | string | `"1Gi"` |  |
| service.port | int | `80` |  |
| service.type | string | `"ClusterIP"` |  |
| tolerations | list | `[]` |  |
| volumeMounts[0].mountPath | string | `"/config"` |  |
| volumeMounts[0].name | string | `"myvolume"` |  |
| volumeMounts[0].subPath | string | `"configs/ombi"` |  |
| volumes[0].name | string | `"myvolume"` |  |
| volumes[0].persistentVolumeClaim.claimName | string | `"myvolume"` |  |

