#!/usr/bin/perl

open(FILEHANDLER , "sanity_final_DWCSSEED.log");

my @content = <FILEHANDLER>;

foreach(@content){
	print "$_";
}
close(FILEHANDLER);
