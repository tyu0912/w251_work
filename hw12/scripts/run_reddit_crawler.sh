i=0
for f in reddit_urls/*.txt; do

  python3 reddit_crawler.py --url $f &
  
  i=$((i+1))
  echo $i

  if [ $i -ge 4 ] 
  then
    i=0   
    wait $!
  fi

done 2>/dev/null
