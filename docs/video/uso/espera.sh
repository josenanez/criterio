#!/bin/bash
# Espera a que la terminal de la toma esté quieta 6 s o pida una decisión, y muestra el final de la pantalla.
#   uso/espera.sh <toma> [segundos máximos] [líneas]
toma=$1; max=${2:-300}; sleep 8
for i in $(seq 1 "$max"); do
  p=$(cat "$toma/ctl/pantalla.txt" 2>/dev/null)
  q=$(printf '%s' "$p" | tail -1 | sed -nE 's/.*quieta ([0-9]+) s.*/\1/p'); q=${q:-0}
  if printf '%s' "$p" | grep -q "Esc to cancel"; then break; fi
  if [ "$q" -ge 6 ] && ! printf '%s' "$p" | grep -q "esc to interrupt"; then break; fi
  sleep 1
done
python3 "$(dirname "$0")/sesion.py" "$toma" pantalla | grep -v "^$" | tail -"${3:-30}"
