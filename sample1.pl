#!/usr/bin/perl

my $a=5; #Change values to 11,2,5 and observe output
if($a<10){
  print "Inside 1st if block";
        if($a<5){
                print "Inside 2nd if block --- The value is $a\n";
        }
        else{
                print " Inside 2nd else block --- The value is $a\n";
        }
	}
	else{
        	print "Inside 1st else block – The value is $a\n";
    }
