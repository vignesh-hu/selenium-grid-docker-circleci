#!/bin/sh

# function help()
# {
#     echo "Usage: $0 [-b|--browser] <browser_name> [-p|--path] <path/to/tests> [-t|--test] <test_name> [-e|--environment] <local/ci>"
#     echo ""
#     echo "Options:"
#     echo "  -b, --browser 		set browser name"
#     echo "  -p, --path 			path to tests directory or directly to test file"
#     echo "  -t, --test 			name of test or name pattern"
#     echo "  -e, --environment		set environment local or CI (key is not necessary if CI)"
#     echo "  -h, --help 			display this help"
#     echo ""
#     echo "Examples:"
#     echo "  $0 -b chrome -p Tests/ -t test_login -e local"
#     echo "  $0 -b firefox -p Tests/"
#     exit 0
# }

while test $# -gt 0; do
    case $1 in
    	-b|--browser)
    		shift
            if test $# -gt 0; then
         		BROWSER_NAME="$1"
         	fi
            ;;
	    -p|--path) 
			shift
            if test $# -gt 0; then
            	TESTS_DIR_OR_FILE="$1"
            fi
	        ;;
        -t|--test) 
			shift
            if test $# -gt 0; then
				TEST_TO_RUN="-k $1"
			fi
            ;;
        -e|--environment) 
			shift
            if test $# -gt 0; then
				ENV="$1"
			fi
            ;;
	    *) echo "Unknown option $1."
            exit 1
            ;;
    esac
    shift
done

export BROWSER="$BROWSER_NAME"
export ENVIRONMENT="$ENV"

pytest -v "$TESTS_DIR_OR_FILE" "$TEST_TO_RUN"

exit 0