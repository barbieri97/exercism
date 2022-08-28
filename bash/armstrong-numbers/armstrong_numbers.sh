#!/usr/bin/bash

# declarando variaveis globais
declare -a arr_dec
declare -i length="${#1}"

# função para separar o numero em um array. ex: 154 = (1 5 4)
decimais () { 
    declare -i num="$1"
    declare -i mult=10
    for (( i=0;i<"$length";i++ ));
        do
            arr_dec[i]=$(( "$num" % "$mult" ))  # essa linha pega o ultimo digito do numero e coloca na lista
            (( num/=10 )) # essa linha remove o ultimo digito do numero já que o bash só faz divisões inteiras
        done
}

main (){
    declare -i resultado=0
    for item in "${arr_dec[@]}"
        do
            expon=$(( item**length ))
            ((resultado+=expon))
        done
    [[ "$resultado" == "$1" ]] && echo "true" || echo "false"
}

decimais "$1"
main "$1"