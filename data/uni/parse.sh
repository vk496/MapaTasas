#!/bin/bash

echo "unis:"
for i in $(seq 1 77); do
    echo -n "- siglas: "
    yq r u.yml "unis.$i.siglas"

    echo -n "  nombre: "
    yq r u.yml "unis.$i.nombre"

    echo -n "  tipo: "
    yq r u.yml "unis.$i.tipo"

    echo -n "  provincia: "
    yq r u.yml "unis.$i.provincia"

    echo -n "  web: "
    yq r u.yml "unis.$i.url"

    echo "  lugares:"
    echo -n "    - campus: "
    yq r u.yml "unis.$i.campus"

    echo "      titulaciones:"
    echo "        - tipo: grado"
    echo -n "          centro: "
    yq r u.yml "unis.$i.centro"

    echo "          titulación: "
    #echo "          convenios:" #TODO

    echo "          tasas:"
    

    for a in $(seq 2011 2015); do
        echo "            - año: $a"
        echo "              tipo: precio_por_crédito"
        echo -n "              fuente: "
        yq r u.yml "unis.$i.tasas_$a.url"

        echo "              cantidades:"
        
        for z in $(seq 1 4); do
            echo -n "                tasas$z: "
            yq r u.yml "unis.$i.tasas_$a.tasas$z"
        done


    done


    #yq r u.yml "unis.$i.centro"

done