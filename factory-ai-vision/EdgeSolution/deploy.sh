#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# echo "${DIR}"

INFERENCE_MODULE_FILE="${DIR}"/modules/InferenceModule/module.json
WEB_MODULE_FILE="${DIR}"/modules/WebModule/module.json

INFERENCE_MODULE_VERSION=$(cat "${INFERENCE_MODULE_FILE}" | jq '.image.tag.version' |  sed -e 's/^"//' -e 's/"$//')
WEB_MODULE_VERSION=$(cat "${WEB_MODULE_FILE}" | jq '.image.tag.version' |sed -e 's/^"//' -e 's/"$//')

echo $INFERENCE_MODULE_FILE
echo $WEB_MODULE_FILE


# Check module change
if [[ ! $(git log -1 --oneline "${DIR}"/modules/InferenceModule | grep 'new version by deploy.sh') ]]; then
	echo "Inference module change"
	INFERENCE_MODULE_NEW_VERSION=$(echo "${INFERENCE_MODULE_VERSION}" | perl -pe 's/^((\d+\.)*)(\d+)(.*)$/$1.($3+1).$4/e' )
	echo "Inference module version: ${INFERENCE_MODULE_VERSION} => ${INFERENCE_MODULE_NEW_VERSION}"
	cat "${INFERENCE_MODULE_FILE}" | jq ".image.tag.version= \"${INFERENCE_MODULE_NEW_VERSION}\"" > ${INFERENCE_MODULE_FILE}.tmp
	mv ${INFERENCE_MODULE_FILE}.tmp ${INFERENCE_MODULE_FILE}
	git add ${INFERENCE_MODULE_FILE} 
else
	echo "Inference module not changed"
fi

if [[ ! $(git log -1 --oneline "${DIR}"/modules/WebModule | grep 'new version by deploy.sh') ]]; then
	echo "Web module change"
	WEB_MODULE_NEW_VERSION=$(echo "${WEB_MODULE_VERSION}" | perl -pe 's/^((\d+\.)*)(\d+)(.*)$/$1.($3+1).$4/e' )
	echo "Web module version: ${WEB_MODULE_VERSION} => ${WEB_MODULE_NEW_VERSION}"
	cat "${WEB_MODULE_FILE}" | jq ".image.tag.version= \"${WEB_MODULE_NEW_VERSION}\"" > ${WEB_MODULE_FILE}.tmp
	mv ${WEB_MODULE_FILE}.tmp ${WEB_MODULE_FILE}
	git add ${WEB_MODULE_FILE} 
else
	echo "Web module not changed"
fi

git commit -m "new version by deploy.sh"



docker build  --rm -f "${DIR}/modules/InferenceModule/Dockerfile.cpuamd64" -t mycapreg.azurecr.io/intelligentedge/inferencemodule:${INFERENCE_MODULE_NEW_VERSION}-cpuamd64 "${DIR}/modules/InferenceModule"
docker push mycapreg.azurecr.io/intelligentedge/inferencemodule:${INFERENCE_MODULE_NEW_VERSION}-cpuamd64
 
docker build  --rm -f "${DIR}/modules/WebModule/Dockerfile.amd64" -t mycapreg.azurecr.io/intelligentedge/visionwebmodule:${WEB_MODULE_NEW_VERSION}-amd64 "${DIR}/modules/WebModule"
docker push mycapreg.azurecr.io/intelligentedge/visionwebmodule:${WEB_MODULE_NEW_VERSION}-amd64

DEPLOY_FILE="${DIR}/config/deployment.cpu.amd64.json"

sed "s/visionwebmodule.*$/visionwebmodule:${WEB_MODULE_NEW_VERSION}-amd64/g" "${DEPLOY_FILE}"
sed "s/inferencemodule.*$/inferencemodule:${INFERENCE_MODULE_NEW_VERSION}-cpuamd64/g" "${DEPLOY_FILE}"
