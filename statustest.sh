#!/bin/bash

patience=10

read -t "$patience" -p "Press 'Enter' if you run Unix or Linux, otherwise press 'ctrl+d' "

status="$?"

if [[ $status -eq 0 ]]
then
 echo "That's great :-)"
elif [[ $status -eq 1 ]]
then
 echo "(exit status=$status)
You are welcome to try Unix or Linux :-)"
else
 echo "(exit status=$status)
You did not answer within $patience seconds. Anyway :-)"
fi
echo "'Unix & Linux' is a question/answer web site for
Unix and Linux operating systems"
