#!/usr/bin/env bash

str=""

if [ $(expr $1 % 3) = 0 ]
then
	str+=Pling
fi

if [ $(expr $1 % 5 ) = 0 ]
then
	str+=Plang
fi

if [ $(expr $1 % 7  ) = 0 ]
then
	str+=Plong
fi

if [ ! $str ]; then
	echo $1
else
	echo $str
fi
