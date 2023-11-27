#! /bin/bash
THIS_DIR=$(pwd)
SCRIPT_DIR=`dirname -- "$0"`
MODEL_DIR=$THIS_DIR/model
MODEL_VERSIONING_ENABLED=$1

cd $SCRIPT_DIR

#load model metadata
model_name=$(jq -r '.name' model_version.json)
model_version=$(jq -r '.version' model_version.json)

#construct request uri and get S3 link into json file
mlflow_download_uri="http://ml-flow/api/2.0/mlflow/model-versions/get-download-uri?name=${model_name}&version=${model_version}"
curl "${mlflow_download_uri}" >> artifact.json

#print the link for debugging purposes and extract uri
cat artifact_uri.json
artifact_uri=$(jq -r '.artifact_uri' artifact_uri.json)

#copy files from S3
mkdir -p $MODEL_DIR
aws s3 cp "${artifact_uri}" $MODEL_DIR --recursive

cd $THIS_DIR