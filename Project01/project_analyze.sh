#!/bin/bash
cd ..
echo "Please type in the function that you want"
echo "For the list of the functions,please check TODO"
echo "For removing temporary,please check rmtemp"
echo "To find all the commit hashes that merge is mentioned, type in mergelog"
echo "To exit, type in exit"
echo "To check whether the current user is running the program, type usercheck"
read -p "You have typed:" func
echo "Processing,please wait,you have typed:" $func

while [ $func != "exit" ]
do
	if [ $func = "TODO" ];then
		grep -r --exclude="todo.log" "#TODO" > ~/CS1XA3/todo.log
	elif [ $func = "mergelog" ];then
			rm -f "merge.log"
		log=`git log --oneline`
		while read -r somerandombalabala;do
			if [[ ! -z `echo $somerandombalabala | grep "Merge"` ]]; then
				hashes=`echo $somerandombalabala | cut -d " " -f 1`
				echo $hashes >> merge.log
				echo "Founded! $hashes"
			fi
		done <<< $log
		echo "Merge is finished"
	elif [ $func = "usercheck" ];then
		echo "Please enter your username:"
		read username
		truename=$(whoami)
		if test $username = $truename;then
			echo "The user is online"
		else
			echo "The user is offline"
		fi
	elif [ $func = "rmtemp" ];then
	somefile=$(git ls-files . --exclude-standard --others)
	for files in $somefile
	do
		if [[ "$files" == *.tmp ]];then
			echo "removing temporary files"
			rm $files
		fi
	done
	else
		echo "No exisited command match, please retry"
	fi
	read -p "Type in another command:" func
	echo "Processsing, please wait" $func
done
unset func
exit

