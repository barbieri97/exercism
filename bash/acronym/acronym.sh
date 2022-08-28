#!/usr/bin/env bash

# confere se foi passado o numero de parametros corretos para o script
assert_param(){
    [[ $# != 1 ]] && echo "usage: bash acronym.sh \"<string>\"" && exit 2
}

# transforma a string em um array e coloca as letras em maiusculas
str2array(){
    readarray -d " " acr <<< ${var^^}
}

# cria o acronimo
create_acronym(){
    a=""
    for item in ${acr[@]};
        do
        a+=${item:0:1};
        done
        echo $a
}

# troca os caracteres especiais para espaço
replace_especial_caracteres(){
    especial_carac=('-' "." "_" "*")
    set -f 
    var=$1
    for item in ${especial_carac[@]};
        do
        var=${var//"$item"/" "}
        echo $var
        done
}

main(){
    assert_param "$@"
    replace_especial_caracteres "$@"
    str2array
    create_acronym
}

main "$@"