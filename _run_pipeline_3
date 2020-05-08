#!/bin/bash

###################################################################
# 1. Check Argument Types
###################################################################

#1.1. Set default values for starting and stopping pipeline stages
init_stage=1
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
# 2. Print what stages are to be processed
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
# 3. Begin Pipeline
###################################################################

if [[ $init_stage -le 1 && $last_stage -ge 1 ]]; then

    # Make sure output data directory exists for this stage
    if [[ ! -d pipeline3/data1 ]]; then mkdir pipeline3/data1; fi

    # Run chrome locally with selenium; add arg `headless` to run in headless mode
    echo '''
        <<< STAGE 1 >>>
    '''
    # python pipeline3/stage1.py headless
    python pipeline3/stage1.py
fi

if [[ $init_stage -le 2 && $last_stage -ge 2 ]]; then

    # Make sure output data directory exists for this stage
    if [[ ! -d pipeline3/data2 ]]; then mkdir pipeline3/data2; fi

    # ...
    echo '''
        <<< STAGE 2 >>>
    '''
    python pipeline3/stage2.py
fi

###################################################################
# 4. Finish
###################################################################

echo '''
    ==========================
        FINISHING PIPELINE
    ==========================
'''
