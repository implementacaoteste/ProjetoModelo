#!/bin/bash
# wait-for-it.sh
# Espera até que um host/porta esteja disponível antes de continuar

set -e

host="$1"
port="$2"
timeout=30

usage() {
  echo "Uso: $0 host:porta [-t timeout] [-- comando args]"
  echo "  -t TIMEOUT  Timeout em segundos, padrão é $timeout segundos"
  echo "  -- COMANDO   Comando para executar após o host/porta estar disponível"
  exit 1
}

while [[ $# -gt 0 ]]
do
  case "$1" in
    *:* )
    hostport=(${1//:/ })
    host="${hostport[0]}"
    port="${hostport[1]}"
    shift 1
    ;;
    -t)
    timeout="$2"
    if [[ $timeout == "" ]]; then break; fi
    shift 2
    ;;
    --)
    shift
    cliargs="$@"
    break
    ;;
    * )
    echo "Argumento desconhecido: $1"
    usage
    ;;
  esac
done

command="nc -zvw${timeout} $host $port"

echo "Aguardando por $host:$port..."

while ! eval "$command" >/dev/null 2>&1; do
  sleep 1
done

echo "Host $host:$port está disponível agora!"

if [[ -n $cliargs ]]; then
  exec "$cliargs"
fi
