# locust

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square)

A chart for load testing a url

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"tstapler/locust-tasks"` |  |
| image.tag | string | `"latest"` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| targetUrl | string | `"https://fakeurl.this.doesnt.exist.com"` |  |
| workerReplicas | int | `10` |  |

