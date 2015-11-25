BLOCKDB="/root/ip.block"
IPS=$(grep -Ev "^#" $BLOCKDB)
for i in $IPS
do
iptables -A INPUT -s $i -j DROP
iptables -A OUTPUT -d $i -j DROP
done
