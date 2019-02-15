#!/bin/bash
cd ..
echo "Please type in the function that you want"
echo "For the list of the functions,please check TODO"
echo "For removing temporary,please check rmtemp"
echo "To exit, type in exit"
read -p "You have typed:" func
echo "Processing,please wait,you have typed:" $func

while [ $func != "exit" ]
do
	if [ $func = "TODO" ];then
		cp /dev/null ~/CS1XA3/Project01/todo.log
		if [ -e "todo.log" ]
		then
			rm todo.log
		fi
		checklist=$( git ls-files )
		for note in $checklist
		do
			while IFS= read line
			do
				echo "$line #TODO" >> ~/CS1XA3/Project01/todo.log
			done < $note
		done
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

