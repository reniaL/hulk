killProcessByCommandName() {
    commandName=$1
    pid=$(ps -ef | grep "$commandName" | grep -v grep | awk '{print $2}')
    pidCount=$(echo $pid | wc -w)

    if [ $pidCount = "0" ]; then
        echo "no process found: $commandName"
    elif [ $pidCount != "1" ]; then
        echo -e "pid not unique:\n$pid"
        exit 1
    else
        echo "found pid: $pid"
        kill $pid
        checkProcessKilled $commandName
        echo "$pid is killed"
    fi
}