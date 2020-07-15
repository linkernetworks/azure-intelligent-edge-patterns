#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "${DIR}"

INFERENECE_MODULE_FILE="${DIR}"/modules/InferenceModule/module.json
WEB_MODULE_FILE="${DIR}"/modules/WebModule/module.json

INFERENECE_MODULE_VERSION=$(cat "${INFERENECE_MODULE_FILE}" | jq '.image.tag.version')
WEB_MODULE_VERSION=$(cat "${WEB_MODULE_FILE}" | jq '.image.tag.version')

echo $INFERENECE_MODULE_FILE
echo $WEB_MODULE_FILE


# Check module change
if [[ $(git status ${DIR}/modules/InferenceModule --porcelain) ]]; then
	echo -n "Inference module version:"
	echo -n ${INFERENECE_MODULE_VERSION}
	echo "=>" $(echo "${INFERENECE_MODULE_VERSION}" | perl -pe 's/^((\d+\.)*)(\d+)(.*)$/$1.($3+1).$4/e' )
else
	echo "Inference module not changed"
fi

if [[ $(git status ${DIR}/modules/WebModule --porcelain) ]]; then
	echo -n "WebModule module version:"
	echo "WEB_MODULE_VERSION:" $WEB_MODULE_VERSION
	echo "=>" $(echo "${WEB_MODULE_VERSION}" | perl -pe 's/^((\d+\.)*)(\d+)(.*)$/$1.($3+1).$4/e' )
else
	echo "Web module not changed"
fi


# export INFERENECE_MODULE_VERSION="${INFERENECE_MODULE_VERSION}"
# echo "${INFERENECE_MODULE_VERSION}" | awk 

# sed "s/\"version\":.*$/\"version\": ${INFERENECE_MODULE_VERSION}/g" "${INFERENECE_MODULE_FILE}" > "${INFERENECE_MODULE_FILE}"
# sed "s/\"version\":.*$/\"version\": ${WEBMODULE_MODULE_VERSION}/g" "${WEB_MODULE_FILE}" > "${WEB_MODULE_FILE}"

# docker build  --rm -f "${DIR}/modules/InferenceModule/Dockerfile.cpuamd64" -t mycapreg.azurecr.io/intelligentedge/inferencemodule:${INFERENECE_MODULE_VERSION}-cpuamd64 "${DIR}/modules/InferenceModule"
# docker push mycapreg.azurecr.io/intelligentedge/inferencemodule:${INFERENECE_MODULE_FILE}-cpuamd64
 
# docker build  --rm -f "${DIR}/modules/WebModule/Dockerfile.amd64" -t mycapreg.azurecr.io/intelligentedge/visionwebmodule:${WEBMODULE_MODULE_VERSION}-amd64 "${DIR}/modules/WebModule"
# docker push mycapreg.azurecr.io/intelligentedge/visionwebmodule:${WEBMODULE_MODULE_VERSION}-amd64

# DEPLOY_FILE="${DIR}/config/deployment.cpu.amd64.json"

# sed "s/visionwebmodule.*$/visionwebmodule:${WEB_MODULE_VERSION}-amd64/g" "${DEPLOY_FILE}"
# sed "s/inferencemodule.*$/inferencemodule:${INFERENECE_MODULE_VERSION}-cpuamd64/g" "${DEPLOY_FILE}"
