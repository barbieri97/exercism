#!/usr/bin/env bash

function main {
if [ $# = 1 ];
then
	echo "Hello, $1"
	return 0
else
	echo "Usage: error_handling.sh <person>"
	exit 2
fi
}

main "$@"
