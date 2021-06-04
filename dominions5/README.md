# dominions5

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![AppVersion: 1.0](https://img.shields.io/badge/AppVersion-1.0-informational?style=flat-square)

A Helm chart for deploying a dominions5 server to Kubernetes. The included 'args_generator.py' script assists with setting the right values for a game of dominions.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| discordSidecar.channel | string | `""` |  |
| discordSidecar.enabled | bool | `true` |  |
| discordSidecar.image.pullPolicy | string | `"IfNotPresent"` |  |
| discordSidecar.image.repository | string | `"tstapler/dom5_helper"` |  |
| discordSidecar.image.tag | string | `"latest"` |  |
| discordSidecar.resources.limits.memory | string | `"256Mi"` |  |
| discordSidecar.resources.requests.memory | string | `"256Mi"` |  |
| discordSidecar.token | string | `""` |  |
| gameArgs[0] | string | `"--textonly"` |  |
| gameArgs[1] | string | `"--nosteam"` |  |
| gameArgs[2] | string | `"--statusdump"` |  |
| gameArgs[3] | string | `"--statfile"` |  |
| gameArgs[4] | string | `"--scoredump"` |  |
| gameArgs[5] | string | `"--era"` |  |
| gameArgs[6] | string | `"2"` |  |
| gameName | string | `""` |  |
| gameVolumes | list | `[]` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"tstapler/dominions5-base"` |  |
| image.tag | string | `"latest"` |  |
| nodeSelector | object | `{}` |  |
| port | int | `9999` |  |
| replicaCount | int | `1` |  |
| resources.limits.memory | string | `"512Mi"` |  |
| resources.requests.memory | string | `"512Mi"` |  |
| tolerations | list | `[]` |  |

