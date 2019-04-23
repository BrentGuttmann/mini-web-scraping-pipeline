#!/bin/bash

:'-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_

This script is designed to take two optional numeric arguments.
The first argument specifies the starting stage of the pipeline.
The second argument specifies the stopping stage of the pipeline.
By default, the pipeline will start at stage 0 and end at the
final stage.

-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^'

###################################################################
#1. Check Argument Types
###################################################################

#1.1. Set default values for starting and stopping pipeline stages
init_stage=0
last_stage=99999

#1.2. Check if single-argument case has a numeric argument
if [[ $# -eq 1 ]]; then
    re='^[0-9]+$'
    if ! [[ $1 =~ $re ]]; then
        echo "error: arg is not a number " >&2
        return 1
    fi
    init_stage=$1
fi

#1.3. Check two-arg case are increasing integers
if [[ $# -ge 2 ]]; then
    # Check both args are numbers
    re='^[0-9]+$'
    if ! [[ $1 =~ $re ]] || ! [[ $2 =~ $re ]]; then
        echo "error: args not both numbers " >&2
        return 1
    fi
    # Check 2nd arg is >= 1st arg
    if [[ $1 -gt $2 ]]; then
        echo "The first argument must be less than the second" >&2
        return 1
    else
        init_stage=$1
        last_stage=$2
    fi
fi

###################################################################
#2. Print what stages are to be processed
###################################################################

end_message='END'

if [[ $last_stage -lt 99999 ]]; then
    end_message=$last_stage
fi

clear
echo '''
    =========================
        STARTING PIPELINE
    =========================


    RUNNING STAGES:   '$init_stage' - '$end_message'
'''

###################################################################
#3. Begin Pipeline
###################################################################

if [[ $init_stage -le 0 && $last_stage -ge 0 ]]; then

    # Make sure output data directory exists for this stage
    if [[ ! -d pipeline3/data1 ]]; then mkdir pipeline3/data1; fi

    # ...
    echo '''
        <<< STAGE 0 >>>
    '''
    python pipeline3/stage0.py
fi

if [[ $init_stage -le 0 && $last_stage -ge 0 ]]; then

    # Make sure output data directory exists for this stage
    if [[ ! -d pipeline3/data2 ]]; then mkdir pipeline3/data2; fi

    # ...
    echo '''
        <<< STAGE 1 >>>
    '''
    python pipeline3/stage1.py
fi

###################################################################
#4. Finish
###################################################################

echo '''
    ==========================
        FINISHING PIPELINE
    ==========================
'''
