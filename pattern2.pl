#!/usr/bin/perl

use strict;
use warnings;

my $string = "com.T.tutorialpoint.perl 5.8.1.2345 TTT //";

if ($string =~ /perl/){
	print "Matched\n";
}
if ($string !~ /python/){
	print "Not matched \n";
}
if ($string =~ m/\/\//){ # \ is to suppress the meaning and m is to chnage the delimter 
	print "Matched\n";
}
if ($string =~ m{//}){# same as above 
	print "\/\/  matched \n";
}
if ($string =~ /perl/){
	print "Matched\n";
}
if ($string !~ /python/){
	print "Not matched \n";
}
