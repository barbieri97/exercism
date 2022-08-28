#!/bin/bash

function assert_args {
	[ $# != 2 ] && echo "Usage: hamming.sh <string1> <string2>" && exit 2
}

function same_lenght {
	arg1=$( echo -n $1 | wc -m )
	arg2=$( echo -n $2 | wc -m )
	[ $arg1 != $arg2  ] && echo "strands must be of equal length" && exit 2

}

function str2array {
	array1=()
	array2=()	
	len_str=$( echo -n $1 | wc -m  )
	len_str=$(( len_str-1  ))
	for item in $(seq 0 $len_str); do
		array1[ $item ]="${1:item:1}"
		array2[ $item ]="${2:item:1}"
	done
}

function compare_str {
	distance=0
	for i in "${!array1[@]}"
	do
		[ ${array1[i]} != ${array2[i]}  ] && distance=$(( $distance+1  ))
	done
	echo $distance
}


assert_args "$@"
same_lenght "$@"
str2array "$@"
compare_str
