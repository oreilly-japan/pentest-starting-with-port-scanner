#!/bin/sh
set -eu

# ヘルプメッセージを定義
usage() {
  echo "Usage: ${0##*/} -T<0-5> \
<target-hosts.txt> <exclude-hosts.txt>"
}

# コマンドライン引数がなにも無い場合にエラーメッセージを出力する
if [ "$#" -eq 0 ]; then
  echo "Error: Target hosts must be specified"
  usage
  exit 1
fi

if [ "$1" = "-h" ]; then
  usage
  exit 0
fi

today=`date +%Y%m%d` # フォルダ名に使用するための日付を取得する
# 結果を格納するフォルダがなければ作成する
if [ ! -d ./results/${today} ]; then
  mkdir -p ./results/${today}
fi

# 出力するファイル名に使用するための日時を取得する
now=`date +%Y%m%d_%H%M%S`

# 引数を変数に格納
timing_template=$1
hosts=`cat $2`
echo "Target: ${hosts}"

if [ "$#" -eq 3 ]; then
  exclude_hosts=`cat $3`
  echo "Exclude Hosts: ${exclude_hosts}"
  exclude_option="--exclude ${exclude_hosts}"
else
  exclude_option=""
fi

for h in $hosts
do
  # フォルダ名に使用するためCIDR表記の/を_に置換
  host_name=`echo $h | tr "/" "_"`
  # TCP SYN Pingによってホストを発見し、SYNスキャンを行う
  # 結果はXMLファイルとTXTファイルで出力する
  # SYNスキャンで結果がうまく取れない場合、-sSを-sTに変更し、
  # TCP Connectスキャンに切り替える
  echo "Now Launching: sudo nmap ${exclude_option} -v -n \
-p- -PS22,80,443 -sS --host-timeout 30m \
-oX ./results/${today}/${host_name}_syn_ping_${now}.xml \
-oN ./results/${today}/${host_name}_syn_ping_${now}.txt ${h}"

  sudo nmap ${timing_template} ${exclude_option} -v -n \
-p- -PS22,80,443 -sS --host-timeout 30m \
-oX ./results/${today}/${host_name}_syn_ping_${now}.xml \
-oN ./results/${today}/${host_name}_syn_ping_${now}.txt ${h}
done
