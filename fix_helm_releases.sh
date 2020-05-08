#!/bin/bash

set -e
set -o pipefail

# This script fixes helmcharts secrets that was deployed with API objects paths, that was deprecated.
# More info here https://github.com/helm/helm/issues/7219
# Use it own risks and only if your know what for is this!
# After exeecuting you need to perform redeploy
# This is fixed by Victor Yagofarov version of:
# https://github.com/helm/helm/issues/7219#issuecomment-590122046

NamespaceName=($(kubectl get ns -o json | jq '.items[].metadata.name' | tr -d '"'))
if [ -n "$1" ]
then
    unset NamespaceName
    NamespaceName=( $1 )
fi
resource="deployment.yaml"

for namespace in "${NamespaceName[@]}"
do :
    unset ReleaseName
    ReleaseName=($(helm -n $namespace ls -o json | jq '.[].name' | tr -d '"'))
    for release in "${ReleaseName[@]}"
    do :
        echo "Starting to fix k8s objects $(date -R)"
        mkdir -p /tmp/"$namespace"
        cd /tmp/"$namespace" || exit
        echo "Getting latest deployed helm release secret"
        kubectl config set-context --current --namespace="$namespace"

        kubectl --namespace="$namespace" get secret -l owner=helm,status=deployed,name="$release" -o yaml > "$namespace.$release.release.bak"
        cp "$namespace.$release.release.bak" "$namespace.$release.release"
        grep -oP '(?<=release: ).*' "$namespace"."$release".release | base64 -d | base64 -d | gzip -d - > "$namespace"."$release".release.data
        
        # Change that sed replacement to you case
        echo "Replacing wrong path in k8s API"
        sed -i '' "s#$resource\\\napiVersion: extensions/v1beta1#$resource\\\napiVersion: apps/v1#g" "$namespace"."$release".release.data
        
        echo "Encoding release back"
        gzip "$namespace.$release.release.data" --to-stdout | base64 | base64 > "$namespace.$release.release.data.fixed"
        FIXED_DATA=$(cat "$namespace.$release.release.data.fixed")
        
        echo "Replacing release in $namespace.$release.release yaml file"
        sed -i '' "s#release: .*#release: ${FIXED_DATA}#g" "$namespace"."$release".release
        
        echo "Applying fixed release"
        kubectl --namespace="$namespace" apply -f "$namespace"."$release".release
        
        echo "Helm release fixed. You need to perform redeploy"
    done
done
