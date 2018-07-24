#!/bin/sh

IMAGE_NAME="sklearn-server"
VERSION=`cat version.txt`
if [ -n "$CIRCLECI" ]; then
    if [ "$CIRCLE_BRANCH" != "master" ]; then
        BRANCH_NAME="-$CIRCLE_BRANCH"
    fi
    BUILD_ID="$BRANCH_NAME+$CIRCLE_BUILD_NUM"
else
    BUILD_ID="-$USER"
fi

docker build -t $IMAGE_NAME:$VERSION$BUILD_ID .
