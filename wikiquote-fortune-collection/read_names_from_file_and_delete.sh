while IFS='' read -r line || [[ -n "$line" ]]; do
  rm $line
done < "$1"
