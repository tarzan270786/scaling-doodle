#!/usr/bin/perl 

$msg=<<"END_MESSAGE";
Oracle Home directories present in the work directory
If you want to restore the env, set RESTORE_CEN_POD=TRUE and rerun
otherwise, clean the view using servicekill and clntest before starting
END_MESSAGE
print "$msg\n";
