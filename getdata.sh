cookie=$(cat ~/aoctoken)
curl https://adventofcode.com/2024/day/$1/input -H "Cookie: $cookie" > data/day$1.txt
