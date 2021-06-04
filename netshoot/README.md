# netshoot

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square)

A Helm Chart for deploying netshoot as a daemonset. Netshoot is a Docker + Kubernetes network trouble-shooting swiss-army container. https://github.com/nicolaka/netshoot

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"nicolaka/netshoot"` |  |
| image.tag | string | `"latest"` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |

